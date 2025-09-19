from pyrogram import Client, filters, enums
from config import *
import os, time

os.environ['TZ'] = 'Africa/Cairo'
time.tzset()


@Client.on_message(filters.private & ~filters.bot)
async def pv_cmd(c, msg):
    log_chat = r.get(f"{sudo_id}:LOG_CHAT")
    if msg.from_user.id != sudo_id and msg.from_user.id != int(777000):
        try:
            await msg.forward(log_chat)
        except:
            if msg.media == enums.MessageMediaType.VIDEO:
                await msg.download("./Ttl.mp4")
                await app.send_video(log_chat, "Ttl.mp4")
                os.remove("./Ttl.mp4")
            elif msg.media == enums.MessageMediaType.PHOTO:
                await msg.download("./Ttl.jpg")
                await app.send_photo(log_chat, "Ttl.jpg")
                os.remove("./Ttl.jpg")
            pass
        if r.sismember(f"{sudo_id}mute_pv", msg.chat.id):
            await msg.delete(revoke=True)
            return
        if r.get(f"{sudo_id}welcome"):
            if not r.sismember(f"{sudo_id}accept", msg.chat.id):
                if r.get(f"{sudo_id}waiting{msg.chat.id}"):
                    r.delete(f"{sudo_id}waiting{msg.chat.id}")
                    await msg.reply("✷ تم ارسال رسالتك بنجاح \n✷ قام النظام بكتمك انتظر حتا يقوم مالك الحساب بالرد عليك ❄️")
                    r.sadd(f"{sudo_id}mute_pv", msg.chat.id)
                    r.delete(f"{sudo_id}waiting{msg.chat.id}")
                    return
                r.set(f"{sudo_id}waiting{msg.chat.id}", "on")
                PM_logo = r.get(f"{sudo_id}:PMG_MEDIA") or "https://t.me/lkkkkkli/11"
                CHANNEL = r.get(f"{sudo_id}:CHANNEL") or "Hx_x0"
                CHANNEL = CHANNEL.replace('@', '')
                PM_text = r.get(f"{sudo_id}:PM_TEXT_CUSTOM") or "✷ نورت شاتي يا زعيم انا حاليا مشغول ارمي رسالتك لحد ما افتح وهرد عليك متقلقش 🔥❤️"
                send = c.send_video if PM_logo.endswith(".mp4") else c.send_photo
                try:
                    await send(
                        msg.chat.id,
                        PM_logo,
                        caption=f"<b>{PM_text}</b>\n\n💠 [ُِꪔِᥡ ُِᥴَِɦُِᥲَِꪀَِꪀُِᥱَِᥣ](https://t.me/{CHANNEL}) | [ᥱᥣ Ꭵƚᥲᥣᥡ](https://t.me/Hx_x0) 💠"
                    )
                except Exception as e:
                    print(e)
                    await msg.reply(f"<b>{PM_text}</b>\n\n💠 [ُِꪔِᥡ ُِᥴَِɦُِᥲَِꪀَِꪀُِᥱَِᥣ](https://t.me/{CHANNEL}) | [ᥱᥣ Ꭵƚᥲᥣᥡ](https://t.me/Hx_x0) 💠")
                return
    else:
        if msg.text == ".قبول" or msg.text == ".الغاء كتم":
            r.srem(f"{sudo_id}mute_pv", msg.chat.id)
            r.sadd(f"{sudo_id}accept", msg.chat.id)
            await msg.edit("✷ تم السماح له بالتحدث")
        if msg.text == ".رفض":
            r.srem(f"{sudo_id}accept", msg.chat.id)
            await msg.edit("✷ تم رفض العضو")
        if msg.text == ".كتم":
            if msg.chat.id == sudo_id:
                return await msg.edit("مينفعش تكتم نفسك")
            if msg.chat.id == 5993309733:
                return await msg.edit("✷ لا يمكنك كتم ايطالي")
            if msg.chat.id == 6751649015:
                return await msg.edit("لايمكنك كتم ليدر")
            r.sadd(f"{sudo_id}mute_pv", msg.chat.id)
            await msg.edit("✷ تم كتم العضو")


@Client.on_message(filters.group)
async def gp(client, msg):
    log_chat = r.get(f"{sudo_id}:LOG_CHAT")
    current_time = time.strftime('%H:%M')
    chatt = str(msg.chat.id)
    chat = chatt.replace("-100", "").replace("-", "")
    msg_link = f"[✷ اضغط هنا لعرض الرساله](https://t.me/c/{chat}/{msg.id})"
    if msg.mentioned:
        if msg.from_user:
            try:
                txt = f"✷ لديك منشن من العضو [{msg.from_user.first_name}](tg://user?id={msg.from_user.id}) \n✷ اسم الجروب {msg.chat.title} \n✷ الوقت {current_time} \n{msg_link}"
                await app.send_message(log_chat, txt)
                await msg.forward(log_chat)
            except:
                pass
        else:
            txt = f"✷ لديك منشن من القناه {msg.sender_chat.title} \n✷ اسم الجروب {msg.chat.title} \n✷ الوقت {current_time} \n{msg_link}"
            await app.send_message(log_chat, txt)
            await msg.forward(log_chat)
    if msg.from_user:
        sender_id = msg.from_user.id
    elif msg.sender_chat:
        sender_id = msg.sender_chat.id
    if r.sismember(f"{sudo_id}mute", sender_id) or r.sismember(f"{sudo_id}mute{msg.chat.id}", sender_id):
        try:
            await msg.delete()
        except:
            pass
    if r.sismember(f"{sudo_id}ban", sender_id):
        try:
            await msg.delete()
            await client.ban_chat_member(msg.chat.id, msg.from_user.id)
        except:
            pass
