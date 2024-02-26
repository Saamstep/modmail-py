import lightbulb, hikari

from extensions.modmail import *

plugin = lightbulb.Plugin("DM Handler")

@plugin.listener(hikari.DMMessageCreateEvent)
async def ticket_manager(event: hikari.DMMessageCreateEvent) -> None:
    openticket = open_ticket_check(event.author)

    if event.is_human and not openticket:
        create_ticket(event.author)
    elif event.is_human and openticket:
       # handleMessage()
       return

def load(bot: lightbulb.BotApp):
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)