#main.py

import discord
import time
import os

#I just imported stuff you big dum-dum

client = discord.Client()

#This prints a message in the console saying the bot is connected
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')
    if message.author == client.user:
        return
    
    if message.content.startswith('^hello'):
        print('Saying Hello')
        await message.channel.send('Hello!')

client.run(os.environ['BOT_SECRET'])