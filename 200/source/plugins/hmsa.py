from pyrogram import filters
from config import *
import random

@Client.on_message(filters.command(['اهمس'], ".") & filters.reply)
async def HamsaR(c, m):
    rand = random.randint(0, 99999999999999)
    user_id = m.reply_to_message.from_user.id
    msg = await m.edit("👀")
    inline = await c.get_inline_bot_results(bot_user, f"hmsa {rand}")
    q_ = await c.send_inline_bot_result(
        m.chat.id,
        query_id=inline.query_id,
        result_id=inline.results[0].id,
        reply_to_message_id=m.reply_to_message.id
    )
    MSG_ID = q_.updates[0].id
    r.set(f"{sudo_id}:hmsa:{rand}:to", user_id)
    r.set(f"{sudo_id}:hmsa:{rand}:from", m.from_user.id)
    r.set(f"{sudo_id}:hmsa:{rand}:chat", m.chat.id)
    r.set(f"{sudo_id}:hmsa:{rand}:q_id", MSG_ID)
    r.set(f"{sudo_id}:hmsa:{rand}:msg_id", m.reply_to_message.id)
    await msg.delete()
