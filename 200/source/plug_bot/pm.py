from pyrogram import filters, Client
import re
from config import *


@Client.on_message(filters.private)
async def pm(c, m):
    if m.text and re.findall("/start hmsa(\\d+)", m.text):
        rand = re.findall("/start hmsa(\\d+)", m.text)[0]
        from_id = r.get(f"{sudo_id}:hmsa:{rand}:from")
        if int(m.from_user.id) == int(from_id):
            r.set(f"{sudo_id}:hmsa:{from_id}:state", "ready")
            r.set(f"{sudo_id}:hmsa:{from_id}:rand", rand)
            await m.reply("- ارسل الهمسه الان :")
            return
        else:
            await m.reply("- انت مالك ياخي الامر مش ليك")
            return
    if m.text and r.get(f"{sudo_id}:hmsa:{m.from_user.id}:state") == "ready":
        # get data #
        rand = r.get(f"{sudo_id}:hmsa:{m.from_user.id}:rand")
        chat_id = r.get(f"{sudo_id}:hmsa:{rand}:chat")
        q_id = int(r.get(f"{sudo_id}:hmsa:{rand}:q_id"))
        msg_id = int(r.get(f"{sudo_id}:hmsa:{rand}:msg_id"))
        # set text #
        r.set(f"{sudo_id}:hmsa:{rand}:text", m.text)
        await m.reply("- تم ارسال الهمسه بنجاح")
        r.delete(f"{sudo_id}:hmsa:{m.from_user.id}:state")
        # send inline #
        try:
            inline = await app.get_inline_bot_results(bot_user, f"send_hmsa {rand}")
            await app.send_inline_bot_result(
                chat_id,
                query_id=inline.query_id,
                result_id=inline.results[0].id,
                reply_to_message_id=msg_id
            )
        except Exception as e:
            print(e)
        # delete old #
        try:
            await app.delete_messages(chat_id, q_id)
        except Exception as e:
            print(e)
        return