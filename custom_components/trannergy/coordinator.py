"""DataUpdateCoordinator for Trannergy PV Inverter."""

from __future__ import annotations

import logging
from datetime import timedelta
from typing import Any

from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.helpers.event import async_track_time_interval

from .api import (
    TrannergyInverterApi,
    TrannergyInverterConnectionError,
    TrannergyInverterTimeoutError,
)

_LOGGER = logging.getLogger(__name__)


class TrannergyDataUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    """Class to manage fetching Trannergy data from the inverter."""

    def __init__(
        self,
        hass: HomeAssistant,
        api: TrannergyInverterApi,
        name: str,
        update_interval: int,
    ) -> None:
        """Initialize the coordinator.

        Args:
            hass: Home Assistant instance.
            api: API client for the inverter.
            name: Name of the inverter.
            update_interval: Update interval in seconds.
        """
        self.api = api
        self._update_interval_seconds = update_interval
        self._unsub_interval = None

        super().__init__(
            hass,
            _LOGGER,
            name=name,
            update_interval=timedelta(seconds=update_interval),
        )

    async def _async_update_data(self) -> dict[str, Any]:
        """Fetch data from the inverter.

        Returns:
            Dictionary with all sensor data.

        Raises:
            UpdateFailed: If fetching data fails.
        """
        try:
            data = await self.api.async_get_data()
            _LOGGER.debug("Successfully fetched data from inverter: %s", data)
            return data
        except TrannergyInverterTimeoutError as err:
            # Inverter is likely offline (e.g., at night), return offline data
            _LOGGER.debug("Inverter timeout (likely offline): %s", err)
            return self.api._get_offline_data()
        except TrannergyInverterConnectionError as err:
            # Connection error, return offline data
            _LOGGER.debug("Inverter connection error: %s", err)
            return self.api._get_offline_data()
        except Exception as err:
            _LOGGER.exception("Unexpected error fetching data from inverter")
            raise UpdateFailed(f"Error fetching data from inverter: {err}") from err

    @callback
    def async_setup_interval(self) -> None:
        """Set up the update interval using async_track_time_interval."""
        if self._unsub_interval is not None:
            self._unsub_interval()

        async def _async_refresh(_: Any) -> None:
            """Refresh data from the inverter."""
            await self.async_refresh()

        self._unsub_interval = async_track_time_interval(
            self.hass,
            _async_refresh,
            timedelta(seconds=self._update_interval_seconds),
        )

    @callback
    def async_unload(self) -> None:
        """Unload the coordinator."""
        if self._unsub_interval is not None:
            self._unsub_interval()
            self._unsub_interval = None

