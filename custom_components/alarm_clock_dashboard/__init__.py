"""Initialize the Alarm Clock Dashboard integration."""
import logging
from .alarm_dashboard import AlarmClockView

_LOGGER = logging.getLogger(__name__)

DOMAIN = "alarm_clock_dashboard"

async def async_setup(hass, config):
    """Set up the Alarm Clock Dashboard integration."""
    hass.http.register_view(AlarmClockView())
    _LOGGER.info("Alarm Clock Dashboard integration initialized!")
    return True
