from pyrogram import filters
from config import *
import random

@Client.on_message(filters.command(['xo'], "."))
async def xo_game(c, m):
    msg = await m.edit("🕹")
    inline = await c.get_inline_bot_results("xoBot", f" ")
    q_ = await c.send_inline_bot_result(
        m.chat.id,
        query_id=inline.query_id,
        result_id=inline.results[0].id
    )
    await msg.delete()
