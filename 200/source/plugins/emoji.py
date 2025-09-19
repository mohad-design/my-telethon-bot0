from pyrogram import Client, filters
import re
import asyncio
from func.Force_join import FORCE_JOIN
from func import fonts as emojify


@Client.on_message(filters.command("^ايمو", prefixes=f".") & filters.me)
async def emoji(c, m):
    list_ = m.text.split(' ', 2)
    if len(list_) < 2:
        await m.edit("**الصيغه غلط !!**")
        return
    emoji = m.text.split(' ', 2)[1]
    if len(list_) == 3:
        text = m.text.split(' ', 2)[2]
    else:
        await m.edit("**الصيغه غلط !!**")
        return
    result = ""
    for a in text:
        a = a.lower()
        if a in emojify.kakashitext:
            char = emojify.itachiemoji[emojify.kakashitext.index(a)].format(cj=emoji)
            result += char
        else:
            result += a
    await m.edit(result)
    await FORCE_JOIN(c)