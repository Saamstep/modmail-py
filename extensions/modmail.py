import lightbulb, hikari
import helpers.db as db
import config
import logging

plugin = lightbulb.Plugin("ModMail Plugin")

async def getPrimaryGuild():
    return (await plugin.bot.rest.fetch_guild(config.primaryGuild))

async def getTicketsCategory():
    return (await plugin.bot.rest.fetch_channel(config.ticketCategory))

async def create_ticket(user) -> hikari.ChannelType.GUILD_TEXT:
   logging.info("Creating ticket for %s" % user)
   g = await getPrimaryGuild()
   c = await getTicketsCategory()
   channel = await g.create_text_channel(name=user.username, category=c.id, topic="**STATUS** NEW 🔸 **ASSIGNED TO** None", reason="NEW TICKET")
   db.new_ticket(user, channel)
   return channel, user

async def dmToServer(user, content):
    t = db.find_user(user)[0]
    print(t)
    m = await sendDmToServer(t, content)
    if(m == None):
        await plugin.bot.rest.create_message(t.get('channel_id'), "❌ **Error** Unable to send message received by sender.")
        return False
    else:
        await plugin.bot.rest.add_reaction(t.get('channel_id'), m.id, emoji='✅')
        return True

async def sendDmToServer(t, content):
    try:
        msg = await plugin.bot.rest.create_message(t.get('channel_id'), content)
        return msg
    except Exception as e:
        logging.critical(e)
        return None
    
def open_ticket_check(user) -> bool:
    if(len(db.find_user(user)) >= 1): return True
    else: return False

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)