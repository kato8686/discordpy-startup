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
async def .help(ctx):
    embed = discord.Embed(title='Help', description='y.ping：応答速度を測ります（手動）\ny.hello：なんか返します')
    await ctx.send(embed=embed)

bot.run(token)
