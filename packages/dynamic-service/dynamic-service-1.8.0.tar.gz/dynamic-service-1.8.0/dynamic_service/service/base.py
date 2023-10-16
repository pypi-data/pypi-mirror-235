# base.py

import warnings
import datetime as dt
import time
from typing import (
    Optional, Union, Dict, Any, Iterable
)

from looperator import Superator, Operator

from dynamic_service.endpoints import (
    BaseEndpoint, valid_endpoints
)

__all__ = [
    "EndpointsService",
    "ServiceInterface"
]

Endpoints = Dict[str, BaseEndpoint]
EndpointsContainer = Union[Iterable[BaseEndpoint], Endpoints]

class EndpointsService:
    """A class to represent an endpoints service."""

    def __init__(
            self,
            endpoints: Optional[EndpointsContainer] = None
    ) -> None:
        """
        Defines the server datasets for clients and client commands.

        :param endpoints: The commands to run for specific requests of the clients.
        """

        self.endpoints = self.valid_endpoints(endpoints or {})

        for endpoint in self.endpoints.values():
            endpoint.service = self
        # end for
    # end __init__

    @staticmethod
    def valid_endpoints(endpoints: Optional[Any] = None) -> Endpoints:
        """
        Process the endpoints' commands to validate and modify it.

        :param endpoints: The endpoints object to check.

        :return: The valid endpoints object.
        """

        return valid_endpoints(endpoints=endpoints)
    # end valid_endpoints

    def add_endpoint(self, endpoint: BaseEndpoint, path: Optional[str] = None) -> None:
        """
        Adds the endpoint to the service.

        :param path: The path for the endpoint.
        :param endpoint: The command to run.
        """

        self.endpoints[path or endpoint.path] = endpoint
    # end add_endpoint

    def add_endpoints(self, endpoints: EndpointsContainer) -> None:
        """
        Adds the endpoint to the service.

        :param endpoints: The commands to run.
        """

        self.endpoints.update(self.valid_endpoints(endpoints))
    # end add_endpoints

    def set_endpoint(
            self, endpoint: BaseEndpoint, path: Optional[str] = None
    ) -> None:
        """
        Adds the endpoint to the service.

        :param path: The path for the endpoint.
        :param endpoint: The command to run.
        """

        path = path or endpoint.path

        if path not in self.endpoints:
            raise ValueError(
                f"The path was not initialized for a different "
                f"endpoint beforehand. Consider using "
                f"'{self.add_endpoint.__name__}' method instead, "
                f"to add endpoints with new path. Given path: {path}. "
                f"Valid paths: {', '.join(self.endpoints.keys())}"
            )
        # end if

        self.endpoints[path] = endpoint
    # end set_endpoint

    def remove_endpoint(
            self, *,
            path: Optional[str] = None,
            endpoint: Optional[BaseEndpoint] = None
    ) -> None:
        """
        Removes the endpoint from the service.

        :param path: The index for the endpoint.
        :param endpoint: The command to run.
        """

        if path is not None:
            try:
                self.endpoints.pop(path)

            except KeyError:
                raise ValueError(
                    f"The path was not initialized for a different "
                    f"endpoint beforehand, therefore an endpoint "
                    f"labeled with that path couldn't be removed. Given path: {path}. "
                    f"Valid paths: {', '.join(self.endpoints.keys())}"
                )
            # end try

        elif endpoint is not None:
            for key, value in self.endpoints.items():
                if (value is endpoint) or (value == endpoint):
                    self.endpoints.pop(key)
                # end if

            else:
                raise ValueError(
                    f"Endpoint object '{repr(endpoint)}' doesn't "
                    f"exist in the endpoints of service object {repr(self)}, "
                    f"therefore could not be removed. Given path: {path}. "
                    f"Valid paths: {', '.join(self.endpoints.keys())}"
                )
            # end for
        # end if
    # end remove_endpoint

    def remove_endpoints(
            self, *,
            paths: Optional[Iterable[str]] = None,
            endpoints: Optional[EndpointsContainer] = None
    ) -> None:
        """
        Removes the endpoint from the service.

        :param paths: The paths for the endpoint.
        :param endpoints: The commands to run.
        """

        if paths is not None:
            for path in paths:
                self.remove_endpoint(path=path)
            # end if

        else:
            for endpoint in endpoints:
                self.remove_endpoint(endpoint=endpoint)
            # end for
        # end if
    # end remove_endpoint

    def remove_all_endpoints(self) -> None:
        """Removes all the endpoints from the service."""

        self.endpoints.clear()
    # end remove_all_endpoints

    def update_endpoints(self, endpoints: EndpointsContainer) -> None:
        """
        Adds the endpoint to the service.

        :param endpoints: The commands to run.
        """

        self.endpoints.update(self.valid_endpoints(endpoints))
    # end update_endpoints
# end EndpointsService

class ServiceInterface(Superator):
    """A service interface for server client communication."""

    SLEEP = 0.0
    DELAY = 0.0001

    def __init__(self) -> None:
        """Defines the attribute of the server service."""

        self._refreshing = False
        self._updating = False

        self.refresh_value: Optional[Union[float, dt.timedelta]] = None

        self._refresh_operator = Operator(
            operation=self._refresh,
            delay=self.DELAY
        )

        self._update_operator = Operator(
            operation=self.update,
            delay=self.DELAY
        )

        super().__init__(
            operators=[
                self._refresh_operator,
                self._update_operator
            ],
            delay=self.DELAY
        )

        self._start_time = time.time()
        self._current_time = time.time()
    # end __init__

    @property
    def updating(self) -> bool:
        """
        Returns the value of the updating process.

        :return: The updating value.
        """

        return self._updating
    # end updating

    @property
    def refreshing(self) -> bool:
        """
        Returns the value of te execution being refreshing by the service loop.

        :return: The refreshing value.
        """

        return self._refreshing
    # end refreshing

    def update(self) -> None:
        """Updates the options according to the screeners."""
    # end update

    def refresh(self) -> None:
        """Updates the options according to the screeners."""
    # end refresh

    def blocking_loop(self) -> None:
        """Updates the options according to the screeners."""

        self._blocking = True

        while self.blocking:
            time.sleep(self.SLEEP)
        # end while
    # end blocking_loop

    def start_blocking(self) -> None:
        """Starts the blocking process."""

        if self.blocking:
            warnings.warn(f"Blocking process of {self} is already running.")

            return
        # end if

        self.blocking_loop()
    # end start_blocking

    def _refresh(self) -> None:
        """Updates the options according to the screeners."""

        refresh = self.refresh_value

        if refresh:
            self._current_time = time.time()

            if isinstance(refresh, dt.timedelta):
                refresh = refresh.total_seconds()
            # end if

            if (self._current_time - self._start_time) >= refresh:
                self._start_time = self._current_time

                self.refresh()
            # end if
        # end if
    # end _refresh

    def start_refreshing(self, refresh: Union[float, dt.timedelta]) -> None:
        """
        Starts the refreshing process.

        :param refresh: The value to refresh the service.
        """

        self.refresh_value = refresh

        self._refresh_operator.start_operation()
    # end start_refreshing

    def start_updating(self) -> None:
        """Starts the updating process."""

        self._update_operator.start_operation()
    # end start_updating

    def run(
            self,
            update: Optional[bool] = False,
            block: Optional[bool] = False,
            refresh: Optional[Union[float, dt.timedelta]] = None,
            wait: Optional[Union[float, dt.timedelta, dt.datetime]] = None,
            timeout: Optional[Union[float, dt.timedelta, dt.datetime]] = None,
    ) -> None:
        """
        Runs the api service.

        :param update: The value to update the service.
        :param block: The value to block the execution and wain for the service.
        :param refresh: The value to refresh the service.
        :param wait: The waiting time.
        :param timeout: The start_timeout for the process.
        """

        if update:
            self.start_updating()
        # end if

        if refresh:
            self.start_refreshing(refresh)
        # end if

        if timeout:
            self.start_timeout(timeout)
        # end if

        if wait:
            self.start_waiting(wait)
        # end if

        if block:
            self.start_blocking()
        # end if
    # end run

    def stop_refreshing(self) -> None:
        """Stops the refreshing process."""

        self._refresh_operator.stop_operation()
    # end stop_refreshing

    def stop_updating(self) -> None:
        """Stops the updating process."""

        self._update_operator.stop_operation()
    # end stop_updating

    def terminate(self) -> None:
        """Pauses the process of service."""

        self.stop()
    # end terminate

    def stop(self) -> None:
        """Stops the service."""

        self.stop_updating()
        self.stop_refreshing()

        super().stop()
    # end stop
# end ServiceInterface