import asyncio
import logging
from asyncio import iscoroutinefunction
from logging import Logger
from typing import Callable, Any, List, cast

from plugp100.api.base_tapo_device import _BaseTapoDevice
from plugp100.api.hub.hub_device_tracker import (
    HubConnectedDeviceTracker,
    HubDeviceEvent,
)
from plugp100.api.tapo_client import TapoClient, Json
from plugp100.common.functional.tri import Try
from plugp100.common.utils.json_utils import dataclass_encode_json
from plugp100.requests.set_device_info.play_alarm_params import PlayAlarmParams
from plugp100.requests.tapo_request import TapoRequest
from plugp100.responses.alarm_type_list import AlarmTypeList
from plugp100.responses.child_device_list import ChildDeviceList
from plugp100.responses.device_state import HubDeviceState

HubSubscription = Callable[[], Any]


# The HubDevice class is a blueprint for creating hub devices.
class HubDevice(_BaseTapoDevice):
    def __init__(self, api: TapoClient, logger: Logger = None):
        super().__init__(api)
        self._tracker = HubConnectedDeviceTracker(logger)
        self._is_tracking = False
        self._tracking_tasks: List[asyncio.Task] = []
        self._tracking_subscriptions: List[Callable[[HubDeviceEvent], Any]] = []
        self._logger = logger if logger is not None else logging.getLogger("HubDevice")

    async def turn_alarm_on(self, alarm: PlayAlarmParams = None) -> Try[bool]:
        request = TapoRequest(
            method="play_alarm",
            params=dataclass_encode_json(alarm) if alarm is not None else None,
        )
        return (await self._api.execute_raw_request(request)).map(lambda _: True)

    async def turn_alarm_off(self) -> Try[bool]:
        return (
            await self._api.execute_raw_request(
                TapoRequest(method="stop_alarm", params=None)
            )
        ).map(lambda _: True)

    async def get_state(self) -> Try[HubDeviceState]:
        """
        The function `get_state` asynchronously retrieves device information and returns either the device state or an
        exception.
        @return: an instance of the `Either` class, which can hold either a `HubDeviceState` object or an `Exception`
        object.
        """
        return (await self._api.get_device_info()).flat_map(HubDeviceState.try_from_json)

    async def get_supported_alarm_tones(self) -> Try[AlarmTypeList]:
        return (
            await self._api.execute_raw_request(
                TapoRequest(method="get_support_alarm_type_list", params=None)
            )
        ).flat_map(AlarmTypeList.try_from_json)

    async def get_state_as_json(self) -> Try[Json]:
        return await self._api.get_device_info()

    async def get_children(self) -> Try[ChildDeviceList]:
        return await self._api.get_child_device_list()

    async def control_child(self, device_id: str, request: TapoRequest) -> Try[Json]:
        """
        The function `control_child` is an asynchronous method that takes a device ID and a TapoRequest object as
        parameters, and it returns either a JSON response or an Exception.

        @param device_id: A string representing the ID of the device that needs to be controlled
        @type device_id: str
        @param request: The `request` parameter is an instance of the `TapoRequest` class. It is used to specify the details
        of the control operation to be performed on a child device
        @type request: TapoRequest
        @return: an `Either` object, which can contain either a `Json` object or an `Exception`.
        """
        return await self._api.control_child(device_id, request)

    def start_tracking(self, interval_millis: int = 10_000):
        """
        The function `start_tracking` starts a background task that periodically polls for updates.

        @param interval_millis: The `interval_millis` parameter is an optional integer that specifies the time interval in
        milliseconds at which the `_poll` method will be called. The default value is 10,000 milliseconds (or 10 seconds),
        @defaults to 10_000
        @type interval_millis: int (optional)
        """
        if not self._is_tracking:
            self._is_tracking = True
            self._tracking_tasks = [
                asyncio.create_task(self._poll(interval_millis)),
                asyncio.create_task(self._poll_tracker()),
            ]

    def stop_tracking(self):
        """
        The function `stop_tracking` cancels a background task and sets the `is_observing` attribute to False.
        """
        if self._is_tracking:
            self._is_tracking = False
            for task in self._tracking_tasks:
                task.cancel()
            self._tracking_tasks = []

    def subscribe(self, callback: Callable[[HubDeviceEvent], Any]) -> HubSubscription:
        """
        The `subscribe` function adds a callback function to the list of subscriptions and returns an unsubscribe function.

        @param callback: The `callback` parameter is a function that takes a `ChildDeviceList` object as input and returns
        any value
        @type callback: Callable[[ChildDeviceList], Any]
        @return: The function `unsubscribe` is being returned.
        """
        self._tracking_subscriptions.append(callback)

        def unsubscribe():
            self._tracking_subscriptions.remove(callback)

        return unsubscribe

    def _emit(self, state_change: HubDeviceEvent):
        for sub in self._tracking_subscriptions:
            if iscoroutinefunction(sub):
                asyncio.create_task(sub(state_change))
            else:
                sub(state_change)

    async def _poll(self, interval_millis: int):
        while self._is_tracking:
            new_state = await self._api.get_child_device_list()
            if new_state.is_success():
                await self._tracker.notify_state_update(
                    cast(ChildDeviceList, new_state.get()).get_device_ids()
                )
            else:
                self._logger.error(new_state.error())
            await asyncio.sleep(interval_millis / 1000)  # to seconds

    async def _poll_tracker(self):
        while self._is_tracking:
            state_change = await self._tracker.get_next_state_change()
            self._emit(state_change)
