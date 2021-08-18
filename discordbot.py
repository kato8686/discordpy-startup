import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
import os
from discord_slash.utils.manage_commands import create_option

bot = commands.Bot(command_prefix='@', intents=discord.Intents.all())

slash_client = SlashCommand(bot)

@slash_client.slash(name='test', description='test', options=[create_option(name='testoption', description='めっちゃテスト', option_type=3, required=False)]))])
async def test(ctx, option: str):
    await ctx.send(option)

bot.run(os.environ['DISCORD_BOT_TOKEN'])
