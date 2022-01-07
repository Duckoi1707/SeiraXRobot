
import os
import requests
import datetime
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, version
from SeiraRobot.events import register
from SeiraRobot import telethn as aasf
from SeiraRobot import StartTime, dispatcher

edit_time = 5
""" =======================2022====================== """
newyear1 = "https://telegra.ph/file/ee0fa410c0414a650f673.jpg"
newyear2 = "https://telegra.ph/file/ee0fa410c0414a650f673.jpg"
newyear3 = "https://telegra.ph/file/ee0fa410c0414a650f673.jpg"
newyear4 = "https://telegra.ph/file/789d31689646320c217c3.jpg"
newyear5 = "https://telegra.ph/file/b8e2f6eff4ddd608561d8.jpg"
""" =======================2022====================== """

@register(pattern=("/luatbot"))
async def hmm(event):
    chat = await event.get_chat()
    await event.delete()
    pm_caption = f"**Luật BOT OGGY VN **\n\n"
    pm_caption += "**1.Không Lạm quyền bot,không ban hoặc mute cá nhân nào khi không có lí do\n2.Sử dụng bot văn minh không spam tin nhắn bot không cố tình phá hoại bot tập thể\n3.Hãy là người có ý thức bảo vệ văn hoá tránh những logic sai suy nghĩ của người khác\n Cảm Ơn Bởi OGVN Team**\n\n"
    on = await aasf.send_file(event.chat_id, file=newyear1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await aasf.edit_message(event.chat_id, on, file=newyear2) 

    await asyncio.sleep(edit_time)
    ok2 = await aasf.edit_message(event.chat_id, ok, file=newyear3)

    await asyncio.sleep(edit_time)
    ok3 = await aasf.edit_message(event.chat_id, ok2, file=newyear4)
    
    await asyncio.sleep(edit_time)
    ok4 = await aasf.edit_message(event.chat_id, ok3, file=newyear1)
    
    await asyncio.sleep(edit_time)
    ok5 = await aasf.edit_message(event.chat_id, ok4, file=newyear2)
    
    await asyncio.sleep(edit_time)
    ok6 = await aasf.edit_message(event.chat_id, ok5, file=newyear3)
    
    await asyncio.sleep(edit_time)
    ok7 = await aasf.edit_message(event.chat_id, ok6, file=newyear4)
    
    await asyncio.sleep(edit_time)
    ok8 = await aasf.edit_message(event.chat_id, ok7, file=newyear5)
