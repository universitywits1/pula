class script(object):
    START_TXT = """нєℓℓσω {}\n\n🌝 𝘛𝘩𝘦𝘳𝘦 𝘐𝘴 𝘕𝘰𝘵𝘩𝘪𝘯𝘨 𝘠𝘰𝘶 𝘕𝘦𝘦𝘥\n\n𝘏𝘦𝘳𝘦 𝘞𝘪𝘵𝘩𝘰𝘶𝘵 𝘞𝘢𝘴𝘵𝘪𝘯𝘨 𝘛𝘪𝘮𝘦..!!\n\n🌚 𝘛𝘩𝘢𝘵'𝘴 𝘈𝘭𝘭 𝘔𝘢𝘯 𝘐 𝘞𝘪𝘭𝘭 𝘗𝘳𝘰𝘷𝘪𝘥𝘦\n\n𝘔𝘰𝘷𝘪𝘦𝘴 𝘐𝘯 𝘗𝘔✨\n\n𝐌𝐚𝐢𝐧𝐭𝐚𝐢𝐧𝐞𝐝 𝐁𝐲 :  <a href='https://t.me/Rafeeq_Kunnimon'>★ 𝐑𝐚𝐟𝐞𝐞𝐪 ★</a> """
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """<b>🥱 My Name : 𝐒𝐡𝐢𝐧𝐨𝐛𝐮 𝐊𝐨𝐜𝐡𝐨 ❤️
🕵‍♂ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 : <a href='https://t.me/Rafeeq_Kunnimon'>★ 𝐑𝐚𝐟𝐞𝐞𝐪 ★</a>
📚 𝐋𝐢𝐛𝐫𝐚𝐫𝐲 : 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦
🖥 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 : 𝐏𝐲𝐭𝐡𝐨𝐧 𝟑
☢️ 𝐃𝐚𝐭𝐚 𝐁𝐚𝐬𝐞 : 𝐌𝐨𝐧𝐠𝐨 𝐃𝐛
🏡 𝐁𝐨𝐭 𝐆𝐫𝐨𝐮𝐩 : @MovieRosterGroup </b>"""
    SOURCE_TXT = """<b>NOTE:</b>
👋<b><i>എന്താടാ മോനെ നോക്കുന്നേ നിനക്ക് ആവശ്യമായിട്ടുള്ളത് ഇവിടെ ഇല്ല 😌
</i></b>
<b>🕵‍♂ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 : <a href='https://t.me/Rafeeq_Kunnimon'>★ 𝐑𝐚𝐟𝐞𝐞𝐪 ★</a> </b>
"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>
- Filter is the feature were users can set automated replies for a particular keyword and tessa will respond whenever a keyword is found the message
<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.
<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>
- Eva Maria Supports both url and alert inline buttons.
<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format
<b>URL buttons:</b>
<code>[Button Text](buttonurl:https//t.me/Movie_Roster_bot)</code>
<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>
<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains cam rip, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>
- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.
<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM
<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>
<b>NOTE:</b>
these are the extra features of tessa
<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>
<b>NOTE:</b>
This module only works for my admins
<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝐓𝐨𝐭𝐚𝐥 𝐅𝐢𝐥𝐞𝐬: <code>{}</code><b>\n\n★ 𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫𝐬 :</b> <code>{}</code><b>\n\n★ 𝐓𝐨𝐭𝐚𝐥 𝐂𝐡𝐚𝐭𝐬 :</b> <code>{}</code><b>\n\n★ 𝐔𝐬𝐞𝐝 𝐒𝐭𝐨𝐫𝐚𝐠𝐞 :</b> <code>{}</code> 𝙼𝚒𝙱<b>\n\n★ 𝐅𝐫𝐞𝐞 𝐒𝐭𝐨𝐫𝐚𝐠𝐞 :<b> <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
