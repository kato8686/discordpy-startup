import discord
from discord_slash import SlashCommand # Importing the newly installed library.
import os

client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True) # Declares slash commands through the client.

@client.event
async def on_ready():
    print("Ready!")
    
guild_ids = [796546441702932481] # Put your server ID in this array.

@slash.slash(name="ping", guild_ids=guild_ids)
async def _ping(ctx): # Defines a new "context" (ctx) command called "ping."
    await ctx.send(f"Pong! ({client.latency*1000}ms)")

client.run(os.environ['DISCORD_BOT_TOKEN'])
