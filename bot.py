# bot.py
import os
import discord
import random
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Intents

intents = Intents.all()
from dotenv import load_dotenv

load_dotenv('.env')
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
intents=discord.Intents.default()

client = discord.Client(intents=intents)
intents.message_content = True

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name='Skill Brigade')
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
      return
    if message.content.startswith('$hello'):
      await message.channel.send('Hello! {}'.format(client.user))
    
print(os.getenv('TOKEN') is None)
client.run(TOKEN)
