import discord
import os
import random
import interactions
from discord_slash import SlashCommand, SlashContext
from dotenv import load_dotenv
load_dotenv()

client = discord.Client()
slash = SlashCommand(client, sync_commands=True)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    os.chdir("./sexcat")
    
@slash.slash(name ="meow", description="Sends sexcat photo")
async def _meow (ctx = SlashContext):
    await ctx.send(file=discord.File(random.choice(os.listdir(os.getcwd()))))

@slash.slash(name ="answer", description="Solves your life for you")
async def _answer (ctx = SlashContext):
    await ctx.send('Can')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!'):
        await message.channel.send('meow meow I just want can')
        await message.channel.send(file=discord.File(random.choice(os.listdir(os.getcwd()))))

client.run(os.environ['DISCORD_TOKEN'])
