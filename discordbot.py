from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='y.')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def hello(ctx):
    await ctx.send('good')
async def ping(ctx):
    await ctx.send('pongだよ！！！！！！！！！')

@commands.command()
async def help!(ctx):
    embed = discord.Embed(title='Help', description='y.ping：おなじみ¥ny.hello：気分で変わる')
    await ctx.send(embed=embed)

bot.add_command(help!)

bot.run(token)
