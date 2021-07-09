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
    help = discord.Embed(title='Help(β)', description='y.ping　おなじみ（？）　動作中\ny.hello　なんか　動作中\ny.pong　おなじみ（？）　動作中\ny.slot　スロット　動作中\ny.start　カウント　動作中\ny.stop　カウントをストップ　動作中y.ping　おなじみ（？）　動作中\n\n以下は管理者のみ\ny.manage　コマンドの管理\ny.shutdown　そのまま\n\n不具合があればyuiyuinagaming864649@gmail.comへ')
    await ctx.channel.send(embed=help)

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
    embed = discord.Embed(title='user information', description=f'```\nUser name ：{ctx.author.name}#{ctx.author.discriminator}\nUser id   ：{ctx.author.id}\nBot?      ：{ctx.author.bot}\navatar url[{ctx.author.avatar_url}]\n```')
    await ctx.channel.send(f'```\nUser name ：{ctx.author.name}#{ctx.author.discriminator}\nUser id   ：{ctx.author.id}\nBot?      ：{ctx.author.bot}\navatar url：{ctx.author.avatar_url}\n```')

bot.run(token)
