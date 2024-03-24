import os, hikari
import lightbulb
from dotenv import load_dotenv
from helpers.db import *
import config
load_dotenv()

INTENTS = hikari.Intents.GUILD_MEMBERS | hikari.Intents.GUILDS | hikari.Intents.DM_MESSAGES | hikari.Intents.MESSAGE_CONTENT | hikari.Intents.ALL_MESSAGES | hikari.Intents.ALL_GUILDS

bot = lightbulb.BotApp(token=os.environ["TOKEN"],intents=INTENTS,banner=None)

bot.load_extensions_from('commands')
bot.load_extensions_from('extensions')

bot.run()