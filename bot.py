# bot.py
import os

import discord

# !pip install nest_asyncio to get rid of RuntimeError: Cannot close a running event loop
import nest_asyncio
nest_asyncio.apply()

from dotenv import load_dotenv
from discord.ext import commands

''' Functions '''

def get_callout_map(map_name):
    
    print("Retrieving callout map for {}".format(map_name))
    
    callout_map_dir = os.path.join(os.getcwd(), 'callout_maps')
    
    for image in os.listdir(callout_map_dir):
        if map_name in image:
            print(image)
            return os.path.join('callout_maps', image)

''' Start '''

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')    
csgo_bot = commands.Bot(command_prefix = 'cs.', case_insensitive = True, decription = "Hello!")
    
@csgo_bot.event
async def on_connect():
    print("Connected...")
    
@csgo_bot.event 
async def on_disconnect():
    print("Disconnected")
    
@csgo_bot.event
async def on_ready():
    print('Logged in as')
    print(csgo_bot.user.name)
    print(csgo_bot.user.id)
    print('------')

    
@csgo_bot.event
async def on_message(message):
    print("Message from {0.author} in channel {0.channel.id}:".format(message))
    print("{0.content}".format(message))
    
    msg_str = message.content
    channel = csgo_bot.get_channel(message.channel.id)
    
    if message.author.id == csgo_bot.user.id:
        return
    
    if message.content.startswith("cs.callout"):
        
        map_name = msg_str.split(" ")[1]
        
        file_name = get_callout_map(map_name)
        print(file_name)
        await channel.send(file=discord.File(file_name))
        
csgo_bot.run(TOKEN)

    
    
