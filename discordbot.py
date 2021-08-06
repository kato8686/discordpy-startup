# -*- coding: utf-8 -*-

import discord
import os
intents = discord.Intents.all()
client = discord.Client(intents=intents)
TOKEN = os.environ['DISCORD_BOT_TOKEN']
@client.event
async def on_message(m):
    def check(me):
        return me.author == m.author and me.channel == m.channel
    if m.author.bot:
        return
    elif m.content == 'y.api':
        embed = discord.Embed(title='APIリファレンス', description='バージョン関連情報\n1:discord.version_info\n2:discord.`___version__`\nClients\n3:discord.Client\n4:discord.AutoShardedClient\nApplication Info\n5:discord.AppInfo')
        message = await m.channel.send(content='1~5で数字を指定してください。\nendで受付を終了します。', embed=embed)
        msg = await client.wait_for('message', check=check)
        if msg.content == '1':
            embed = discord.Embed(title='discord.version_info', description='sys.version_info に似た名前付きタプル。\nsys.version_info と同じように releaselevel の有効値は \'alpha\'、\'beta\'、\'candidate\'、そして \'final\' です。')
            await message.edit(embed=embed)
        elif msg.content == '2':
            embed = discord.Embed(title='discord.`__version__`', description='\'1.0.0rc1\' のようなバージョンの文字列表現。これは PEP 440 に基づいています。')
            await message.edit(embed=embed)
        elif msg.content == '3':
            embed = discord.Embed(title='discord.Client[1]', description='Discordに接続するクライアント接続を表します。このクラスは、DiscordのWebSocket、及びAPIとの対話に使用されます。\n多くのオプションを Client に渡すことが可能です。\n\n1:discord.Client.オプション\n2:discord.Client.activity\n3:discord.Client.allowed_mentions\n4:discord.Client.application_id\n5:discord.Client.cached_messages\n6:discord.Client.emojis\n7:discord.Client.guilds\n8:discord.Client.intents\n9:discord.Client.latency\n10:discord.Client.loop')
            await message.edit(content='1~10で数字を指定してください。\nnextで次のページ、endで受付を終了します。', embed=embed)
            page = 1
            def check(me):
                return me.author == m.author and me.channel == m.channel
            for i in range(10):
                msg = await client.wait_for('message', check=check)
                if msg.content == '1':
                    if page == 1:
                        embed = discord.Embed(title='discord.Client', description='・max_messages (Optional[int]) --\n　The maximum number of messages to store in the internal message cache. This defaults to 1000. Passing in None disables the message cache.\n　バージョン 1.3 で変更: Allow disabling the message cache and change the default size to 1000.\n・loop (Optional[asyncio.AbstractEventLoop]) -- 非同期操作に使用する asyncio.AbstractEventLoop 。デフォルトは None です。この場合、デフォルトのイベントループは asyncio.get_event_loop() を介して使用されます。\n・connector (Optional[aiohttp.BaseConnector]) -- コネクションプーリングに使用するコネクタ。\n・proxy (Optional[str]) -- プロキシのURL。\n・proxy_auth (Optional[aiohttp.BasicAuth]) -- プロキシのHTTP Basic認証を表すオブジェクト。\n・shard_id (Optional[int]) -- Integer starting at 0 and less than shard_count.\nshard_count (Optional[int]) -- Shardの総数。\n・application_id (int) -- The client\'s application ID.\n・intents (Intents) --\n　The intents that you want to enable for the session. This is a way of disabling and enabling certain gateway events from triggering and being sent. If not given, defaults to a regularly constructed Intents class.\n　バージョン 1.5 で追加.\n・member_cache_flags (MemberCacheFlags) --\n　Allows for finer control over how the library caches members. If not given, defaults to cache as much as possible with the currently selected intents.\n　バージョン 1.5 で追加.\n・chunk_guilds_at_startup (bool) --\n　Indicates if on_ready() should be delayed to chunk all guilds at start-up if necessary. This operation is incredibly slow for large amounts of guilds. The default is True if Intents.members is True.\n　バージョン 1.5 で追加.\n・status (Optional[Status]) -- Discordにログインした際の、開始時ステータス。\n・activity (Optional[BaseActivity]) -- Discordにログインした際の、開始時アクティビティ。\n・allowed_mentions (Optional[AllowedMentions]) --\n　Control how the client handles mentions by default on every message sent.\n　バージョン 1.4 で追加.\n・heartbeat_timeout (float) -- HEARTBEAT_ACKを受信できない際に、WebSocketをタイムアウトさせて再起動するまでの最大秒数。最初のパケットの処理に時間がかかり、接続を切断できないというような状況時に便利です。デフォルトでは60秒に設定されています。\n・guild_ready_timeout (float) --\n　The maximum number of seconds to wait for the GUILD_CREATE stream to end before preparing the member cache and firing READY. The default timeout is 2 seconds.\n　バージョン 1.4 で追加.\n・assume_unsync_clock (bool) --\n　Whether to assume the system clock is unsynced. This applies to the ratelimit handling code. If this is set to True, the default, then the library uses the time to reset a rate limit bucket given by Discord. If this is False then your system clock is used to calculate how long to sleep for. If this is set to False it is recommended to sync your system clock to Google\'s NTP server.\n　バージョン 1.3 で追加.')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '2':
                    if page == 1:
                        embed = discord.Embed(title='discord.Client.activity', description='The activity being used upon logging in.\n\nType:Optional[BaseActivity]')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '3':
                    if page == 1:
                        embed = discord.Embed(title='discord.Client.allowed_mentions', description='The allowed mention configuration.\nバージョン 1.4 で追加.\n\nType:Optional[AllowedMentions]')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '4':
                    if page == 1:
                        embed = discord.Embed(title='discord.Client.application_id', description='The client\'s application ID.\nIf this is not passed via `__init__` then this is retrieved through the gateway when an event contains the data. Usually after on_connect() is called.\n\nType:Optional[int]')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '5':
                    if page == 1:
                        embed = discord.Embed(title='discord.Client.cached_messages', description='Read-only list of messages the connected client has cached.\nバージョン 1.1 で追加.\n\nType:Sequence[Message]')
                        await message.edit(embed=embed)
                        break
                elif msg.content  == '6':
                    if page == 1:
                        embed = discord.Embed(title='discord.Client.emojis', description='The emojis that the connected client has.\n\nType:List[Emoji]')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '7':
                    if page == 1:
                        embed = discord.Embed(title='discord.Client.guilds', description='The guilds that the connected client is a member of.\n\nType:List[Guild]')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '8':
                    if page == 1:
                        embed = discord.Embed(title='discord.Client.intents', description='The intents configured for this connection.\nバージョン 1.5 で追加.\n\nType:Intents')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '9':
                    if page == 1:
                        embed = discord.Embed(title='discord.Client.latency', description='Measures latency between a HEARTBEAT and a HEARTBEAT_ACK in seconds.\nこれはDiscord WebSocketプロトコルの待ち時間とも言えます。\n\nType:float')
                        await message.edit(embed=embed)
                        break
                elif msg.content =='10':
                    if page == 1:
                        embed = discord.Embed(title='discord.Client.loop', description='The event loop that the client uses for asynchronous operations.\n\nType:asyncio.AbstractEventLoop')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '11':
                    if page == 2:
                        embed= discord.Embed(title='discord.Client.persistent_views', description='A sequence of persistent views added to the client.\n\nType:Sequence[View]')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '12':
                    if page == 2:
                        embed = discord.Embed(title='discord.Client.private_channels', description='The private channels that the connected client is participating on.\n\n注釈\nDiscordでのプライベートチャンネルの取扱いは内部的に処理されているため、これは最新のプライベートチャンネルから最大128個までしか取得できません。\n\nType:List[abc.PrivateChannel]')
                        await message.edit(embed=embed)
                        break
                elif msg.content== '13':
                    if page == 2:
                        embed = discord.Embed(title='discord.Client.stickers', description='The stickers that the connected client has.\nバージョン 2.0 で追加.\n\nType:List[GuildSticker]')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '14':
                    if page == 2:
                        embed = discord.Embed(title='discord.Client.user', description='Represents the connected client. None if not logged in.\n\nType:Optional[ClientUser]')
                        await message.edit(embed=embed)
                        break
                elif msg.content== '15':
                    if page == 2:
                        embed= discord.Embed(title='discord.Client.users', description='Returns a list of all the users the bot can see.\n\nType:List[User]')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '16':
                    if page == 2:
                        embed= discord.Embed(title='discord.Client.voice_clients', description='Represents a list of voice connections.\nThese are usually VoiceClient instances.\n\nType:List[VoiceProtocol]')
                        await message.edit(embed=embed)
                        break
                elif msg.content  == '17':
                    if page == 2:
                        embed = discord.Embed(title='discord.Client.ws', description='クライアントが現在接続しているWebSocketゲートウェイ。 None でもかまいません。')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '18':
                    if page == 2:
                        embed = discord.Embed(title='discord.Client.add_view', description='Registers a View for persistent listening.\nThis method should be used for when a view is comprised of components that last longer than the lifecycle of the program.\n\nパラメータ\n・view (discord.ui.View) -- The view to register for dispatching.\n・message_id (Optional[int]) -- The message ID that the view is attached to. This is currently used to refresh the view\'s state during message update events. If not given then message update events are not propagated for the view.\n\n例外\n・TypeError -- A view was not passed.\n・ValueError -- The view is not persistent. A persistent view has no timeout and all their components have an explicitly provided custom_id.')
                        await message.edit(embed=embed)
                        break
                elif msg.content== '19':
                    if page == 2:
                        embed = discord.Embed(title='discord.Client.application_info', description='This function is a coroutine.\nBotのアプリケーション情報を取得します。\n\n例外\nHTTPException -- Retrieving the information failed somehow.\n\n戻り値\nBotのアプリケーション情報。\n\n戻り値の型\nAppInfo')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '20':
                    if page == 2:
                        embed = discord.Embed(title='discord.Client.before_identify_hook', description='This function is a coroutine.\nA hook that is called before IDENTIFYing a session. This is useful if you wish to have more control over the synchronization of multiple IDENTIFYing clients.\nThe default implementation sleeps for 5 seconds.\nバージョン 1.4 で追加.\n\nパラメータ\n・shard_id (int) -- The shard ID that requested being IDENTIFY\'d\n・initial (bool) -- Whether this IDENTIFY is the first initial IDENTIFY.')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '21':
                    if page == 3:
                        embed = discord.Embed(title='discord.Client.change_presence', description='This function is a coroutine.\nクライアントのプレゼンスを変更します。\nバージョン 2.0 で変更: Removed the afk keyword-only parameter.\n\nサンプル\n```python\ngame = discord.Game("with the API")\nawait client.change_presence(status=discord.Status.idle, activity=game)\n```\n\nパラメータ\n・activity (Optional[BaseActivity]) -- 実行中のアクティビティ。何も実行していない場合は None です。\n・status (Optional[Status]) -- 変更するステータスを示します。 None の場合、:attr:‘.Status.online‘となります。\n\n例外\nInvalidArgument -- If the activity parameter is not the proper type.')
                        await message.edit(embed=embed)
                        break
                elif msg.content  == '22':
                    if page == 3:
                        embed = discord.Embed(title='discord.Client.clear', description='Botの内部状態をクリアします。\nこれが実行されると、Botは「再オープン」されたとみなされます。そのため、 is_closed() や is_ready() は False を返し、内部のキャッシュもクリアされます。')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '23':
                    if page == 3:
                        embed = discord.Embed(title='discord.Client.close', description='This function is a coroutine.\nDiscordとの接続を閉じます。')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '24':
                    if page == 3:
                        embed = discord.Embed(title='discord.Client.connect', description='This function is a coroutine.\nWebSocket接続を作成し、Discordからのメッセージをリッスンできるようにします。これはイベントシステム全体とライブラリの様々な機能を実行するループです。WebSocket接続が終了するまで、制御は再開されません。\n\nパラメータ\nreconnect (bool) -- インターネットの障害やDiscord側の特定の障害が発生した際に再接続を試みるかどうかを表します。不正な状態へつながることによる特定の切断（無効なシャーディングペイロードや不正なトークンなど）は処理されません。\n\n例外\n・GatewayNotFound -- If the gateway to connect to Discord is not found. Usually if this is thrown then there is a Discord API outage.\n・ConnectionClosed -- The websocket connection has been terminated.')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '25':
                    if page == 3:
                        embed = discord.Embed(title='discord.Client.create_dm', description='This function is a coroutine.\nCreates a DMChannel with this user.\nThis should be rarely called, as this is done transparently for most people.\nバージョン 2.0 で追加.\n\nパラメータ\nuser (Snowflake) -- The user to create a DM with.\n\n戻り値\nThe channel that was created.\n\n戻り値の型\nDMChannel')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '26':
                    if page == 3:
                        embed= discord.Embed(title='discord.Client.create_guild', description='This function is a coroutine.\nGuild を作成します。\n10以上のギルドに参加しているBotアカウントはギルドの作成ができません。\n\nパラメータ\n・name (str) -- ギルドの名前。\n・region (VoiceRegion) -- ボイスチャンネルの通信サーバーのリージョンです。デフォルトは VoiceRegion.us_west です。\n・icon (Optional[bytes]) -- アイコンを表す bytes-like object です。 ClientUser.edit() で、予期されるデータの詳細を確認してください。\n・code (str) --\nThe code for a template to create the guild with.\nバージョン 1.4 で追加.\n\n例外\n・HTTPException -- Guild creation failed.\n・InvalidArgument -- Invalid icon image format given. Must be PNG or JPG.\n\n戻り値\n作成されたギルド。キャッシュに追加されるギルドとは別物です。\n\n戻り値の型\nGuild')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '27':
                    if page == 3:
                        embed = discord.Embed(title='discord.Client.delete_invite', description='This function is a coroutine.\nInvite や、招待のURL、IDを削除します。\nこれを行うには、関連付けられたGuildにて、 manage_channels 権限が必要です。\n\nパラメータ\ninvite (Union[Invite, str]) -- 取り消す招待。\n\n例外\n・Forbidden -- You do not have permissions to revoke invites.\n・NotFound -- The invite is invalid or expired.\n・HTTPException -- Revoking the invite failed.')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '28':
                    if page == 3:
                        embed = discord.Embed(title='discord.Client.event', description='リッスンするイベントを登録するデコレータ。\nイベントの詳細については 以下のドキュメント を参照してください。\nイベントは コルーチン でなければいけません。違う場合は TypeError が発生します。\n\nサンプル\n```python\n@client.event\nasync def on_ready():\n    print(\'Ready!\')\n```\n\n例外\nTypeError -- The coroutine passed is not actually a coroutine.')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '29':
                    if page == 3:
                        embed = discord.Embed(title='discord.Client.fetch_channel', description='This function is a coroutine.\nRetrieves a abc.GuildChannel, abc.PrivateChannel, or Thread with the specified ID.\nバージョン 1.2 で追加.\n\n注釈\nこのメソッドはAPIを呼び出します。通常は get_channel() を代わりとして使用してください。\n\n例外\n・InvalidData -- An unknown channel type was received from Discord.\n・HTTPException -- Retrieving the channel failed.\n・NotFound -- Invalid Channel ID.\n・Forbidden -- You do not have permission to fetch this channel.\n\n戻り値\nIDから取得したチャンネル。\n\n戻り値の型\nUnion[abc.GuildChannel, abc.PrivateChannel, Thread]')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '30':
                    if page == 3:
                        embed = discord.Embed(title='discord.Client.fetch_guild', description='This function is a coroutine.\nIDから Guild を取得します。\n\n注釈\n・Using this, you will not receive Guild.channels, Guild.members, Member.activity and Member.voice per Member.\n・このメソッドはAPIを呼び出します。通常は get_guild() を代わりとして使用してください。\n\nパラメータ\nguild_id (int) -- 取得したいギルドのID。\n\n例外\n・Forbidden -- You do not have access to the guild.\n・HTTPException -- Getting the guild failed.\n\n戻り値\nIDから取得したギルド。\n\n戻り値の型\nGuild')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '31':
                    if page == 4:
                        embed = discord.Embed(title='discord.Client.fetch_invite', description='This function is a coroutine.\nInvite をdiscord.gg URLやIDから取得します。\n\n注釈\nIf the invite is for a guild you have not joined, the guild and channel attributes of the returned Invite will be PartialInviteGuild and PartialInviteChannel respectively.\n\nパラメータ\n・url (Union[Invite, str]) -- Discordの招待ID、またはURL（discord.gg URLである必要があります）。\n・with_counts (bool) -- 招待にカウントの情報を含めるかどうか。これにより Invite.approximate_member_count と Invite.approximate_presence_count が追加されます。\n・with_expiration (bool) --\nWhether to include the expiration date of the invite. This fills the Invite.expires_at field.\nバージョン 2.0 で追加.\n\n例外\n・NotFound -- The invite has expired or is invalid.\n・HTTPException -- Getting the invite failed.\n\n戻り値\nURL/IDから取得した招待。\n\n戻り値の型\nInvite')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '32':
                    if page == 4:
                        embed = discord.Embed(title='discord.Client.fetch_premium_sticker_packs', description='This function is a coroutine.\nRetrieves all available premium sticker packs.\nバージョン 2.0 で追加.\n\n例外\nHTTPException -- Retrieving the sticker packs failed.\n\n戻り値\nAll available premium sticker packs.\n\n戻り値の型\nList[StickerPack]')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '33':
                    if page == 4:
                        embed = discord.Embed(title='discord.Client.fetch_stage_instance', description='This function is a coroutine.\nGets a StageInstance for a stage channel id.\nバージョン 2.0 で追加.\n\nパラメータ\nchannel_id (int) -- The stage channel ID.\n\n例外\n・NotFound -- The stage instance or channel could not be found.\n・HTTPException -- Getting the stage instance failed.\n\n戻り値\nThe stage instance from the stage channel ID.\n\n戻り値の型\nStageInstance')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '34':
                    if page == 4:
                        embed = discord.Embed(title='discord.Client.fetch_sticker', description='This function is a coroutine.\nRetrieves a Sticker with the specified ID.\nバージョン 2.0 で追加.\n\n例外\n・HTTPException -- Retrieving the sticker failed.\n・NotFound -- Invalid sticker ID.\n\n戻り値\nThe sticker you requested.\n\n戻り値の型\nUnion[StandardSticker, GuildSticker]')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '35':
                    if page == 4:
                        embed = discord.Embed(title='discord.Client.fetch_template', description='This function is a coroutine.\nGets a Template from a discord.new URL or code.\n\nパラメータ\ncode (Union[Template, str]) -- The Discord Template Code or URL (must be a discord.new URL).\n\n例外\n・NotFound -- The template is invalid.\n・HTTPException -- Getting the template failed.\n\n戻り値\nThe template from the URL/code.\n\n戻り値の型\nTemplate')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '36':
                    if page == 4:
                        embed = discord.Embed(title='discord.Client.fetch_user', description='This function is a coroutine.\nRetrieves a User based on their ID. You do not have to share any guilds with the user to get this information, however many operations do require that you do.\n\n注釈\nThis method is an API call. If you have discord.Intents.members and member cache enabled, consider get_user() instead.\n\nパラメータ\nuser_id (int) -- 取得したいユーザーのID。\n\n例外\n・NotFound -- A user with this ID does not exist.\n・HTTPException -- Fetching the user failed.\n\n戻り値\nあなたがリクエストしたユーザー。\n\n戻り値の型\nUser')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '37':
                    if page == 4:
                        embed = discord.Embed(title='discord.Client.fetch_webhook', description='This function is a coroutine.\n特定のIDの Webhook を取得します。\n\n例外\n・HTTPException -- Retrieving the webhook failed.\n・NotFound -- Invalid webhook ID.\nForbidden -- You do not have permission to fetch this webhook.\n\n戻り値\n要求したWebhook。\n\n戻り値の型\nWebhook')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '38':
                    if page == 4:
                        embed = discord.Embed(title='discord.Client.fetch_widget', description='This function is a coroutine.\nギルドIDから Widget を取得します。\n\n注釈\nこの情報を取得するためには、ギルドのウィジェットを有効化しておく必要があります。\n\nパラメータ\nguild_id (int) -- ギルドのID。\n\n例外\n・Forbidden -- The widget for this guild is disabled.\n・HTTPException -- Retrieving the widget failed.\n\n戻り値\nギルドのウィジェット。\n\n戻り値の型\nWidget')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '39':
                    if page == 4:
                        embed = discord.Embed(title='discord.Client.get_all_channels', description='クライアントが「アクセス」できるすべての abc.GuildChannel のジェネレータを取得します。\n使用例:\n```python\nfor guild in client.guilds:\n    for channel in guild.channels:\n        yield channel\n```\n\n注釈\nabc.GuildChannel を受け取ったからと言って、そのチャンネルで発言ができるという意味ではありません。発言可能なチャンネルのみを取得したいのなら、 abc.GuildChannel.permissions_for() を使いましょう。\n\n列挙\nabc.GuildChannel -- A channel the client can \'access\'.')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '40':
                    if page == 4:
                        embed = discord.Embed(title='discord.Client.get_all_members', description='クライアントが参照可能なすべての Member のジェネレータを返します。\n使用例:\m```python\nfor guild in client.guilds:\n    for member in guild.members:\n        yield member\n```\n\n列挙\nMember -- A member the client can see.')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '41':
                    if page == 5:
                        embed = discord.Embed(title='discord.Client.get_channel', description='Returns a channel with the given ID.\n\nパラメータ\nid (int) -- The ID to search for.\n\n戻り値\nThe returned channel or None if not found.\n\n戻り値の型\nOptional[Union[abc.GuildChannel, abc.PrivateChannel]]')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '42':
                    if page == 5:
                        embed = discord.Embed(title='discord.Client.get_emoji', description='Returns an emoji with the given ID.\n\nパラメータ\nid (int) -- The ID to search for.\n\n戻り値\nThe custom emoji or None if not found.\n\n戻り値の型\nOptional[Emoji]')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '43':
                    if page == 5:
                        embed = discord.Embed(title='discord.Client.get_guild', description='Returns a guild with the given ID.\n\nパラメータ\nid (int) -- The ID to search for.\n\n戻り値\nThe guild or None if not found.\n\n戻り値の型\nOptional[Guild]')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '44':
                    if page == 5:
                        embed = discord.Embed(title='discord.Client.get_stage_instance', description='Returns a stage instance with the given stage channel ID.\nバージョン 2.0 で追加.\n\nパラメータ\nid (int) -- The ID to search for.\n\n戻り値\nThe returns stage instance of None if not found.\n\n戻り値の型\nOptional[StageInstance]')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '45':
                    if page == 5:
                        embed = discord.Embed(title='discord.Client.get_sticker', description='Returns a guild sticker with the given ID.\nバージョン 2.0 で追加.\n\n注釈\nTo retrieve standard stickers, use fetch_sticker(). or fetch_premium_sticker_packs().\n\n戻り値\nThe sticker or None if not found.\n\n戻り値の型\nOptional[GuildSticker]')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '46':
                    if page == 5:
                        embed=discord.Embed(title='discord.Client.get_user', description='Returns a user with the given ID.\n\nパラメータ\nid (int) -- The ID to search for.\n\n戻り値\nThe user or None if not found.\n\n戻り値の型\nOptional[User]')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '47':
                    if page == 5:
                        embed = discord.Embed(title='discord.Client.is_closed', description='bool: Indicates if the websocket connection is closed.')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '48':
                    if page == 5:
                        embed = discord.Embed(title='discord.Client.is_ready', description='bool: Specifies if the client\'s internal cache is ready for use.')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '49':
                    if page == 5:
                        embed = discord.Embed(title='discord.Client.is_ws_ratelimited', description='bool: Whether the websocket is currently rate limited.\nThis can be useful to know when deciding whether you should query members using HTTP or via the gateway.\nバージョン 1.6 で追加.')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '50':
                    if page == 5:
                        embed = discord.Embed(title='discord.Client.login', description='This function is a coroutine.\n指定された資格情報を使用してクライアントにログインします。\n\nパラメータ\ntoken (str) -- 認証用のトークン。このライブラリが処理するため、トークンの頭に何も付けないでください。\n\n例外\n・LoginFailure -- The wrong credentials are passed.\n・HTTPException -- An unknown HTTP related error occurred, usually when it isn\'t 200 or the known incorrect credentials passing status code.')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '51':
                    if page == 6:
                        embed = discord.Embed(title='discord.Client.on_error', description='This function is a coroutine.\nクライアントによって提供されるデフォルトのエラーハンドラ。\nデフォルトでは、これは sys.stderr に出力されますが、異なる実装によって上書きされる可能性があります。詳細については on_error() を確認してください。')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '52':
                    if page == 6:
                        embed = discord.Embed(title='discord.Client.run', description='イベントループの初期化を抽象化するブロッキングコール。\nイベントループをより詳細に制御するには、この関数を使用しないでください。 start() または connect() + login() を使用してください。\nおおよそ次のものに相当：\n```python\ntry:\n    loop.run_until_complete(start(*args, **kwargs))\nexcept KeyboardInterrupt:\n    loop.run_until_complete(close())\n    # cancel all tasks lingering\nfinally:\n    loop.close()\n```\n\n警告\nこの関数はブロッキングを行うため、必ず最後に呼び出してください。この関数を呼び出した後に呼び出されるイベントや関数は、Botが停止するまで実行されません。')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '53':
                    if page == 6:
                        embed = discord.Embed(title='discord.Client.start', description='This function is a coroutine.\nlogin() + connect() を簡略化したコルーチン。\n\n例外\nTypeError -- An unexpected keyword argument was received.')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '54':
                    if page == 6:
                        embed = discord.Embed(title='discord.Client.wait_for', description='This function is a coroutine.\nWebSocketイベントがディスパッチされるまで待機します。\nメッセージの送信者が、メッセージに返信したり、リアクションをつけたり、編集したりする、自己完結型の処理に利用できます。\ntimeout パラメータは asyncio.wait_for() に渡されます。デフォルトではタイムアウトしません。タイムアウトした際に asyncio.TimeoutError が発生するのは、使いやすさを考慮したためです。\nイベントが複数の引数を返す場合は、それらを含む tuple が代わりに返ります。イベントとそのパラメーターについては ドキュメント を参照してください。\nこの関数は 条件を満たす最初のイベント を返します。\n\nサンプル\nユーザーからの返信を待つ場合:\n```python\n@client.event\nasync def on_message(message):\n    if message.content.startswith(\'$greet\'):\n        channel = message.channel\n        await channel.send(\'Say hello!\')\n\n        def check(m):\n            return m.content == \'hello\' and m.channel == channel\n\n        msg = await client.wait_for(\'message\', check=check)\n        await channel.send(f\'Hello {msg.author}!\')\n```\nメッセージ送信者がサムズアップリアクションを付けるのを待つ場合:\n```python\n@client.event\nasync def on_message(message):\n    if message.content.startswith(\'$thumb\'):\n        channel = message.channel\n        await channel.send(\'Send me that 👍 reaction, mate\')\n\n        def check(reaction, user):\n            return user == message.author and str(reaction.emoji) == \'👍\'\n\n        try:\n            reaction, user = await client.wait_for(\'reaction_add\', timeout=60.0, check=check)\n        except asyncio.TimeoutError:\n            await channel.send(\'👎\')\n        else:\n            await channel.send(\'👍\')\n```\n\nパラメータ\n・event (str) -- イベント名は イベントリファレンス に似ていますが接頭詞の on_ が必要ありません。\n・check (Optional[Callable[..., bool]]) -- 待っているものに該当するかを確認する関数。引数は待機しているイベントのパラメータを満たしている必要があります。\n・timeout (Optional[float]) -- タイムアウトして asyncio.TimeoutError が発生するまでの秒数。\n\n例外\nasyncio.TimeoutError -- If a timeout is provided and it was reached.\n\n戻り値\n単一の引数、あるいは イベントリファレンス のパラメータを反映した複数の引数の値を含む tuple が返ります。返る引数がない場合もあります。\n\n戻り値の型\nAny')
                        await message.edit(embed=embed)
                        break
                elif msg.content == '55':
                    if page == 6:
                        embed = discord.Embed(title='discord.Client.wait_until_ready', description='This function is a coroutine.\nクライアントの内部キャッシュの準備が完了するまで待機します。')
                        await message.edit(embed=embed)
                        break
                elif msg.content == 'next':
                    if page == 1:
                        embed = discord.Embed(title='discord.Client[2]', description='11:discord.Client.persistent_views\n12:discord.Client.private_channels\n13:discord.Client.stickers\n14:discord.Client.user\n15:discord.Client.users\n16:discord.Client.voice_clients\n17:discord.Client.ws\n18:discord.Client.add_view\n19:discord.Client.application_info\n20:discord.Client.before_identify_hook')
                        await message.edit(content='11~20の数字で項目の右の数字を指定してください。\nnextで次のページ、backで前のページ、endで受付を終了します。', embed=embed)
                        page  = 2
                    elif page == 2:
                        embed = discord.Embed(title='discord.Client[3]', description='21:discord.Client.change_presence\n22:discord.Client.clear\n23:discord.Client.close\n24:discord.Client.connect\n25:discord.Client.create_dm\n26:discord.Client.create_guild\n27:discord.Client.delete_invite\n28:discord.Client.event\n29:discord.Client.fetch_channel\n30:discord.Client.fetch_guild')
                        await message.edit(content='21~30の数字で項目の右の数字を指定してください。\nnextで次のページ、backで前のページ、endで受付を終了します。', embed=embed)
                        page = 3
                    elif page == 3:
                        embed = discord.Embed(title='discord.Client[4]', description='31:discord.Client.fetch_invite\n32:discord.Client.fetch_premium_sticker_packs\n33:discord.Client.fetch_stage_instance\n34:discord.Client.fetch_sticker\n35:discord.Client.fetch_template\n36:discord.Client.fetch_user\n37:discord.Client.fetch_webhook\n38:discord.Client.fetch_widget\n39:discord.Client.get_all_channels\n40:discord.Client.get_all_members')
                        await message.edit(content='31~40の数字で項目の右の数字を指定してください。\nnextで次のページ、backで前のページ、endで受付を終了します。', embed=embed)
                        page = 4
                    elif page == 4:
                        embed = discord.Embed(title='discord.Client[5]', description='41:discord.Client.get_channel\n42:discord.Client.get_emoji\n43:discord.Client.get_guild\n44:discord.Client.get_stage_instance\n45:discord.Client.get_sticker\n46:discord.Client.get_user\n47:discord.Client.is_closed\n48:discord.Client.is_ready\n49:discord.Client.is_ws_ratelimited\n50:discord.Client.login')
                        await message.edit(content='41~50の数字で項目の右の数字を指定してください。\nnextで次のページ、backで前のページ、endで受付を終了します。', embed=embed)
                        page = 5
                    elif page == 5:
                        embed = discord.Embed(title='discord.Client[6]', description='51:discord.Client.on_error\n52:discord.Client.run\n53:discord.Client.start\n54:discord.Client.wait_for\n55:discord.Client.wait_until_ready')
                        await message.edit(content='51~55の数字で項目の右の数字を指定してください。\nbackで前のページ、endで受付を終了します。', embed=embed)
                        page = 6
                elif msg.content == 'back':
                    if page == 2:
                        embed = discord.Embed(title='discord.Client[1]', description='Discordに接続するクライアント接続を表します。このクラスは、DiscordのWebSocket、及びAPIとの対話に使用されます。\n多くのオプションを Client に渡すことが可能です。\n1:オプション\n2:activity\n3:allowed_mentions\n4:application_id\n5:cached_messages\n6:emojis\n7:guilds\n8:intents\n9:latency\n10:loop')
                        await message.edit(content='1~10で数字を指定してください。\nnextで次のページ、endで受付を終了します。', embed=embed)
                        page = 1
                    elif page == 3:
                        embed = discord.Embed(title='discord.Client[2]', description='11:persistent_views\n12:private_channels\n13:stickers\n14:user\n15:users\n16:voice_clients\n17:ws\n18:add_view\n19:application_info\n20:before_identify_hook')
                        await message.edit(content='11~20の数字で項目の右の数字を指定してください。\nnextで次のページ、backで前のページ、endで受付を終了します。', embed=embed)
                        page  = 2
                    elif page == 4:
                        embed = discord.Embed(title='discord.Client[3]', description='21:change_presence\n22:clear\n23:close\n24:connect\n25:create_dm\n26:create_guild\n27:delete_invite\n28:event\n29:fetch_channel\n30:fetch_guild')
                        await message.edit(content='21~30の数字で項目の右の数字を指定してください。\nnextで次のページ、backで前のページ、endで受付を終了します。', embed=embed)
                        page = 3
                    elif page == 5:
                        embed = discord.Embed(title='discord.Client[4]', description='31:fetch_invite\n32:fetch_premium_sticker_packs\n33:fetch_stage_instance\n34:fetch_sticker\n35:fetch_template\n36:fetch_user\n37:fetch_webhook\n38:fetch_widget\n39:get_all_channels\n40:get_all_members')
                        await message.edit(content='31~40の数字で項目の右の数字を指定してください。\nnextで次のページ、backで前のページ、endで受付を終了します。', embed=embed)
                        page = 4
                    elif page == 6:
                        embed = discord.Embed(title='discord.Client[5]', description='41:get_channel\n42:get_emoji\n43:get_guild\n44:get_stage_instance\n45:get_sticker\n46:get_user\n47:is_closed\n48:is_ready\n49:is_ws_ratelimited\n50:login')
                        await message.edit(content='41~50の数字で項目の右の数字を指定してください。\nnextで次のページ、backで前のページ、endで受付を終了します。', embed=embed)
                        page = 5
                elif msg.content == 'end':
                    await message.edit(content='ended')
                    break
                else:
                    await msg.channel.send('!?!?!invalid index!?!?!')
                    break
                i -= 1
        elif msg.content == '4':
            embed = discord.Embed(title='discord.AutoShardedClient', description='このクライアントは Client に似ていますが、管理しやすく、かつ透過的なシングルプロセスのBotに分割するという複雑な処理を行います。\nこのクライアントは、実装に関して内部的に複数のシャードに分割されていても、単一のシャードの通常の Client のように使用することができます。これにより、IPCやその他の複雑なインフラストラクチャへの対処を行う必要がなくなります。\n少なくとも1000を超えるギルドで使用される場合にのみ、このクライアントを使用することをおすすめします。\nshard_count が指定されていない場合、ライブラリはBot Gatewayのエンドポイント呼び出しを使用して使用するシャードの数を見つけ出します。\nshard_ids パラメータが指定されている場合、それらのシャードIDが内部シャードの起動時に使用されます。これを使用する場合 shard_count の指定が必須です。このパラメータを省略した場合は、クライアントは0から shard_count - 1 までのシャードを起動します。\n\n1:discord.AutoShardedClient.shard_ids\n2:discord.AutoShardedClient.latency\n3:discord.AutoShardedClient.latencies\n4:discord.AutoShardedClient.get_shard\n5:discord.AutoShardedClient.shards\n6:discord.AutoShardedClient.connect\n7:discord.AutoShardedClient.close\n8:discord.AutoShardedClient.change_presence\n9:discord.AutoShardedClient.is_ws_ratelimited')
            await message.edit(content='1~9の数字で項目の右の数字を指定してください。\nendで受付を終了します。', embed=embed)
            msg = await client.wait_for('message', check=check)
            if msg.content == '1':
                embed = discord.Embed(title='discord.AutoShardedClient.shard_ids', description='An optional list of shard_ids to launch the shards with.\n\nType:Optional[List[int]]')
                await message.edit(embed=embed)
            elif msg.content == '2':
                embed = discord.Embed(title='discord.AutoShardedClient.latency', description='Measures latency between a HEARTBEAT and a HEARTBEAT_ACK in seconds.\nこれは Client.latency() と同様に機能しますが、すべてのシャードの平均待ち時間を使用する点が異なります。シャードの待ち時間のリストを取得するには latencies プロパティを参照してください。準備ができていない場合は nan を返します。\n\nType:float')
                await message.edit(embed=embed)
            elif msg.content == '3':
                embed = discord.Embed(title='discord.AutoShardedClient.latencies', description='A list of latencies between a HEARTBEAT and a HEARTBEAT_ACK in seconds.\nこれは、 (shard_id, latency) の要素を持つタプルのリストを返します。\n\nType:List[Tuple[int, float]]')
                await message.edit(embed=embed)
            elif msg.content == '4':
                embed = discord.Embed(title='discord.AutoShardedClient.get_shard', description='Optional[ShardInfo]: Gets the shard information at a given shard ID or None if not found.')
                await message.edit(embed=embed)
            elif msg.content == '5':
                embed = discord.Embed(title='discord.AutoShardedClient.shards', description='Returns a mapping of shard IDs to their respective info object.\n\nType:Mapping[int, ShardInfo]')
                await message.edit(embed=embed)
            elif msg.content == '6':
                embed = discord.Embed(title='discord.AutoShardedClient.connect', description='This function is a coroutine.\nWebSocket接続を作成し、Discordからのメッセージをリッスンできるようにします。これはイベントシステム全体とライブラリの様々な機能を実行するループです。WebSocket接続が終了するまで、制御は再開されません。\n\nパラメータ\nreconnect (bool) -- インターネットの障害やDiscord側の特定の障害が発生した際に再接続を試みるかどうかを表します。不正な状態へつながることによる特定の切断（無効なシャーディングペイロードや不正なトークンなど）は処理されません。\n\n例外\n・GatewayNotFound -- If the gateway to connect to Discord is not found. Usually if this is thrown then there is a Discord API outage.\n・ConnectionClosed -- The websocket connection has been terminated.')
                await message.edit(embed=embed)
            elif msg.content == '7':
                embed = discord.Embed(title='discord.AutoShardedClient.close', description='This function is a coroutine.\nDiscordとの接続を閉じます。')
                await message.edit(embed=embed)
            elif msg.content == '8':
                embed = discord.Embed(title='discord.AutoShardedClient.change_presence', description='This function is a coroutine.\nクライアントのプレゼンスを変更します。\n例\n```python\ngame = discord.Game("with the API")\nawait client.change_presence(status=discord.Status.idle, activity=game)\n```\nバージョン 2.0 で変更: Removed the afk keyword-only parameter.\n\nパラメータ\n・activity (Optional[BaseActivity]) -- 実行中のアクティビティ。何も実行していない場合は None です。\n・status (Optional[Status]) -- 変更するステータスを示します。 None の場合、 Status.online となります。\n・shard_id (Optional[int]) -- プレゼンスを変更したいシャードのshard_id。指定されていない、または None が渡された場合はBotがアクセスできるすべてのシャードのプレゼンスが変更されます。\n\n例外\nInvalidArgument -- If the activity parameter is not of proper type.')
                await message.edit(embed=embed)
            elif msg.content == '9':
                embed = discord.Embed(title='discord.AutoShardedClient.is_ws_ratelimited', description='bool: Whether the websocket is currently rate limited.\nThis can be useful to know when deciding whether you should query members using HTTP or via the gateway.\nThis implementation checks if any of the shards are rate limited. For more granular control, consider ShardInfo.is_ws_ratelimited().\nバージョン 1.6 で追加.')
                await message.edit(embed=embed)
            elif msg.content == 'end':
                await message.edit(content='ended')
            else:
                await msg.channel.send('!?!?!invalid index!?!?!')
            elif msg.content == '5':
                embed = discord.Embed(title='discord.AppInfo[1]', description='Discordが提供するBotのアプリケーション情報を表します。\n1:discord.AppInfo.id\n2:discord.AppInfo.name\n3:discord.AppInfo.owner\n4:discord.AppInfo.team\n5:discord.AppInfo.description')
                await message.edit(content='1~10で数字を指定してください。\nnextで次のページ、endで受付を終了します。', embed=embed)
                page = 1
                def check(me):
                    return m.author == me.author and m.channel == me.channel
                for i in range(600):
                    msg = await client.wait_for('message', check=check)
                    if msg.content == '1':
                        if page == 1:
                            embed = discord.Embed(title='discord.AppInfo.id', description='The application ID.\nType:int')
                            await message.edit(embed=embed)
                    elif msg.content == '2':
                        if page == 1:
                            embed = discord.Embed(title='discord.AppInfo.name', description='The application name.Type:str')
                            await message.edit(embed=embed)
                    elif msg.content == '3':
                        if page == 1:
                            embed = discord.Embed(title='discord.AppInfo.owner', description='The application owner.\nType:User')
                            await message.edit(embed=embed)
                    elif msg.content == '4':
                        if page == 1:
                            embed = discord.Embed(title='discord.AppInfo.team', description='The application\'s team.\nバージョン 1.3 で追加.\nType:Optional[Team]')
                            await message.edit(embed=embed)
                    elif msg.content == '5':
                        if page == 1:
                            embed = discord.Embed(title='discord.AppInfo.description', description='The application description.\nType:str')
                            await message.edit(embed=embed)
        elif msg.content == 'end':
            await message.edit(content='ended')
        else:
            await msg.channel.send('!?!?!invalid index!?!?!')
client.run(TOKEN)
