import discord
from discord.ext import commands
# from itertools import cycle
import asyncio
import platform
import time
import colorsys
import random
prefix = "§"
bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')
BOT_OWNER_ROLE="owner" #change which role you need!



@bot.event
async def on_ready():
    print('Online')
    print("Made by Subrata#3297")
    print("DANGER TRIVIA || BOTS:")
    print("https://discord.gg/2degbQMAxU")
    print("Everything is okay.")
    while True:
    	await bot.change_presence(activity=discord.Activity(type=1,name="with Love ♥️ with all members !"))
    	await asyncio.sleep(2)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with TRIVIA || DANGER★᭄ꦿ᭄"))
    	await asyncio.sleep(2)
	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with Sb ke sb ek saath Maze karo"))
    	await asyncio.sleep(2)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with Love ♥️"))
    	await asyncio.sleep(2)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with  Trivia Danger is my jaan"))
    	await asyncio.sleep(2)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with Love Mom & Dad ❤️"))
    	await asyncio.sleep(2)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with MAZE KARO"))
    	await asyncio.sleep(2)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with HQ specially our bot Danger Trivia"))
    	await asyncio.sleep(2)

    	await bot.change_presence(activity=discord.Activity(type=1,name="with JAY MAHADEV"))
    	await asyncio.sleep(2)
	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with DANGER TRIVIA || BOTS !"))
    	await asyncio.sleep(2)
	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with MADE BY ANSHU BHAI"))
    	await asyncio.sleep(2)
	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with MY LOVE"))
    	await asyncio.sleep(2)
    	
    	await bot.change_presence(activity=discord.Activity(type=1, name=f'''{len(bot.guilds)} servers'''))
    	await asyncio.sleep(2)

@bot.command(name="hi")
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)
    
bot.run("NjQ1Mjc3MDY5NDcwNzI4MjEy.X9zdjA.rixnPSLI3qu0Bi32UT80RncexjU",bot=False)
