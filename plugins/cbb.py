#(©)codeflix_bots

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>ᴀᴅᴍɪɴ</a>\n○ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/botsbyadmin'>ᴀᴅᴍɪɴ ᴋᴇ ʙᴏᴛꜱ</a>\n○ ᴍᴏᴠɪᴇs ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/indmoviesfree'>ɪɴᴅᴍᴏᴠɪᴇꜱꜰʀᴇᴇ</a>\n○ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href=https://t.me/+bTe4ijGa9eg1MDc9''>ɪɴᴅᴍᴏᴠɪᴇꜱꜰʀᴇᴇ ɢᴄ</a>\n○ ᴍᴏᴅ ᴀᴘᴋꜱ ᴀɴᴅ ɢᴀᴍᴇꜱ : <a href='https://t.me/modapksfreeio'>ᴍᴏᴅᴀᴘᴋꜱꜰʀᴇᴇ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ᴄʜᴀɴɴᴇʟ', url='https://t.me/botsbyadmin')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pas
