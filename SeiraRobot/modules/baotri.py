from pyrogram import filters, Client
from pyrogram.types import Message
from SeiraRobot.utils.onoff import (is_on_off, add_on, add_off)
from telethon.tl.types import ChannelParticipantsAdmins

@register(pattern=("/baotri"))
async def smex(_, message):
    usage = "**usage:**\n/maintenance [enable|disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    chat_id = message.chat.id
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        user_id = 1
        await add_on(user_id)
        await message.reply_text("✅ chế độ bảo trì được kích hoạt\n\n• từ bây giờ, người dùng không thể phát nhạc sau khi chế độ bảo trì bị tắt.")
    elif state == "disable":
        user_id = 1
        await add_off(user_id)
        await message.reply_text("❌ chế độ bảo trì bị vô hiệu hóa\n\n• từ bây giờ, người dùng có thể dùng lại.")
    else:
        await message.reply_text(usage)
