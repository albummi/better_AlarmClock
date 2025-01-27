"""Alarm Clock Dashboard backend logic."""
from homeassistant.components.http import HomeAssistantView
import logging

_LOGGER = logging.getLogger(__name__)

class AlarmClockView(HomeAssistantView):
    """HTTP view to handle alarm clock dashboard actions."""

    url = "/api/alarm_clock_dashboard"
    name = "api:alarm_clock_dashboard"
    requires_auth = True

    async def post(self, request):
        """Handle POST requests for alarm clock settings."""
        hass = request.app["hass"]
        try:
            data = await request.json()
            alarm_time = data.get("alarm_time")
            enabled = data.get("enabled")

            # Log the received data for debugging
            _LOGGER.info("Received alarm clock update: %s", data)

            if enabled:
                # Logic to enable alarm
                _LOGGER.info(f"Alarm enabled for {alarm_time}.")
            else:
                # Logic to disable alarm
                _LOGGER.info("Alarm disabled.")

            return self.json({"success": True})
        except Exception as e:
            _LOGGER.error("Error handling alarm clock update: %s", e)
            return self.json({"success": False, "error": str(e)}, status=500)
