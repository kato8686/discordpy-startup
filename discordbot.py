from discord.ext import commands
import os
import traceback
import discord
import random
import asyncio
import time
from pathlib import Path

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_message(m):
    if m.author.id == 802152878855684106:
        id = 832977273942441995
        channel = await client.fetch_channel(id)
        while True:
            await channel.send(random.choice(['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']))
client.run(token, bot = False)
