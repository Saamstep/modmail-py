import lightbulb, hikari

from extensions.modmail import *

plugin = lightbulb.Plugin("DM Handler")

@plugin.listener(hikari.DMMessageCreateEvent)
async def dm_manager(event: hikari.DMMessageCreateEvent) -> None:
    if event.is_human:
        open = open_ticket_check(event.author)

        if not open:
            await create_ticket(event.author)

        await dmToServer(event.author, event.content)

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)
