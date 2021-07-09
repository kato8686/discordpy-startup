from discord.ext import commands
import os
import traceback
import discord
import random
import asyncio
import time
from pathlib import Path
import ast
import functools

#a6

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='y.', help_command=None, intents=intents)
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def ping(ctx):
    return

@bot.command()
async def pong(ctx):
    return

@bot.command()
async def hello(ctx):
    return

@bot.command()
async def start(ctx):
    return

@bot.command()
async def stop(ctx):
    return

@bot.command()
async def slot(ctx):
    return

@bot.command()
async def help(ctx):
    return

@bot.command()
async def manage(ctx):
    return

@bot.command()
async def shutdown(ctx):
    return

@bot.command()
async def 隠しコマンドの代名詞(ctx):
    gu = bot.guilds
    for i in gu:
        id = i.owner_id
        user = await bot.fetch_user(id)
        await ctx.channel.send(f'{i.name}：{user.name}')

@bot.command()
async def ui(ctx):
    return

@bot.command()
async def contact(ctx):
    return

bot.run(token)
