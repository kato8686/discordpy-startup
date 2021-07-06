import discord
import time
import random
import os

token = os.environ[DISCORD_BOT_TOKEN]

client = discord.Client()

@client.event
async def on_message(m):
    if m.author.id == 802152878855684106 and m.content == 'start':
        await m.delete()
        random_count = random.randint(1,1000)
        channel = await client.fetch_channel(832977273942441995)
        await channel.send(random_count)
        await channel.send("start")
        time.sleep(1)
    elif m.author.id == 802152878855684106 and m.content == 'end':
        await client.logout()
        await client.close()
client.run(token, bot=False)
