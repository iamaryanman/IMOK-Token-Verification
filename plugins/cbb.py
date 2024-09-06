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
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='https://t.me/indmoviesfreeadminbot'></a>\n○ ᴍʏ ʙᴀᴄᴋ-ᴜᴘ ᴄʜᴀɴɴᴇʟ  : <a href='https://t.me/indmoviesfree'>ɪɴᴅᴍᴏᴠɪᴇꜱꜰʀᴇᴇ ʙᴀᴄᴋ-ᴜᴘ</a>\n○ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/+h1JIR9IcKrY2ODM9'>ɪɴᴅᴍᴏᴠɪᴇꜱꜰʀᴇᴇ ᴍᴀɪɴ</a>\n○ᴄᴏɴᴛᴀᴄᴛ ᴜꜱ : <a href='https://t.me/indmoviesfreeadminbot'>ɪɴᴅᴍᴏᴠɪᴇꜱꜰʀᴇᴇᴀᴅᴍɪɴ</a></b>",
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
