import lightbulb, hikari

from extensions.modmail import *

plugin = lightbulb.Plugin("Server Handler")

@plugin.listener(hikari.MessageEvent)
async def server_t_manager(event: hikari.MessageEvent) -> None:
    if(event.is_human)
        return None

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)
