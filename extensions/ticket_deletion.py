import lightbulb, hikari
import config
from extensions.modmail import *

plugin = lightbulb.Plugin("Ticket Deleter")

@plugin.listener(hikari.GuildChannelDeleteEvent)
async def ticket_delete_handler(event: hikari.GuildChannelDeleteEvent) -> None:
    if(event.channel.guild_id == config.primaryGuild and event.channel.parent_id == config.ticketCategory):
        db.delete_ticket(event.channel.id)
        logging.info("Deleting ticket: %s" % event.channel.name)

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)
