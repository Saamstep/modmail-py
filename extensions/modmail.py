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
    ticketCh = db.getTicketChannel(user)
    m = await sendDmToServer(ticketCh, content)

    if(m == None):
        await plugin.bot.rest.create_message(ticketCh, "❌ **Error** Unable to send message received by sender.")
        logging.error("Unable to send message from %s to primary guild." % user.username)
        return False
    else:
        logging.info("Message from %s sent to primary guild." % user.username)
        return True

async def sendDmToServer(t, content):
    try:
        msg = await plugin.bot.rest.create_message(t, content)
        return msg
    except Exception as e:
        logging.critical(e)
        return None
    
def open_ticket_check(user) -> bool:
    return db.find_user(user)

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)