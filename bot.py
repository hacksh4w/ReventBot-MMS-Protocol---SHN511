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
#to send notif
ini_time_for_now = datetime.now()
#array containing the tests and assignments
x=['testmath%4','testscience%6']

timern = str(ini_time_for_now)
print(timern[8:11])
async def check(x):
  for i in x:
    temp = i.split('%')
    temp_name,temp_time = temp[0],temp[1]
    temp3 = str(datetime.now())
    temp3 = temp3[8:11]
    if temp3 == temp[1]:
      on_message()

#Time check command for Tests
@Bot.command(pass_context=True)
async def countdown(ctx, seconds: int):
    td = timedelta(seconds=seconds)
    while True:
        await Bot.say(time_repr(td))
        if td.total_seconds() > 259200: # 3 days
            td -= timedelta(seconds=259200)
            await sleep(timren-259200) # time until 3 days
        elif td.total_seconds > 172800: # 2 days
            td -= timedelta(seconds=172800) 
            await sleep(10)  # time until 2 days
        elif td.total_seconds > 86,400: # 1 day
            td -= timedelta(seconds=86,400) 
            await sleep(1)  # time until 1 day
        else:
            break

print(os.getenv('TOKEN') is None)
client.run(TOKEN)
