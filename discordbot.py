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

@slash.context_menu(target=ContextMenuType.USER,
                    name="avatar",
                    guild_ids=guild_ids)
async def commandname(ctx: MenuContext):
    await ctx.send(
        content=f"this!\n{ctx.target_author.avatar_url}",
        hidden=False
    )

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
async def romaji(ctx, genbunn: str):
    genbun = genbunn
    genbun = genbun.replace('ka', 'か')
    genbun = genbun.replace('sa', 'さ')
    genbun = genbun.replace('ta', 'た')
    genbun = genbun.replace('na', 'な')
    genbun = genbun.replace('ha', 'は')
    genbun = genbun.replace('ma', 'ま')
    genbun = genbun.replace('ya', 'や')
    genbun = genbun.replace('ra', 'ら')
    genbun = genbun.replace('ga', 'が')
    genbun = genbun.replace('za', 'ざ')
    genbun = genbun.replace('da', 'だ')
    genbun = genbun.replace('ba', 'ば')
    genbun = genbun.replace('pa', 'ぱ')
    genbun = genbun.replace('la', 'ぁ')
    genbun = genbun.replace('lya', 'ゃ')
    genbun = genbun.replace('lwa', 'ゎ')
    genbun = genbun.replace('xa', 'ぁ')
    genbun = genbun.replace('kya', 'きゃ')
    genbun = genbun.replace('sya', 'しゃ')
    genbun = genbun.replace('sha', 'しゃ')
    genbun = genbun.replace('tya', 'ちゃ')
    genbun = genbun.replace('cha', 'ちゃ')
    genbun = genbun.replace('nya', 'にゃ')
    genbun = genbun.replace('hya', 'ひゃ')
    genbun = genbun.replace('mya', 'みゃ')
    genbun = genbun.replace('xya', 'ゃ')
    genbun = genbun.replace('rya', 'りゃ')
    genbun = genbun.replace('wa', 'わ')
    genbun = genbun.replace('gya', 'ぎゃ')
    genbun = genbun.replace('zya', 'じゃ')
    genbun = genbun.replace('ja', 'じゃ')
    genbun = genbun.replace('jya', 'じゃ')
    genbun = genbun.replace('dya', 'ぢゃ')
    genbun = genbun.replace('bya', 'びゃ')
    genbun = genbun.replace('pya', 'ぴゃ')
    genbun = genbun.replace('va', 'ゔぁ')
    genbun = genbun.replace('fa', 'ふぁ')
    genbun = genbun.replace('la', 'あ')
    genbun = genbun.replace('ki', 'き')
    genbun = genbun.replace('si', 'し')
    genbun = genbun.replace('ti', 'ち')
    genbun = genbun.replace('ni', 'に')
    genbun = genbun.replace('hi', 'ひ')
    genbun = genbun.replace('mi', 'み')
    genbun = genbun.replace('ri', 'り')
    genbun = genbun.replace('sh', 'し')
    genbun = genbun.replace('chi', 'ち')
    genbun = genbun.replace('gi', 'ぎ')
    genbun = genbun.replace('zi', 'じ')
    genbun = genbun.replace('ji', 'じ')
    genbun = genbun.replace('di', 'ぢ')
    genbun = genbun.replace('bi', 'び')
    genbun = genbun.replace('pi', 'ぴ')
    genbun = genbun.replace('li', 'ぃ')
    genbun = genbun.replace('xi', 'ぃ')
    genbun = genbun.replace('wi', 'うぃ')
    genbun = genbun.replace('vi', 'ゔぃ')
    genbun = genbun.replace('thi', 'てぃ')
    genbun = genbun.replace('fi', 'ふぃ')
    genbun = genbun.replace('dhi', 'でぃ')
    genbun = genbun.replace('i', 'い')
    genbun = genbun.replace('ku', 'く')
    genbun = genbun.replace('su', 'す')
    genbun = genbun.replace('tu', 'つ')
    genbun = genbun.replace('nu', 'ぬ')
    genbun = genbun.replace('yu', 'ゆ')
    genbun = genbun.replace('ru', 'る')
    genbun = genbun.replace('hu', 'ふ')
    genbun = genbun.replace('mu', 'む')
    genbun = genbun.replace('fu', 'ふ')
    genbun = genbun.replace('gu', 'ぐ')
    genbun = genbun.replace('zu', 'ず')
    genbun = genbun.replace('du', 'づ')
    genbun = genbun.replace('bu', 'ぶ')
    genbun = genbun.replace('pu', 'ぷ')
    genbun = genbun.replace('lu', 'ぅ')
    genbun = genbun.replace('xu', 'ぅ')
    genbun = genbun.replace('kyu', 'きゅ')
    genbun = genbun.replace('syu', 'しゅ')
    genbun = genbun.replace('shu', 'しゅ')
    genbun = genbun.replace('tyu', 'ちゅ')
    genbun = genbun.replace('chu', 'ちゅ')
    genbun = genbun.replace('nyu', 'にゅ')
    genbun = genbun.replace('hyu', 'ひゅ')
    genbun = genbun.replace('myu', 'みゅ')
    genbun = genbun.replace('lyu', 'ゅ')
    genbun = genbun.replace('xyu', 'ゅ')
    genbun = genbun.replace('ryu', 'りゅ')
    genbun = genbun.replace('gyu', 'ぎゅ')
    genbun = genbun.replace('zyu', 'じゅ')
    genbun = genbun.replace('ju', 'じゅ')
    genbun = genbun.replace('jyu', 'じゅ')
    genbun = genbun.replace('dyu', 'ぢゅ')
    genbun = genbun.replace('byu', 'びゅ')
    genbun = genbun.replace('pyu', 'ぴゅ')
    genbun = genbun.replace('vu', 'ゔ')
    genbun = genbun.replace('twu', 'とぅ')
    genbun = genbun.replace('ltu', 'っ')
    genbun = genbun.replace('xtu', 'っ')
    genbun = genbun.replace('fyu', 'ふゅ')
    genbun = genbun.replace('dhu', 'でゅ')
    genbun = genbun.replace('dwu', 'どぅ')
    genbun = genbun.replace('u', 'う')
    genbun = genbun.replace('ke', 'け')
    genbun = genbun.replace('se', 'せ')
    genbun = genbun.replace('te', 'て')
    genbun = genbun.replace('ne', 'ね')
    genbun = genbun.replace('he', 'へ')
    genbun = genbun.replace('me', 'め')
    genbun = genbun.replace('re', 'れ')
    genbun = genbun.replace('ge', 'げ')
    genbun = genbun.replace('ze', 'ぜ')
    genbun = genbun.replace('de', 'で')
    genbun = genbun.replace('be', 'べ')
    genbun = genbun.replace('pe', 'ぺ')
    genbun = genbun.replace('le', 'ぇ')
    genbun = genbun.replace('xe', 'ぇ')
    genbun = genbun.replace('sye', 'しぇ')
    genbun = genbun.replace('she', 'しぇ')
    genbun = genbun.replace('tye', 'ちぇ')
    genbun = genbun.replace('che', 'ちぇ')
    genbun = genbun.replace('we', 'うぇ')
    genbun = genbun.replace('zye', 'じぇ')
    genbun = genbun.replace('je', 'じぇ')
    genbun = genbun.replace('jye', 'じぇ')
    genbun = genbun.replace('ve', 'ゔぇ')
    genbun = genbun.replace('fe', 'ふぇ')
    genbun = genbun.replace('e', 'え')
    genbun = genbun.replace('ko', 'こ')
    genbun = genbun.replace('so', 'そ')
    genbun = genbun.replace('to', 'と')
    genbun = genbun.replace('no', 'の')
    genbun = genbun.replace('ho', 'ほ')
    genbun = genbun.replace('mo', 'も')
    genbun = genbun.replace('yo', 'よ')
    genbun = genbun.replace('ro', 'ろ')
    genbun = genbun.replace('wo', 'を')
    genbun = genbun.replace('go', 'ご')
    genbun = genbun.replace('zo', 'ぞ')
    genbun = genbun.replace('do', 'ど')
    genbun = genbun.replace('bo', 'ぼ')
    genbun = genbun.replace('po', 'ぽ')
    genbun = genbun.replace('lo', 'ぉ')
    genbun = genbun.replace('xo', 'ぉ')
    genbun = genbun.replace('kyo', 'きょ')
    genbun = genbun.replace('syo', 'しょ')
    genbun = genbun.replace('sho', 'しょ')
    genbun = genbun.replace('tyo', 'ちょ')
    genbun = genbun.replace('cho', 'ちょ')
    genbun = genbun.replace('nyo', 'にょ')
    genbun = genbun.replace('hyo', 'ひょ')
    genbun = genbun.replace('myo', 'みょ')
    genbun = genbun.replace('lyo', 'ょ')
    genbun = genbun.replace('xyo', 'ょ')
    genbun = genbun.replace('gyo', 'ぎょ')
    genbun = genbun.replace('zyo', 'じょ')
    genbun = genbun.replace('jo', 'じょ')
    genbun = genbun.replace('jyo', 'じょ')
    genbun = genbun.replace('dyo', 'ぢょ')
    genbun = genbun.replace('byo', 'びょ')
    genbun = genbun.replace('pyo', 'ぴょ')
    genbun = genbun.replace('vo', 'ゔぉ')
    genbun = genbun.replace('fo', 'ふぉ')
    genbun = genbun.replace('o', 'お')
    genbun = genbun.replace('nn', 'ん')
    genbun = genbun.replace('n', 'ん')
    await ctx.send(genbun)

client.run(os.environ['DISCORD_BOT_TOKEN'])
