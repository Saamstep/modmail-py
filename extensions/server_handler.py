import lightbulb, hikari
from config import *
from extensions.modmail import *

plugin = lightbulb.Plugin("Server Handler")

@plugin.listener(hikari.MessageEvent)
async def server_t_manager(event: hikari.GuildMessageCreateEvent) -> None:
    if event.is_human and str(event.guild_id) == config.primaryGuild:
        channel = await plugin.bot.rest.fetch_channel(event.channel_id)
        if(str(channel.parent_id) == config.ticketCategory):
            serverToDm(event.author, event.content)

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)
