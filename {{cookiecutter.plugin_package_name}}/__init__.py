import lightbulb

{%- if cookiecutter.protected == "Yes" -%}
from remi.core.constant import Client
from remi.core.exceptions import ProtectedPlugin

{%- elif cookiecutter.protected == "No" -%}
{%- endif %}

from .{{ cookiecutter.plugin_base_file }} import {{ cookiecutter.plugin_base_name }}

__plugin_name__ = {{ cookiecutter.plugin_base_name }}.name
__plugin_description__ = {{ cookiecutter.plugin_base_name }}.description


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin({{ cookiecutter.plugin_base_name }})


def unload(bot: lightbulb.BotApp) -> None:
    {% if cookiecutter.protected == "Yes" -%}
    if Client.dev_mode:
        bot.remove_plugin({{ cookiecutter.plugin_base_name }})
    else:
        raise ProtectedPlugin(f"Cannot unload protected plugin {% raw %}{{% endraw %}{{ cookiecutter.plugin_base_name }}.name{% raw %}}{% endraw %}!")
    {% else -%}
    bot.remove_plugin({{ cookiecutter.plugin_base_name }})
    {%- endif -%}
