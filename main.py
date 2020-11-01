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
    	await bot.change_presence(activity=discord.Activity(type=1,name="with LOVE YOU MOM DAD"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with R€FL€X ॥乛♥P⃠𝙖 𝙧 𝙖 𝙢#0005"))
    	await asyncio.sleep(5)
	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with all members !"))
    	await asyncio.sleep(5)

        await bot.change_presence(activity=discord.Activity(type=1,name="with want HQ Life in 1.2rs DM me !"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with  Trivia Master || Bots !"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with  my all friends !"))
    	await asyncio.sleep(5)

        await bot.change_presence(activity=discord.Activity(type=1,name="with  Subrata#3297 !"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with SPIDER TRIVIA || Bot !"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with all Trivia Games !"))
    	await asyncio.sleep(5)

        await bot.change_presence(activity=discord.Activity(type=1,name="with want Vedantu life DM me !"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with TRIVIA EMPIRE !"))
    	await asyncio.sleep(5)

        await bot.change_presence(activity=discord.Activity(type=1,name="with TRIVIA || DANGER★᭄ꦿ᭄ !"))
    	await asyncio.sleep(5)
	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with your Love😍!"))
    	await asyncio.sleep(5)
	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with DANGER TRIVIA || BOTS !"))
    	await asyncio.sleep(5)
	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with CHALLENGE || PHOENIX !"))
    	await asyncio.sleep(5)
	
    	await bot.change_presence(activity=discord.Activity(type=1,name="with  Trivia | Community !"))
    	await asyncio.sleep(5)
    	
    	await bot.change_presence(activity=discord.Activity(type=1, name=f'''{len(bot.guilds)} servers'''))
    	await asyncio.sleep(5)

@bot.command(name="hi")
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)
    
bot.run("NjYwMzM3MzQyMDMyMjQ4ODMy.X4xc9g.XML7C0hxrePba_yvU5zapQi3e6U",bot=False)
