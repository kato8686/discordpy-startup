from discord.ext import commands
import os
import traceback
import discord
import random
import asyncio
import time
from pathlib import Path

global evbool
evbool = True
bot = commands.Bot(command_prefix='y.', help_command=None)
token = os.environ['DISCORD_BOT_TOKEN']
admin = [790054604799868939, 802152878855684106, 695996824112332887, 594404458327310336]
owner = [802152878855684106]

@bot.event
async def on_command_error(ctx):
    await ctx.channel.send(f'{ctx.content}は存在しません！')

@bot.command()
async def ev(ctx):
    if evbool:
        a = random.randint(1,3000)
        if a == 2536:
            await ctx.channel.send(f'<@{ctx.author.id}>おめでとう！\n管理人に連絡して特典をもらおう！')
            evbool = False

bot.run(token)
