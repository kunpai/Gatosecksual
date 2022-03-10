import discord
import os
import random
from dotenv import load_dotenv
load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    os.chdir("./sexcat")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!'):
        await message.channel.send('meow meow I just want can')
        await message.channel.send(file=discord.File(random.choice(os.listdir(os.getcwd()))))

client.run(os.environ['DISCORD_TOKEN'])
