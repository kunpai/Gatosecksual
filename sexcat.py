import discord
import os
import random
import interactions
from discord_slash import SlashCommand, SlashContext
from discord.ext import tasks
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents = intents)
slash = SlashCommand(client, sync_commands=True)
can = {}

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    for guild in client.guilds:
          print(
            f'{client.user} is connected to the following guild:\n'
          f'{guild.name}\n'
          )
    global members
    members = guild.members
    for member in guild.members:
        can[member] = 0
    can_request.start()
    os.chdir("./sexcat")
    
@slash.slash(name ="meow", description="Sends sexcat photo")
async def _meow (ctx = SlashContext):
    await ctx.send(file=discord.File(random.choice(os.listdir(os.getcwd()))))

@slash.slash(name ="answer", description="Solves your life for you")
async def _answer (ctx = SlashContext):
    await ctx.send('Can')

@slash.slash(name="can_request", description="Requests a random user for can")
async def _can_request(ctx = SlashContext):
    user = random.choice(members)
    await ctx.send(user.mention)
    await ctx.send('Pwease can I have can?')
    await ctx.send(file=discord.File("pwease.jpg"))

@tasks.loop(hours=10)
async def can_request():
    channel = client.get_channel(951343927909310477)
    user = random.choice(members)
    await channel.send(user.mention)
    await channel.send('Pwease can I have can?')
    await channel.send(file=discord.File("pwease.jpg")) 

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('🥫'):
        await message.channel.send('meow thank u for can')
        can[message.author] += message.content.count('🥫')
        can_status = 'you have currently given me ' + str(can[message.author]) + ' can'
        await message.channel.send(can_status)

    if message.content.startswith('!'):
        await message.channel.send('meow meow I just want can')
        await message.channel.send(file=discord.File(random.choice(os.listdir(os.getcwd()))))

client.run(os.environ['DISCORD_TOKEN'])
