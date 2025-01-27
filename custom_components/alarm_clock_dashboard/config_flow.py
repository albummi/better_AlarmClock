"""Config flow for the Alarm Clock Dashboard integration."""
from homeassistant import config_entries
from . import DOMAIN


class AlarmClockConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for the Alarm Clock Dashboard."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="Alarm Clock Dashboard", data={})
        return self.async_show_form(step_id="user")
