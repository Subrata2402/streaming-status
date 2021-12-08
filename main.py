import discord
from discord.ext import commands
import asyncio
import random

bot = discord.Client()


@bot.event
async def on_ready():
    print('Online')
    while True:
        await bot.change_presence(activity=discord.Activity(type=0,name="with 24/7 online"))
        await asyncio.sleep(2)

    	await bot.change_presence(activity=discord.Activity(type=1,name="with"))
        await asyncio.sleep(2)

    
bot.run("SELF_TOKEN",bot=False)
