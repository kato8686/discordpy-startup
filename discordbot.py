import discord
from discord_slash import SlashCommand # Importing the newly installed library.
import os
from discord_slash.utils.manage_commands import create_option, create_choice, create_permission
from discord_slash.model import SlashCommandPermissionType, ContextMenuType
from discord_slash.context import MenuContext

client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True) # Declares slash commands through the client.

@client.event
async def on_ready():
    print("Ready!")
    
guild_ids = [796546441702932481] # Put your server ID in this array.

@slash.context_menu(target=ContextMenuType.USER,
                    name="avatar",
                    guild_ids=[796546441702932481])
async def commandname(ctx: MenuContext):
    await ctx.send(
        content=f"this!\n{ctx.target_author.avatar}",
        hidden=False
    )

client.run(os.environ['DISCORD_BOT_TOKEN'])
