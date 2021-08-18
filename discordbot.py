# -*- coding: utf-8 -*-

#webhook test

import psycopg2
import asyncio
import discord
import io
from contextlib import redirect_stdout
import traceback
from pathlib import Path
import os
import random
import datetime
intents = discord.Intents.all()
client = discord.Client(intents=intents)
TOKEN = os.environ['DISCORD_BOT_TOKEN']
prefix = 'y.'
owner_id = 802152878855684106
kidou_id = 865364213878620171
server_id = 857204248807079977
welcome = 'FubukiBOT公式鯖へようこそ！\nこの鯖ではニトロ抽選や最新情報のお知らせを行っています！\nぜひ抜けずにこのまま残っていてください！\n今後ともFubukiBOTをよろしくお願いします！'
global count
count = 0
def get_connection():
    dsn = os.environ['DATABASE_URL']
    return psycopg2.connect(dsn)
con = get_connection()
cur = con.cursor()
@client.event
async def on_message(m):
    global count
    count += 1
    if count == 1:
        now = datetime.datetime.now()
        await client.get_channel(kidou_id).send(embed=discord.Embed(title='起動！', description=f'{now.year}年{now.month}月{now.day}日{now.hour + 9}時{now.minute}分{now.second}秒'))
        game = discord.Game(name=f'{prefix}help|{len(client.guilds)}サーバー')
        await client.change_presence(activity=game)
    def check(me):
        return me.author == m.author and me.channel == m.channel
    if m.author.bot:
        return
    elif m.content == f'{prefix}eval':
        if m.author.id == owner_id:
            await m.reply('実行するコードをどうぞ\nコードブロックでもokです', mention_author=False)
            def check(me):
                return me.channel == m.channel and me.author == m.author
            msg = await client.wait_for('message', check=check)
            code = msg.content.replace('```', '').replace('py', '')
            try:
                f = io.StringIO()
                with redirect_stdout(f):
                    exec(
                    f'async def __ex(m): ' +
                        ''.join(f'\n {l}' for l in code.split('\n'))
                    )
                    await locals()['__ex'](msg)
                s = f.getvalue()
                if s:
                    await msg.reply(s or 'Done!', mention_author=False)
            except Exception as e:
                t = ''.join(traceback.format_exception(type(e), e, e.__traceback__))
                await msg.reply(f'```powershell\n{t}\n```', mention_author=False)
    elif m.content.startswith(f'{prefix}ui'):
        list_msg = list(map(str, m.content.split()))
        if len(list_msg) == 1:
            cur.execute('SELECT * FROM user_data;')
            talk_dic = {}
            slot_dic = {}
            slot = 0
            talk = 0
            boo = False
            for i in cur:
                if str(m.author.id) == i[0]:
                    boo = True
                    slot = int(i[1])
                    talk = int(i[2])
                talk_dic[int(i[0])] = int(i[2])
                slot_dic[int(i[0])] = int(i[1])
            talk_dic = sorted(talk_dic.items(), key=lambda x:x[1], reverse=True)
            slot_dic = sorted(slot_dic.items(), key=lambda x:x[1], reverse=True)
            talk_rank = []
            slot_rank = []
            for i in talk_dic:
                talk_rank.append(i[0])
            for i in slot_dic:
                slot_rank.append(i[0])
            if boo:
                await m.reply(embed=discord.Embed(title=f'{m.author.name}のデータ', description=f'～会話～\n回数：{talk}\n順位：{talk_rank.index(m.author.id) + 1}位\n\n～スロット～\n当選回数：{slot}\n順位：{slot_rank.index(m.author.id) + 1}位'), mention_author=False)
            else:
                await m.reply('your data is not find.', mention_author=False)
        elif len(list_msg) == 2:
            cur.execute('SELECT * FROM user_data;')
            talk_dic = {}
            slot_dic = {}
            slot = 0
            talk = 0
            boo = False
            for i in cur:
                if list_msg[1] == i[0]:
                    boo = True
                    slot = int(i[1])
                    talk = int(i[2])
                talk_dic[int(i[0])] = int(i[2])
                slot_dic[int(i[0])] = int(i[1])
            talk_dic = sorted(talk_dic.items(), key=lambda x:x[1], reverse=True)
            slot_dic = sorted(slot_dic.items(), key=lambda x:x[1], reverse=True)
            talk_rank = []
            slot_rank = []
            for i in talk_dic:
                talk_rank.append(i[0])
            for i in slot_dic:
                slot_rank.append(i[0])
            if boo:
                await m.reply(embed=discord.Embed(title=f'{client.get_user(int(list_msg[1])).name}のデータ', description=f'～会話～\n回数：{talk}\n順位：{talk_rank.index(int(list_msg[1])) + 1}位\n\n～スロット～\n当選回数：{slot}\n順位：{slot_rank.index(int(list_msg[1])) + 1}位'), mention_author=False)
            else:
                await m.reply('data is not find.', mention_author=False)
    elif m.content == f'{prefix}slot':
        list_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        a = random.choice(list_A)
        b = random.choice(list_A)
        c = random.choice(list_A)
        await m.reply(f'||{a}||||{b}||||{c}||', mention_author=False)
        if a == b and b == c:
            cur.execute('CREATE TABLE IF NOT EXISTS user_data (\
                        id text,\
                        slot text,\
                        talk text\
                        );\
                        COMMIT;\
                        SELECT * FROM user_data;')
            boo = False
            for i in cur:
                if i[0] == str(m.author.id):
                    boo = True
                    slot = int(i[1])
                    talk = int(i[2])
            if boo:
                slot += 1
                cur.execute(f'DELETE FROM user_data WHERE id = \'{m.author.id}\';\
                            INSERT INTO user_data VALUES (\'{m.author.id}\', \'{slot}\', \'{talk}\');\
                            COMMIT;')
            else:
                cur.execute(f'INSERT INTO user_data VALUES (\'{m.author.id}\', \'1\', \'0\');\
                            COMMIT;')
            await m.reply(f'当選しました！あなたの当選回数は合計で{slot}回です！', mention_author=False)
            cur.execute('SELECT * FROM user_data;')
            dic = {}
            for i in cur:
                dic[int(i[0])] = int(i[1])
            dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
            rank = []
            for i in dic:
                rank.append(i[0])
            await m.reply(f'{rank.index(m.author.id) + 1}位です。', mention_author=False)
    elif m.content == f'{prefix}now':
        now_2 = datetime.datetime.now()
        await m.reply(f'{now_2.year}年{now_2.month}月{now_2.day}日{now_2.hour + 9}時{now_2.minute}分{now_2.second}.{now_2.microsecond}秒', mention_author=False)
    elif m.content.startswith(f'{prefix}pin'):
        if m.guild != None:
            if m.author.guild_permissions.manage_messages:
                list_msg = list(map(str, m.content.split()))
                if len(list_msg) != 2:
                    await m.reply('y.pin [messagelink]で実行してください', mention_author=False)
                else:
                    link = list(map(str, list_msg[1].split('/')))
                    if len(link) != 7 or link[2] != 'discord.com':
                        await m.reply('正しいリンクを指定してください', mention_author=False)
                    else:
                        if link[4] == '@me':
                            channel = client.get_channel(int(link[5]))
                            if channel == None:
                                await m.reply('チャンネルが見つかりませんでした', mention_author=False)
                            else:
                                try:
                                    msg = await channel.fetch_message(int(link[6]))
                                except:
                                    await m.reply('存在しないメッセージです', mention_author=False)
                                else:
                                    try:
                                        await msg.pin()
                                    except:
                                        await m.reply('権限がありません', mention_author=False)
                                    else:
                                        await m.reply('ピン留めしました', mention_author=False)
                        else:
                            id = int(link[4])
                            guild = client.get_guild(id)
                            id = m.author.id
                            member = guild.get_member(id)
                            if guild != None:
                                if member.guild_permissions.manage_messages:
                                    channel = client.get_channel(int(link[5]))
                                    if channel == None:
                                        await m.reply('チャンネルが見つかりませんでした', mention_author=False)
                                    else:
                                        try:
                                            msg = await channel.fetch_message(int(link[6]))
                                        except:
                                            await m.reply('存在しないメッセージです', mention_author=False)
                                        else:
                                            try:
                                                await msg.pin()
                                            except:
                                                await m.reply('権限がありません', mention_author=False)
                                            else:
                                                await m.reply('ピン留めしました', mention_author=False)
                                else:
                                    await m.reply('あなたは権限がないため使用できません', mention_author=False)
                            else:
                                await m.reply('サーバーが見つかりませんでした', mention_author=False)
            else:
                await m.reply('あなたは権限がないため使用できません', mention_author=False)
        else:
            await m.reply('DMではできません', mention_author=False)
    elif m.content.startswith(f'{prefix}say'):
        list_msg = list(map(str, m.content.split()))
        if len(list_msg) != 2:
            await m.reply('y.say [description]の形で入力してください', mention_author=False)
        else:
            await m.channel.send(embed=discord.Embed(title=f'{m.author.name}のsay!', description=f'{list_msg[1]}'))
            try:
                await m.delete()
            except:
                return
    elif m.content == f'{prefix}invites':
        list_ = await m.guild.invites()
        s = ''
        for i in list_:
            s += f'{i.url}\n作成者{i.inviter}, 使用回数{i.uses}\n'
        try:
            await m.reply(embed=discord.Embed(title=f'{m.guild.name}の招待リンク一覧', description=s), mention_author=False)
        except:
            await m.reply('多すぎます！これもう管理に影響してるんじゃないんですか…？', mention_author=False)
    elif m.content.startswith(f'{prefix}rename'):
        member = m.guild.get_member(m.author.id)
        if m.guild == None:
            await m.reply('DMでは使用できません', mention_author=False)
        else:
            if member.guild_permissions.manage_nicknames:
                list_msg = list(map(str, m.content.split()))
                if len(list_msg) != 3:
                    await m.reply(f'{prefix}rename [targetid] [name]の形で実行してください。', mention_author=False)
                else:
                    try:
                        target = m.guild.get_member(int(list_msg[1]))
                    except:
                        await m.reply('invalid id', mention_author=False)
                    else:
                        try:
                            await target.edit(nick=list_msg[2])
                        except:
                            await m.reply('i dont have permission', mention_author=False)
                        else:
                            await m.reply('done', mention_author=False)
            else:
                await m.reply('あなたは権限を持っていません。', mention_author=False)
    elif m.content == f'{prefix}reimu':
        await m.reply('https://media.discordapp.net/attachments/873162873453576202/875918520985215076/67c21681.jpg', mention_author=False)
    elif m.content == f'{prefix}otofu':
        await m.reply('<:obutu:873608373923360829>', mention_author=False)
    elif m.content == f'{prefix}emoji':
        await m.reply(random.choice(client.emojis), mention_author=False)
    elif m.content == f'{prefix}art':
        await m.reply('```\n██████╗░░█████╗░  ███╗░░██╗░█████╗░████████╗  ███████╗██╗██████╗░███████╗  ████████╗░█████╗░\n██╔══██╗██╔══██╗  ████╗░██║██╔══██╗╚══██╔══╝  ██╔════╝██║██╔══██╗██╔════╝  ╚══██╔══╝██╔══██╗\n██║░░██║██║░░██║  ██╔██╗██║██║░░██║░░░██║░░░  █████╗░░██║██████╔╝█████╗░░  ░░░██║░░░██║░░██║\n██║░░██║██║░░██║  ██║╚████║██║░░██║░░░██║░░░  ██╔══╝░░██║██╔══██╗██╔══╝░░  ░░░██║░░░██║░░██║\n██████╔╝╚█████╔╝  ██║░╚███║╚█████╔╝░░░██║░░░  ██║░░░░░██║██║░░██║███████╗  ░░░██║░░░╚█████╔╝\n╚═════╝░░╚════╝░  ╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░\n\n███╗░░░███╗███████╗\n████╗░████║██╔════╝\n██╔████╔██║█████╗░░\n██║╚██╔╝██║██╔══╝░░\n██║░╚═╝░██║███████╗\n╚═╝░░░░░╚═╝╚══════╝\n```', mention_author=False)
    elif m.content == f'{prefix}omikuji':
        await m.reply(random.choice(['大吉', '中吉', '小吉', '末吉', '吉', '凶']), mention_author=False)
    elif m.channel.id == 876355240625057822:
        try:
            await m.author.edit(nick=m.content)
        except discord.Forbidden:
            await m.reply('権限がありません。ロールの位置などを確認してください。', mention_author=False)
        except discord.HTTPException:
            await m.reply('長すぎます。（多分）', mention_author=False)
    elif m.content.startswith(f'{prefix}remind'):
        list_msg = list(map(str, m.content.split()))
        if len(list_msg) == 2:
            if list_msg[1][-1] == 'h':
                list_msg[1] = list_msg[1].replace('h', '')
                try:
                    list_msg[1] = int(list_msg[1])
                except:
                    await m.reply('単位の前は半角数字にしてください。', mention_author=False)
                else:
                    await m.reply(f'{list_msg[1]}時間後に{m.channel.name}でお知らせします。', mention_author=False)
                    await asyncio.sleep(list_msg[1] * 3600)
                    await m.reply(f'<@{m.author.id}>お時間です！', mention_author=False)
            elif list_msg[1][-1] == 'm':
                list_msg[1] = list_msg[1].replace('m', '')
                try:
                    list_msg[1] = int(list_msg[1])
                except:
                    await m.reply('単位の前は半角数字にしてください。', mention_author=False)
                else:
                    await m.reply(f'{list_msg[1]}分後に{m.channel.name}でお知らせします。', mention_author=False)
                    await asyncio.sleep(list_msg[1] * 60)
                    await m.reply(f'<@{m.author.id}>お時間です！', mention_author=False)
            elif list_msg[1][-1] == 's':
                list_msg[1] = list_msg[1].replace('s', '')
                try:
                    list_msg[1] = int(list_msg[1])
                except:
                    await m.reply('単位の前は半角数字にしてください。', mention_author=False)
                else:
                    await m.reply(f'{list_msg[1]}秒後に{m.channel.name}でお知らせします。', mention_author=False)
                    await asyncio.sleep(list_msg[1])
                    await m.reply(f'<@{m.author.id}>お時間です！', mention_author=False)
            else:
                await m.reply(f'{prefix}remind [time]で入力してください。\ntimeには次の単位が使えます\nh:時間, m:分, s:秒\nまた、BOTが再起動すると途切れますがご了承ください。', mention_author=False)
        else:
            await m.reply(f'{prefix}remind [time]で入力してください。\ntimeには次の単位が使えます\nh:時間, m:分, s:秒\nまた、BOTが再起動すると途切れますがご了承ください。', mention_author=False)
    elif m.content == f'{prefix}help':
        await m.reply(embed=discord.Embed(title='help', description=f'～BOT系コマンド～\n・{prefix}help\n・{prefix}ui\n～遊び系コマンド～\n・{prefix}slot\n・{prefix}say [description]\n・{prefix}reimu\n・{prefix}otofu\n・{prefix}emoji\n・{prefix}art\n・{prefix}omikuji\n～便利系コマンド～\n・{prefix}now\n・{prefix}pin [messagelink]\n・{prefix}invites\n・{prefix}rename [targetid] [name]\n・{prefix}remind [time]\n～スラッシュコマンド～\n/avatar [user]\n～（めっちゃ）特殊コマンド～\nユーザー系：\nHow to use:ユーザーを右クリックしたアプリという項目の中にあります。（PC限定）\navatar\n～特殊コマンド～\n・{prefix}eval'), mention_author=False)
    else:
        cur.execute('CREATE TABLE IF NOT EXISTS user_data (\
                    id text,\
                    slot text,\
                    talk text\
                    );\
                    COMMIT;\
                    SELECT * FROM user_data;')
        boo = False
        for i in cur:
            if i[0] == str(m.author.id):
                boo = True
                slot = int(i[1])
                talk = int(i[2])
        if boo:
            talk += 1
            cur.execute(f'DELETE FROM user_data WHERE id = \'{m.author.id}\';\
                        INSERT INTO user_data VALUES ( \'{m.author.id}\', \'{slot}\', \'{talk}\' );\
                        COMMIT;')
        else:
            cur.execute(f'INSERT INTO user_data VALUES ( \'{m.author.id}\', \'0\', \'1\' );\
                        COMMIT;')
async def on_member_join(member):
    if member.guild.id == server_id:
        await member.send(embed=discord.Embed(title='公式鯖にようこそ！', description=welcome))
client.run(TOKEN)
