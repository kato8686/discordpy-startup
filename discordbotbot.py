import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

bot = commands.Bot(command_prefix='@', intents=discord.Intents.all())

slash_client = SlashCommand(bot)

@slash_client.slash(name="test")
async def _slash_hello(ctx: SlashContext):
    await ctx.send(content="Hello!")

bot.run(os.environ['DISCORD_BOT_TOKEN'])
