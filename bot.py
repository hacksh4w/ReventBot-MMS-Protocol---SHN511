# bot.py
import os
import discord
import random
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Intents
#from keep_alive import keep_alive

intents = Intents.all()
from dotenv import load_dotenv

load_dotenv('.env')
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name='Skill Brigade')
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


bot = Bot(intents=intents, command_prefix='$')  # command prefix

#keep_alive()
print(os.getenv('TOKEN') is None)
client.run(TOKEN)
