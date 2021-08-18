import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
import os
from discord_slash.utils.manage_commands import create_option

bot = commands.Bot(command_prefix='@', intents=discord.Intents.all())

slash_client = SlashCommand(bot)

@slash_client.slash(name="test", description="This is just a test command, nothing more.", options=[create_option(name="optone", description="This is the first option we have.", option_type=3, required=False)])
async def test(ctx, optone: str):
    await ctx.send(content=f"I got you, you said {optone}!")

bot.run(os.environ['DISCORD_BOT_TOKEN'])
