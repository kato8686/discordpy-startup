from discord.ext import commands
import os
import traceback
import discord
import random

bot = commands.Bot(command_prefix='y.', help_command=None)
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def hello(ctx):
    await ctx.channel.send('good')
@bot.command()
async def ping(ctx):
    await ctx.channel.send('pongだよ！！！！！！！！！')
@bot.command()
async def help(ctx):
    help = discord.Embed(title='Help(β)', description='y.ping　おなじみ（？）\ny.hello　なんか\ny.pong　おなじみ（？）')
    await ctx.channel.send(embed=help)
@bot.command()
async def pong(ctx):
    await ctx.channel.send('ぴんぐぽーんぐ♪')
@bot.command()
await def slot(ctx, arg):
    a,b,c = random.randint(1,9),random.randint(1,9),random.randint(1,9)
    await ctx.channel.send(f'{a} {b} {c}')
    if a == b == c:
        await ctx.author.send('当たったよ')

bot.run(token)
