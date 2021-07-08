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

bot = commands.Bot(command_prefix='y.', help_command=None)
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

bot.run(token)
