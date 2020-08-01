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

def get_item(msg_str):
    
    command = msg_str.split(".")[1].split(" ")[0]
    item_name = msg_str.split(" ")[1]
        
    
    item_dir = os.path.join(os.getcwd(), command)
    
    item_list = []
    
    for image in os.listdir(item_dir):
        if item_name in image:
            item_list.append(os.path.join(item_dir, image))

    if len(item_list) < 1:
        item_list.append(os.path.join(item_dir, '{}_404.png'.format(command)))
   
    return item_list

def get_nade(msg_str):

    # cs.nadetype map from to
    
    command = msg_str.split(".")[1].split(" ")[0]
    
    nade_map = msg_str.split(" ")[1]
    nade_from = msg_str.split(" ")[2]
    try:
        nade_to = msg_str.split(" ")[3]
    except IndexError:
        nade_to = ""
        
    nade_desc = nade_from + "_" + nade_to

    nade_dir = os.path.join(os.getcwd(), command)
    nade_map_dir =  os.path.join(nade_dir, nade_map)
    
    nade_list = []
    
    for image in os.listdir(nade_map_dir):
        if nade_desc in image:
            nade_list.append(os.path.join(nade_map_dir, image))
    
    if len(nade_list) < 1:
        nade_list.append(os.path.join(nade_dir, '{}_404.png'.format(command)))
   
    return nade_list
    
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
        file_list = get_item(msg_str)
                
    if message.content.startswith("cs.spray"):
        file_list = get_item(msg_str)
        
    if message.content.startswith("cs.weapon"):
        file_list = get_item(msg_str)
        
    if message.content.startswith("cs.smoke") or message.content.startswith("cs.molotov"):
        file_list = get_nade(msg_str)
    
    
    if len(file_list) > 0:
        for file_name in file_list:
            await channel.send(file=discord.File(file_name))
       
        
csgo_bot.run(TOKEN)

    
    
