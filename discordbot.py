from discord.ext import commands
import os
import traceback
import discord
import random

bot = commands.Bot(command_prefix='y.', help_command=None)
token = os.environ['DISCORD_BOT_TOKEN']
slot = []
slotbool = False
global slotbool

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
    help = discord.Embed(title='Help(β)', description='y.ping　おなじみ（？）\ny.hello　なんか\ny.pong　おなじみ（？）\ny.slot　スロット')
    await ctx.channel.send(embed=help)
@bot.command()
async def pong(ctx):
    await ctx.channel.send('ぴんぐぽーんぐ♪')
@bot.command()
async def slot(ctx, arg):
    await ctx.channel.send(f'{arg}回スロットをします\n「y.stop」とそのチャンネルで発言すると止まります')
    slotbool = True
    slot.append([ctx.author.id, ctx.channel.id])
    for i in range(int(arg)):
        if slotbool:
            a,b,c = random.randint(1,9),random.randint(1,9),random.randint(1,9)
            msg = await ctx.channel.send(f'{a} {b} {c}')
            if a == b == c:
                await ctx.author.send(f'当たったよ\n{msg.jump_url}')
                id = 848897434063339541
                channel = bot.get_channel(id)
                await channel.send(f'スロット当選\n{msg.jump_url}\nユーザー名　{ctx.author.name}\nチャンネル名 {ctx.channel.name}\nギルド名　{ctx.guild.name}')
@bot.command()
async def stop(ctx):
    for i in slot:
        if ctx.author.id in i and ctx.channel.id in i:
            slotbool = False

bot.run(token)
