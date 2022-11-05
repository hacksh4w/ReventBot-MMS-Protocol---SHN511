# bot.py
import os

import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Intents
intents = Intents.all()
 #from dotenv import load_dotenv
TOKEN = 'MTAzODQzMzkxNDUwNDYxMzk3OA.G48fmI.OshF3B7_3J7VRU-NDiiJlNUuPA8Pzc2hfriP0Q'
#load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')
#GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
bot = Bot(intents=intents, command_prefix='$') # or whatever prefix you choose(!,%,?)

client.run(TOKEN)