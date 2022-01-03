import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SeiraRobot.events import register as MEMEK
from SeiraRobot import telethn as tbot

PHOTO = "https://telegra.ph/file/ed27010abc3804bebbddd.jpg"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  LUNA = "**Xin Chào Tôi Là OGGY VN!** \n\n"
  LUNA += "💎 **Tôi Đang Làm Việc Như Một Con Ong Thợ** \n\n"
  LUNA += "💎 **Chủ Nhân Tôi Là : [OGGY Là Trai Zin :3](https://t.me/oggyvn)** \n\n"
  LUNA += f"💎 **Phiên bản Telethon : {tlhver}** \n\n"
  LUNA += f"💎 **Phiên bản Pyrogram : {pyrover}** \n\n"
  LUNA += "**Cảm ơn vì đã thêm OGGY Vào Nhóm Ạ💜**"
  BUTTON = [[Button.url("Hỗ Trợ Lệnh", "https://t.me/oggyvipbot?start=help"), Button.url("Hỗ Trợ", "https://t.me/oggyvn")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)

