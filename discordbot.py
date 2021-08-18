import discord
from discord_slash import SlashCommand # Importing the newly installed library.
import os
from discord_slash.utils.manage_commands import create_option, create_choice, create_permission
from discord_slash.model import SlashCommandPermissionType, ContextMenuType
from discord_slash.context import MenuContext

client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True) # Declares slash commands through the client.list

guild_ids = []
for i in client.guilds:
    guild_ids.append(i.id)

@client.event
async def on_ready():
    print("Ready!")
"""
@slash.context_menu(target=ContextMenuType.USER,
                    name="avatar",
                    guild_ids=guild_ids)
async def commandname(ctx: MenuContext):
    await ctx.send(
        content=f"this!\n{ctx.target_author.avatar_url}",
        hidden=False
    )
"""
@slash.slash(name='avatar',
             description='ユーザーのアイコンを表示します。',
             options=[
                 create_option(name='user',
                               description='ユーザーのメンションを指定してください。',
                               option_type=3,
                               required=True
                              )
             ],
             guild_ids=guild_ids)
async def avatar(ctx, user: str):
    try:
        await ctx.send(client.get_user(int(user[2:21])).avatar_url)
    except:
        await ctx.send('エラー')

@slash.slash(name='romaji',
             description='ローマ字から日本語のひらがなに変換します',
             options=[
                 create_option(name='genbun',
                               description='原文です',
                               option_type=3,
                               required=True
                              )
             ],
             guild_ids=guild_ids)
async def romaji(ctx, genbun: str):
    genbun = genbun.replace('ka', 'か')
    genbun = genbun.replace('sa', 'さ')
    genbun = genbun.replace('ta', 'た')
    genbun = genbun.replace('na', 'な')
    genbun = genbun.replace('ha', 'は')
    genbun = genbun.replace('ma', 'ま')
    genbun = genbun.replace('ya', 'や')
    genbun = genbun.replace('ra', 'ら')
    genbun = genbun.replace('wa', 'わ')
    genbun = genbun.replace('a', 'あ')
    genbun = genbun.replace('ki', 'き')
    genbun = genbun.replace('si', 'し')
    genbun = genbun.replace('ti', 'ち')
    genbun = genbun.replace('ni', 'に')
    genbun = genbun.replace('hi', 'ひ')
    genbun = genbun.replace('mi', 'み')
    genbun = genbun.replace('ri', 'り')
    genbun = genbun.replace('i', 'い')
    genbun = genbun.replace('ku', 'く')
    genbun = genbun.replace('su', 'す')
    genbun = genbun.replace('tu', 'つ')
    genbun = genbun.replace('nu', 'ぬ')
    genbun = genbun.replace('yu', 'ゆ')
    genbun = genbun.replace('ru', 'る')
    genbun = genbun.replace('hu', 'ふ')
    genbun = genbun.replace('mu', 'む')
    genbun = genbun.replace('u', 'う')
    genbun = genbun.replace('ke', 'け')
    genbun = genbun.replace('se', 'せ')
    genbun = genbun.replace('te', 'て')
    genbun = genbun.replace('ne', 'ね')
    genbun = genbun.replace('he', 'へ')
    genbun = genbun.replace('me', 'め')
    genbun = genbun.replace('re', 'れ')
    genbun = genbun.replace('e', 'え')
    genbun = genbun.replace('ko', 'こ')
    genbun = genbun.replace('so', 'そ')
    genbun = genbun.replace('to', 'と')
    genbun = genbun.replace('no', 'の')
    genbun = genbun.replace('ho', 'ほ')
    genbun = genbun.replace('mo', 'も')
    genbun = genbun.replace('yo', 'よ')
    genbun = genbun.replace('ro', 'ろ')
    genbun = genbun.replace('o', 'お')
    genbun = genbun.replace('nn', 'ん')
    await ctx.send(genbun)

client.run(os.environ['DISCORD_BOT_TOKEN'])
