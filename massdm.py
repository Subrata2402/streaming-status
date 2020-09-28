import discord
from discord.ext import commands
from.discord.ext.commands import Bot

bot=commands.Bot(command_prefix="+")
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print("Made by Mr.Subrata")
    print(bot.user.id)
@bot.command(pass_context=True)
async def dmail(ctx,*,message,):
    for members in bot.get_all_members():
        try:
                embed=discord.Embed(description=message, color=0x00FF00)
                embed.set_author(name="DM BOT")
                embed.set_footer(text="Made by Mr.Subrata#3297")
                await bot.send_message(members,embed=embed)
                x=y
                y=x+1
                await bot.say("sended()message!".format(y))
           except Exception        
                continue
           else:
               break
bot.run("TOKEN")               
