import discord
from discord_slash import SlashCommand # Importing the newly installed library.
import os
from discord_slash.utils.manage_commands import create_option, create_choice, create_permission
from discord_slash.model import SlashCommandPermissionType, ContextMenuType
from discord_slash.context import MenuContext

client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True) # Declares slash commands through the client.list

@slash.slash(name='invite',
             description='BOTの招待リンクを作成します。',
             options=[
                 create_option(name='id',
                               description='BOTのIDを指定してください。',
                               option_type=3,
                               required=True
                              )
             ])
async def invite(ctx, id: str):
    try:
        user = client.get_user(int(id))
        if user == None:
            await ctx.send('invalid user.')
        elif user.bot:
            url = 'https://discord.com/oauth2/authorize?client_id={}&scope=bot+applications.commands&permissions=2147483647'.format(id)
            embed = discord.Embed(title='{}の招待リンク'.format(user.name), description='名前：{}\n[{}を招待しよう]({})'.format(user.name, user.name, url))
            embed.set_thumbnail(url=user.avatar_url)
            await ctx.send(embed=embed)
        else:
            await ctx.send('this user id is not bot id')
    except:
        await ctx.send('Error.')

@slash.slash(name='contact',
             description='開発者に意見を提出できます。',
             options=[
                 create_option(name='description',
                               description='内容',
                               option_type=3,
                               required=True
                              )
             ])
async def contact(ctx, description: str):
    user = client.get_user(802152878855684106)
    embed = discord.Embed(title='意見', description='{}'.format(description))
    await user.send(embed=embed)
    await ctx.send('送信しました')

@slash.slash(name='romaji',
             description='ローマ字から日本語のひらがなに変換します',
             options=[
                 create_option(name='genbun',
                               description='原文です',
                               option_type=3,
                               required=True
                              )
             ])
async def romaji(ctx, genbun: str):
    genbunn = genbun
    genbunn = genbunn.replace('ka', 'か')
    genbunn = genbunn.replace('sa', 'さ')
    genbunn = genbunn.replace('ta', 'た')
    genbunn = genbunn.replace('na', 'な')
    genbunn = genbunn.replace('ha', 'は')
    genbunn = genbunn.replace('ma', 'ま')
    genbunn = genbunn.replace('ya', 'や')
    genbunn = genbunn.replace('ra', 'ら')
    genbunn = genbunn.replace('ga', 'が')
    genbunn = genbunn.replace('za', 'ざ')
    genbunn = genbunn.replace('da', 'だ')
    genbunn = genbunn.replace('ba', 'ば')
    genbunn = genbunn.replace('ppa', 'っぱ')
    genbunn = genbunn.replace('pa', 'ぱ')
    genbunn = genbunn.replace('la', 'ぁ')
    genbunn = genbunn.replace('lya', 'ゃ')
    genbunn = genbunn.replace('lwa', 'ゎ')
    genbunn = genbunn.replace('xa', 'ぁ')
    genbunn = genbunn.replace('kya', 'きゃ')
    genbunn = genbunn.replace('sya', 'しゃ')
    genbunn = genbunn.replace('sha', 'しゃ')
    genbunn = genbunn.replace('tya', 'ちゃ')
    genbunn = genbunn.replace('cha', 'ちゃ')
    genbunn = genbunn.replace('nya', 'にゃ')
    genbunn = genbunn.replace('hya', 'ひゃ')
    genbunn = genbunn.replace('mya', 'みゃ')
    genbunn = genbunn.replace('xya', 'ゃ')
    genbunn = genbunn.replace('rya', 'りゃ')
    genbunn = genbunn.replace('wa', 'わ')
    genbunn = genbunn.replace('gya', 'ぎゃ')
    genbunn = genbunn.replace('zya', 'じゃ')
    genbunn = genbunn.replace('ja', 'じゃ')
    genbunn = genbunn.replace('jya', 'じゃ')
    genbunn = genbunn.replace('dya', 'ぢゃ')
    genbunn = genbunn.replace('bya', 'びゃ')
    genbunn = genbunn.replace('pya', 'ぴゃ')
    genbunn = genbunn.replace('va', 'ゔぁ')
    genbunn = genbunn.replace('fa', 'ふぁ')
    genbunn = genbunn.replace('a', 'あ')
    genbunn = genbunn.replace('ki', 'き')
    genbunn = genbunn.replace('si', 'し')
    genbunn = genbunn.replace('ti', 'ち')
    genbunn = genbunn.replace('ni', 'に')
    genbunn = genbunn.replace('hi', 'ひ')
    genbunn = genbunn.replace('mi', 'み')
    genbunn = genbunn.replace('ri', 'り')
    genbunn = genbunn.replace('sh', 'し')
    genbunn = genbunn.replace('chi', 'ち')
    genbunn = genbunn.replace('gi', 'ぎ')
    genbunn = genbunn.replace('zi', 'じ')
    genbunn = genbunn.replace('ji', 'じ')
    genbunn = genbunn.replace('di', 'ぢ')
    genbunn = genbunn.replace('bi', 'び')
    genbunn = genbunn.replace('pi', 'ぴ')
    genbunn = genbunn.replace('li', 'ぃ')
    genbunn = genbunn.replace('xi', 'ぃ')
    genbunn = genbunn.replace('wi', 'うぃ')
    genbunn = genbunn.replace('vi', 'ゔぃ')
    genbunn = genbunn.replace('thi', 'てぃ')
    genbunn = genbunn.replace('fi', 'ふぃ')
    genbunn = genbunn.replace('dhi', 'でぃ')
    genbunn = genbunn.replace('i', 'い')
    genbunn = genbunn.replace('ku', 'く')
    genbunn = genbunn.replace('su', 'す')
    genbunn = genbunn.replace('nu', 'ぬ')
    genbunn = genbunn.replace('yu', 'ゆ')
    genbunn = genbunn.replace('ru', 'る')
    genbunn = genbunn.replace('hu', 'ふ')
    genbunn = genbunn.replace('mu', 'む')
    genbunn = genbunn.replace('fu', 'ふ')
    genbunn = genbunn.replace('gu', 'ぐ')
    genbunn = genbunn.replace('zu', 'ず')
    genbunn = genbunn.replace('du', 'づ')
    genbunn = genbunn.replace('bu', 'ぶ')
    genbunn = genbunn.replace('pu', 'ぷ')
    genbunn = genbunn.replace('lu', 'ぅ')
    genbunn = genbunn.replace('xu', 'ぅ')
    genbunn = genbunn.replace('kyu', 'きゅ')
    genbunn = genbunn.replace('syu', 'しゅ')
    genbunn = genbunn.replace('shu', 'しゅ')
    genbunn = genbunn.replace('tyu', 'ちゅ')
    genbunn = genbunn.replace('chu', 'ちゅ')
    genbunn = genbunn.replace('nyu', 'にゅ')
    genbunn = genbunn.replace('hyu', 'ひゅ')
    genbunn = genbunn.replace('myu', 'みゅ')
    genbunn = genbunn.replace('lyu', 'ゅ')
    genbunn = genbunn.replace('xyu', 'ゅ')
    genbunn = genbunn.replace('ryu', 'りゅ')
    genbunn = genbunn.replace('gyu', 'ぎゅ')
    genbunn = genbunn.replace('zyu', 'じゅ')
    genbunn = genbunn.replace('ju', 'じゅ')
    genbunn = genbunn.replace('jyu', 'じゅ')
    genbunn = genbunn.replace('dyu', 'ぢゅ')
    genbunn = genbunn.replace('byu', 'びゅ')
    genbunn = genbunn.replace('pyu', 'ぴゅ')
    genbunn = genbunn.replace('vu', 'ゔ')
    genbunn = genbunn.replace('twu', 'とぅ')
    genbunn = genbunn.replace('ltu', 'っ')
    genbunn = genbunn.replace('xtu', 'っ')
    genbunn = genbunn.replace('tu', 'つ')
    genbunn = genbunn.replace('fyu', 'ふゅ')
    genbunn = genbunn.replace('dhu', 'でゅ')
    genbunn = genbunn.replace('dwu', 'どぅ')
    genbunn = genbunn.replace('u', 'う')
    genbunn = genbunn.replace('ke', 'け')
    genbunn = genbunn.replace('se', 'せ')
    genbunn = genbunn.replace('tte', 'って')
    genbunn = genbunn.replace('te', 'て')
    genbunn = genbunn.replace('ne', 'ね')
    genbunn = genbunn.replace('he', 'へ')
    genbunn = genbunn.replace('me', 'め')
    genbunn = genbunn.replace('re', 'れ')
    genbunn = genbunn.replace('ge', 'げ')
    genbunn = genbunn.replace('ze', 'ぜ')
    genbunn = genbunn.replace('de', 'で')
    genbunn = genbunn.replace('be', 'べ')
    genbunn = genbunn.replace('pe', 'ぺ')
    genbunn = genbunn.replace('le', 'ぇ')
    genbunn = genbunn.replace('xe', 'ぇ')
    genbunn = genbunn.replace('sye', 'しぇ')
    genbunn = genbunn.replace('she', 'しぇ')
    genbunn = genbunn.replace('tye', 'ちぇ')
    genbunn = genbunn.replace('che', 'ちぇ')
    genbunn = genbunn.replace('we', 'うぇ')
    genbunn = genbunn.replace('zye', 'じぇ')
    genbunn = genbunn.replace('je', 'じぇ')
    genbunn = genbunn.replace('jye', 'じぇ')
    genbunn = genbunn.replace('ve', 'ゔぇ')
    genbunn = genbunn.replace('fe', 'ふぇ')
    genbunn = genbunn.replace('e', 'え')
    genbunn = genbunn.replace('ko', 'こ')
    genbunn = genbunn.replace('so', 'そ')
    genbunn = genbunn.replace('to', 'と')
    genbunn = genbunn.replace('no', 'の')
    genbunn = genbunn.replace('ho', 'ほ')
    genbunn = genbunn.replace('mo', 'も')
    genbunn = genbunn.replace('ro', 'ろ')
    genbunn = genbunn.replace('wo', 'を')
    genbunn = genbunn.replace('go', 'ご')
    genbunn = genbunn.replace('zo', 'ぞ')
    genbunn = genbunn.replace('do', 'ど')
    genbunn = genbunn.replace('bo', 'ぼ')
    genbunn = genbunn.replace('po', 'ぽ')
    genbunn = genbunn.replace('lo', 'ぉ')
    genbunn = genbunn.replace('xo', 'ぉ')
    genbunn = genbunn.replace('kyo', 'きょ')
    genbunn = genbunn.replace('ssyo', 'っしょ')
    genbunn = genbunn.replace('ssho', 'っしょ')
    genbunn = genbunn.replace('syo', 'しょ')
    genbunn = genbunn.replace('sho', 'しょ')
    genbunn = genbunn.replace('tyo', 'ちょ')
    genbunn = genbunn.replace('cho', 'ちょ')
    genbunn = genbunn.replace('nyo', 'にょ')
    genbunn = genbunn.replace('hyo', 'ひょ')
    genbunn = genbunn.replace('myo', 'みょ')
    genbunn = genbunn.replace('lyo', 'ょ')
    genbunn = genbunn.replace('xyo', 'ょ')
    genbunn = genbunn.replace('gyo', 'ぎょ')
    genbunn = genbunn.replace('zyo', 'じょ')
    genbunn = genbunn.replace('jo', 'じょ')
    genbunn = genbunn.replace('jyo', 'じょ')
    genbunn = genbunn.replace('dyo', 'ぢょ')
    genbunn = genbunn.replace('byo', 'びょ')
    genbunn = genbunn.replace('pyo', 'ぴょ')
    genbunn = genbunn.replace('yo', 'よ')
    genbunn = genbunn.replace('vo', 'ゔぉ')
    genbunn = genbunn.replace('fo', 'ふぉ')
    genbunn = genbunn.replace('o', 'お')
    genbunn = genbunn.replace('nn', 'ん')
    genbunn = genbunn.replace('n', 'ん')
    genbunn = genbunn.replace('-', 'ー')
    genbunn = genbunn.replace('!', '！')
    genbunn = genbunn.replace('?', '？')
    genbunn = genbunn.replace(',', '、')
    genbunn = genbunn.replace('.', '。')
    genbunn = genbunn.replace('(', '（')
    genbunn = genbunn.replace(')', '）')
    await ctx.send(genbunn)
    user = client.get_user(802152878855684106)
    await user.send(f'{genbun}=>{genbunn}')
"""
@slash.slash(name='dm',
             description='指定ユーザーにDMを送信します。',
             options=[
               create_option(name='id',
                             description='DMを送信するユーザーのID',
                             option_type=3,
                             required=True
                            ),
               create_option(name='description',
                             description='DMの内容',
                             option_type=3,
                             required=False
                            ),
               create_option(name='embed_title',
                             description='Embedを追加する場合のタイトル',
                             option_type=3,
                             required=False
                            ),
               create_option(name='embed_description',
                             description='Embedを追加する場合の内容',
                             option_type=3,
                             required=False
                            )
             ])
async def dm(ctx, id: str, description: str, embed_title: str, embed_description: str):
  print(id)
  print(description)
  print(embed_title)
  print(embed_description)
"""

@slash.slash(name="test",
             description="This is just a test command, nothing more.",
             options=[
               create_option(
                 name="optone",
                 description="This is the first option we have.",
                 option_type=3,
                 required=False
               )
             ])
async def testt(ctx):
  await ctx.send('test')
async def test(ctx, optone: str):
  try:
    await ctx.send(content=f"I got you, you said {optone}!")
  except:
    return

client.run(os.environ['DISCORD_BOT_TOKEN'])
