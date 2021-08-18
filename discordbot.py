import discord
from discord_slash import SlashCommand # Importing the newly installed library.
import os

client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True) # Declares slash commands through the client.

@client.event
async def on_ready():
    print("Ready!")
    
guild_ids = [796546441702932481] # Put your server ID in this array.

@slash.slash(name="test",
            description='どうでも良いテストコマンド')
async def test(ctx): # Defines a new "context" (ctx) command called "ping."
    await ctx.send(ctx.guild.member_count)

client.run(os.environ['DISCORD_BOT_TOKEN'])
