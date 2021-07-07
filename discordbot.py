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

async_compile = functools.partial(compile,
    mode="exec",
    filename="<discord>",
    flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT)
bot = commands.Bot(command_prefix='y.', help_command=None)
token = os.environ['DISCORD_BOT_TOKEN']
admin = [790054604799868939, 802152878855684106, 695996824112332887, 594404458327310336]
owner = [802152878855684106]

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def eval(ctx):
    if ctx.author.id == 802152878855684106:
        args = message.content.splitlines()
        code = ""
        for x in args[1:]:
            code += "\n" + x
        exec(code)
@bot.command()
async def hello(ctx):
    await ctx.channel.send('good')
@bot.command()
async def ping(ctx):
    await ctx.channel.send('pongだよ！！！！！')
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
    await ctx.channel.send(content = '何回実行しますか？\n（バックグラウンド実行のためログは出力されません）')
    def slotcheck(m):
        return m.author == ctx.author and m.channel == ctx.channel
    msg = await bot.wait_for('message', check=slotcheck)
    try:
        num = int(msg.content)
    except ValueError:
        await ctx.channel.send('数値を指定してください')
    else:
        if int(msg.content) <= 3600 or ctx.author.id in admin:
            s = ''
            await ctx.channel.send(f'{int(msg.content)}回実行します\n所要時間：{int(msg.content) * 1 - 1}秒')
            message = await ctx.author.send(f'```\n{msg.content}回実行中\n```')
            for i in range(int(msg.content)):
                a,b,c = random.randint(1,9),random.randint(1,9),random.randint(1,9)
                if a == b == c:
                    tousen += 1
                    s += f'{a} {b} {c} （{i+1}回目）\n'
                await message.edit(content=f'```\n{msg.content}回実行中\n{i+1}回終了\n{tousen}回当選\n{s}\n```')
                time.sleep(1)
            await message.edit(content=f'```\n終了しました\n当選回数{tousen}\n実行回数{msg.content}\n{s}\n```\n当選回数をスコアに換算しますか？（yes or no）')
            def admincheck(m):
                return m.author.id == ctx.author.id
            message = await bot.wait_for('message', check=admincheck)
            if message.content == 'yes':
                await message.author.send(f'{tousen*3}point取得しました！')
            else:
                await message.author.send('中止しました')
        else:
            await ctx.channel.send('長すぎます\nリミッターを外すにはADMINになる必要があります。\nADMIN申請しますか？？？（yes or no）')
            def admincheck(m):
                return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id
            message = await bot.wait_for('message', check=admincheck)
            if message.content == 'yes':
                id = owner[0]
                user = await bot.fetch_user(id)
                await user.send(f'ADMIN申請\n{ctx.author.name}\n{ctx.author.id}')
            else:
                await ctx.send('申請しませんでした')
@bot.command()
async def fack(ctx):
    await ctx.channel.send('は？？？')
@bot.command()
async def 隠しコマンドの代名詞(ctx, args, args_2):
    id = int(args)
    channel = await bot.fetch_channel(id)
    list = list(map(str, args_2.split()))
    args_2 = ''
    for i in list:
        args_2 = args_2 + i
    await channel.send(args_2)
@bot.command()
async def start(ctx):
    id = 858555560831483914
    channel = await bot.fetch_channel(id)
    i = 1364
    for i in range(1, 10000000):
        await channel.send(str(i))
        i = int(i)
        i += 1

bot.run(token)
