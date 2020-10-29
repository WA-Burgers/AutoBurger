#main.py

import logging
import time
import os

import discord
from discord.ext import commands

#I just imported stuff you big dum-dum

#logging setup
logging.basicConfig(level=logging.INFO)

#Defining Discord Client
client = discord.Client()

#Defining Discord Commands
bot = commands.Bot(command_prefix='^')

#This prints a message in the console saying the bot is connected
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

#Maybe prints hello?
@bot.command()
async def hello(ctx):
    print('Saying Hello')
    ctx.send(f'Hello {ctx.author}!')

@bot.command()
async def echo(ctx, arg):
    print('echoing')
    ctx.send(arg)

@bot.command()
async def test(ctx):
    pass

client.run(os.environ['BOT_SECRET'])