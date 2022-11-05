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

#code to add event
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content
#says hello
    if msg.content.startswith('$hello'):
      await msg.channel.send('Hello! {}'.format(client.user))
#code to set event reminders
    if msg.startswith('$test'):
#    #run (check time elapsed command)
    if msg.startswith('$assn'):
#     #run (check time elapsed command)
    if msg.startswith('$game'):
#     #run (check time elapsed command)    

#to add event 
  if msg.startswith("$new"):
    event_message = msg.split("$new ",1)[1]
    update_events(event_message)
    await message.channel.send("New event message added.")
#delete and list
  if msg.startswith("$del"):
    events = []
    if "events" in db.keys():
      index = int(msg.split("$del",1)[1])
      delete_encouragment(index)
      events = db["events"]
    await message.channel.send(events)

  if msg.startswith("$list"):
    events = []
    if "events" in db.keys():
      events = db["events"]
    await message.channel.send(events)


print(os.getenv('TOKEN') is None)
client.run(TOKEN)
