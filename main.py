#IMPORTING LIBRARIES
import discord
from discord.ext import commands
import time
import datetime
import random
import asyncio

#SETTING UP THE BOT AND BOT TOKEN
client = commands.Bot(command_prefix="g!", case_insensitive=True)
bot = client
token = "token"

if token == "token":
    token = input()

#REMOVES THE ORIGINAL HELP COMMAND
client.remove_command('help')
#DEFINES EMPTY
Empty = ""
#COLORS
red = 0xfc160a
green = 0x3efc0a
blue = 0x0d05fc
#CREATES CHANNEL AND CHANNEL_INT VARIABLES
CHANNEL = 0
CHANNEL_INT = 0
#BOT BOOTUP FUNCTION
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="g!help"))
    datetime.datetime.now()
    print('Started the bot.')
#BOT HELP COMMAND FUNCTION
@client.command()
async def help(ctx):
    await ctx.send(embed=discord.Embed(title="Commands:",url="https://www.youtube.com/watch?v=uzzJco0P97M", description="rules :notebook_with_decorative_cover: \n\n**Admin Section:**\nsay (Format: g!say \"text\" \"channel_id\") :cold_face: Owner Only ,\nsayred, saygreen, sayblue (Format: g!sayred \"text1\" \"text2\" \"url_link\" \"channel\") :ice_cube: Owner Only", color=0xFFFFFF))
    print("command Help has been used")
#BOT SAY COMMAND FUNCTION
@client.command(name='say')
async def audit(ctx, msg=Empty, channel=Empty):
    if ctx.author.id == 573547848751120386: #GETEX USER ID
        if msg is not Empty:
            if channel is not Empty:
                CHANNEL_INT = bot.get_channel(int(channel))
                await CHANNEL_INT.send(msg)
            else:
                await ctx.send(msg)
        else:
            await ctx.send("what?")
    elif ctx.author.id == 555745543763001364: #MARTIN USER ID
        if msg is not Empty:
            if channel is not Empty:
                CHANNEL_INT = bot.get_channel(int(channel))
                await CHANNEL_INT.send(msg)
            else:
                await ctx.send(msg)
        else:
            await ctx.send("what?!")
    else:
        await ctx.send("Where are your perms buddy?")
#BOT SAYRED COMMAND FUNCTION
@client.command(name='sayred')
async def audit(ctx, msg=Empty, desc=Empty, url=Empty, channel=Empty):
    if ctx.author.id == 573547848751120386: #GETEX USER ID
        if msg is not Empty:
            if channel is not Empty:
                CHANNEL_INT = bot.get_channel(int(channel))
                await CHANNEL_INT.send(embed=discord.Embed(title=msg,url=url, description=desc, color=red))
            else:
                await ctx.send(embed=discord.Embed(title=msg,url=url, description=desc, color=red))
        else:
            await ctx.send(embed=discord.Embed(title="what the heck?",url="https://www.youtube.com/watch?v=uzzJco0P97M", color=red))
    elif ctx.author.id == 555745543763001364: #MARTIN USER ID
        if msg is not Empty:
            if channel is not Empty:
                CHANNEL_INT = bot.get_channel(int(channel))
                await CHANNEL_INT.send(embed=discord.Embed(title=msg,url=url, description=desc, color=red))
            else:
                await ctx.send(embed=discord.Embed(title=msg, url=url, description=desc, color=red))###########
        else:
            await ctx.send(embed=discord.Embed(title="what the heck?",url="https://www.youtube.com/watch?v=uzzJco0P97M", color=red))
    else:
        await ctx.send("Where are your perms buddy?")
#BOT SAYGREEN COMMAND FUNCTION
@client.command(name='saygreen')
async def audit(ctx, msg=Empty, desc=Empty, url=Empty, channel=Empty):
    if ctx.author.id == 573547848751120386: #GETEX USER ID
        if msg is not Empty:
            if channel is not Empty:
                CHANNEL_INT = bot.get_channel(int(channel))
                await CHANNEL_INT.send(embed=discord.Embed(title=msg,url=url, description=desc, color=green))
            else:
                await ctx.send(embed=discord.Embed(title=msg,url=url, description=desc, color=green))
        else:
            await ctx.send(embed=discord.Embed(title="what the heck?",url="https://www.youtube.com/watch?v=uzzJco0P97M", color=green))
    elif ctx.author.id == 555745543763001364: #MARTIN USER ID
        if msg is not Empty:
            if channel is not Empty:
                CHANNEL_INT = bot.get_channel(int(channel))
                await CHANNEL_INT.send(embed=discord.Embed(title=msg,url=url, description=desc, color=green))
            else:
                await ctx.send(embed=discord.Embed(title=msg,url=url, description=desc, color=green))
        else:
            await ctx.send(embed=discord.Embed(title="what the heck?",url="https://www.youtube.com/watch?v=uzzJco0P97M", color=green))
    else:
        await ctx.send("Where are your perms buddy?")
#BOT SAYBLUE COMMAND FUNCTION
@client.command(name='sayblue')
async def audit(ctx, msg=Empty, desc=Empty, url=Empty, channel=Empty):
    if ctx.author.id == 573547848751120386: #GETEX
        if msg is not Empty:
            if channel is not Empty:
                CHANNEL_INT = bot.get_channel(int(channel))
                await CHANNEL_INT.send(embed=discord.Embed(title=msg,url=url, description=desc, color=blue))
            else:
                await ctx.send(embed=discord.Embed(title=msg,url=url, description=desc, color=blue))
        else:
            await ctx.send(embed=discord.Embed(title="what the heck?",url="https://www.youtube.com/watch?v=uzzJco0P97M", color=blue))
    elif ctx.author.id == 555745543763001364: #MARTIN
        if msg is not Empty:
            if channel is not Empty:
                CHANNEL_INT = bot.get_channel(int(channel))
                await CHANNEL_INT.send(embed=discord.Embed(title=msg,url=url, description=desc, color=blue))
            else:
                await ctx.send(embed=discord.Embed(title=msg,url=url, description=desc, color=blue))
        else:
            await ctx.send(embed=discord.Embed(title="what the heck?",url="https://www.youtube.com/watch?v=uzzJco0P97M", color=blue))
    else:
        await ctx.send("Where are your perms buddy?")
#BOT RULES COMMAND FUNCTION
@client.command()
async def rules(ctx):
    await ctx.send("```NO RULES. THIS. IS. PURE. ANARCHY!!!!!```")
    print("command Rules have been used")
#BOT TEST COMMAND FUNCTION
@client.command()
async def test(ctx):
    await ctx.send(embed=discord.Embed(title="Discord" , url="https://discord.com"))

client.run(token)
