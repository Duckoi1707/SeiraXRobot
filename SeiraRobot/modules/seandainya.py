import random
from SeiraRobot.events import register
from SeiraRobot.events import telethn

APAKAH_STRING = ["Haha Chào !", 
                 "Bestie không thể", 
                 "Tôi hy vọng nó sẽ trở thành sự thật, amen✨", 
                 "Heleh ... Đang mơ !",
                 "Nào, đi nào, THẦN 💜",
                 "NGGA MUNGKIN..HAHAHA",
                 "Vâng, bạn không biết, tại sao lại hỏi OGGY",
                 "Nhục đậu khấu của bố bạn là phẳng Xixixixi",
                 "Khả thin..",
                 "Thử hỏi quản trị viên🤭"
                ]


@register(pattern="^/seandainya ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('seandainya apa boss?')
        return
    await event.reply(random.choice(APAKAH_STRING))
