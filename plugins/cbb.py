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
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='https://t.me/botsbyadmin'>ᴀᴅᴍɪɴ</a>\n○ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/botsbyadmin'>ᴀᴅᴍɪɴ ᴋᴇ ʙᴏᴛꜱ</a>\n○ ꜱᴛᴜꜰꜰ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/+A4wxGbQ3ELFkY2Fl'>ᴛʜᴇ ʙᴏʏꜱ</a>\n○ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href='https://t.me/+qG-885heZ8syYWFl'>ᴛʜᴇ ʙᴏʏꜱ ɢᴄ</a>\n○ ꜱᴛᴜꜰꜰ ʙᴀᴄᴋᴜᴘ : <a href='https://t.me/stuffbackup'>ꜱᴛᴜꜰꜰ ʙᴀᴄᴋᴜᴘ</a>\n○ᴄᴏɴᴛᴀᴄᴛ ᴜꜱ : <a href='https://t.me/reachoutadminbot'>ʀᴇᴀᴄʜᴏᴜᴛᴀᴅᴍɪɴʙᴏᴛ</a></b>",
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
