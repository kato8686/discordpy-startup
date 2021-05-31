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
async def on_massage(m):
    if m.content == 'y.hello':
        await m.channel.send('hello')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)
