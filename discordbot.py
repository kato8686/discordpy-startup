from discord.ext import commands
import os
import traceback
import discord
import random
import asyncio
import time

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
    await ctx.channel.send('pongだよ！！！！！！')
@bot.command()
async def help(ctx):
    help = discord.Embed(title='Help(β)', description='y.ping　おなじみ（？）\ny.hello　なんか\ny.pong　おなじみ（？）\ny.slot　スロット')
    await ctx.channel.send(embed=help)
@bot.command()
async def pong(ctx):
    await ctx.channel.send('ぴんぐぽーんぐ♪')
@bot.command()
async def slot(ctx):
    tousen = 0
    await ctx.channel.send('何回実行しますか？\n（バックグラウンド実行のためログは出力されません）')
    def slotcheck(m):
        return m.author == ctx.author and m.channel == ctx.channel
    msg = await bot.wait_for('message', check=slotcheck)
    try:
        num = int(msg.content)
    except ValueError:
        await ctx.channel.send('数値を指定してください')
    else:
        await ctx.channel.send(f'{int(msg.content)}回実行します\n所要時間：{int(msg.content) * 1 - 1}秒')
        message = await ctx.author.send(f'{msg.content}回実行中\n〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜')
        for i in range(int(msg.content)):
            a,b,c = random.randint(1,9),random.randint(1,9),random.randint(1,9)
            if a == b == c:
                tousen += 1
            await message.edit(content=f'{msg.content}回実行中\n{i+1}回終了\n{tousen}回当選\n〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜')
            time.sleep(1)
        await message.edit(f'終了しました\n当選回数{tousen}\n実行回数{msg.content}\n〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜')

bot.run(token)
