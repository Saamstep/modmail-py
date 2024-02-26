import lightbulb, hikari
import helpers.db as db
import config

plugin = lightbulb.Plugin("ModMail Plugin")

def create_ticket(user) -> int:
    print(plugin.bot.get_me())
    plugin.bot.rest.fetch_guild(config.primaryGuild)
    db.new_ticket()
   
    
def open_ticket_check(user) -> bool:
    return False


def load(bot: lightbulb.BotApp):
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)