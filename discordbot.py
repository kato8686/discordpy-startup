"""
import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
import os

bot = commands.Bot(command_prefix='@', intents=discord.Intents.all())

slash_client = SlashCommand(bot)

@slash_client.slash(name='test')
async def _slash_hello(ctx: SlashContext):
    await ctx.send('hello')

bot.run(os.environ['DISCORD_BOT_TOKEN'])
"""
import requests

url = "https://discord.com/api/v8/applications/<APPLICATION ID>/guilds/<GUILD ID>/commands"

json = {
    "name": "blep",
    "description": "Send a random adorable animal photo",
    "options": [
        {
            "name": "animal",
            "description": "The type of animal",
            "type": 3,
            "required": True,
            "choices": [
                {
                    "name": "Dog",
                    "value": "animal_dog"
                },
                {
                    "name": "Cat",
                    "value": "animal_cat"
                },
                {
                    "name": "Penguin",
                    "value": "animal_penguin"
                }
            ]
        },
        {
            "name": "only_smol",
            "description": "Whether to show only baby animals",
            "type": 5,
            "required": False
        }
    ]
}

headers = {
    "Authorization": f"Bot {os.environ['DISCORD_BOT_TOKEN']}"
}

r = requests.post(url, headers=headers, json=json)
print(r.status_code)
