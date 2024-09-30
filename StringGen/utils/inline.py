from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ", callback_data="gensession")],
        [
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=SUPPORT_CHAT),
            InlineKeyboardButton(
                text="𝐒𝐔𝐏𝐏𝐎𝐑𝐓", url="https://t.me/TG_NAME_STYLE"
            ),
        ],
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="𝐏𝐘𝐑𝐎𝐆𝐑𝐀𝐌 v1", callback_data="pyrogram1"),
            InlineKeyboardButton(text="𝐏𝐀𝐑𝐎𝐆𝐑𝐀𝐌 v2", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="𝐓𝐑𝐘 𝐀𝐆𝐀𝐈𝐍", callback_data="gensession")]]
)
