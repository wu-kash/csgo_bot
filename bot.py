# bot.py
import os

import discord

# !pip install nest_asyncio to get rid of RuntimeError: Cannot close a running event loop
import nest_asyncio
nest_asyncio.apply()

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')    
csgo_bot = commands.Bot(command_prefix = 'cs.', case_insensitive = True)
    
''' Functions '''

def do_callout(msg_str):
    map_name = msg_str.split(" ")[1]
        
    print("Retrieving callout map for {}".format(map_name))
    
    callout_map_dir = os.path.join(os.getcwd(), 'callout_maps')
    
    callout_list = []
    
    for image in os.listdir(callout_map_dir):
        if map_name in image:
            callout_list.append(os.path.join(callout_map_dir, image))

    if len(callout_list) < 1:
        callout_list.append(os.path.join(callout_map_dir, 'callout_404.png'))
   
    return callout_list
    
def do_smoke(msg_str):
    
    # cs.smoke dust2 ctspawn snipers
    
    smoke_map = msg_str.split(" ")[1]
    smoke_from = msg_str.split(" ")[2]
    try:
        smoke_to = msg_str.split(" ")[3]
    except IndexError:
        smoke_to = ""
        
    smoke_desc = smoke_from + "_" + smoke_to

    print("Map: " + smoke_map)
    print("From " + smoke_from + ", to " + smoke_to)
    
    smoke_dir = os.path.join(os.getcwd(), 'smokes')
    smoke_map_dir =  os.path.join(smoke_dir, smoke_map)
    
    smoke_list = []
    
    for image in os.listdir(smoke_map_dir):
        if smoke_desc in image:
            smoke_list.append(os.path.join(smoke_map_dir, image))
    
    if len(smoke_list) < 1:
        smoke_list.append(os.path.join(smoke_dir, 'smoke_404.png'))
   
    return smoke_list

def do_molotov(msg_str):
    
    # cs.smoke dust2 ctspawn snipers
    
    molotov_map = msg_str.split(" ")[1]
    molotov_from = msg_str.split(" ")[2]
    try:
        molotov_to = msg_str.split(" ")[3]
    except IndexError:
        molotov_to = ""
        
    molotov_desc = molotov_from + "_" + molotov_to

    print("Map: " + molotov_map)
    print("From " + molotov_from + ", to " + molotov_to)
    
    molotov_dir = os.path.join(os.getcwd(), 'molotovs')
    molotov_map_dir =  os.path.join(molotov_dir, molotov_map)
    
    molotov_list = []
    
    for image in os.listdir(molotov_map_dir):
        if molotov_desc in image:
            molotov_list.append(os.path.join(molotov_map_dir, image))
    
    if len(molotov_list) < 1:
        molotov_list.append(os.path.join(molotov_dir, 'molotov_404.png'))
   
    return molotov_list
    
''' Start '''

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
        callout_list = do_callout(msg_str)
    
        for file_name in callout_list:
            await channel.send(file=discord.File(file_name))

    if message.content.startswith("cs.smoke"):
        smoke_list = do_smoke(msg_str)
    
        for file_name in smoke_list:
            await channel.send(file=discord.File(file_name))
            
    if message.content.startswith("cs.molotov"):
        molotov_list = do_molotov(msg_str)
    
        for file_name in molotov_list:
            await channel.send(file=discord.File(file_name))
       
        
csgo_bot.run(TOKEN)

    
    
