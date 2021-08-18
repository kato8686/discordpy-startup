import discord
from discord_slash import SlashCommand # Importing the newly installed library.
import os
from discord_slash.utils.manage_commands import create_option, create_choice

client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True) # Declares slash commands through the client.

@client.event
async def on_ready():
    print("Ready!")
    
guild_ids = [796546441702932481] # Put your server ID in this array.

@slash.slash(name="test",
             description='どうでも良いテストコマンド',
             options=[
                 create_option(
                     name='option',
                     description='testing now',
                     option_type=3,
                     required=False,
                     choices=[
                         create_choice(
                             name='yes',
                             value='true'
                         ),
                         create_choice(
                             name='no',
                             value='false'
                         )
                     ]
                 )
             ])
async def test(ctx, option: str): # Defines a new "context" (ctx) command called "ping."
    await ctx.send(content=option)

client.run(os.environ['DISCORD_BOT_TOKEN'])
