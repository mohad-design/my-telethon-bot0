from config import *
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def Creat_log_chat():
    if not r.get(f"{sudo_id}:LOG_CHAT"):
        bot_user = bot.me.username
        try:
            log_chat = await app.create_supergroup("جروب تخزين تليثون استيفن", "- لاتقم بتغيير اي شيئ هنا👀❌\n\n- هذا الكود بواسطه المبرمج استيفن  -> @Ues_steven")
        except Exception as e:
            print(f"--------=> LOG CHAT ERROR | {e}")
        try:
            await app.add_chat_members(log_chat.id, bot_user)
        except Exception as e:
            print(f"--------=> LOG CHAT ERROR | {e}")
        try:
            await app.promote_chat_member(log_chat.id, bot_user)
        except Exception as e:
            print(f"--------=> LOG CHAT ERROR | {e}")
        r.set(f"{sudo_id}:LOG_CHAT", log_chat.id)
        print(f"--------=> LOG CHAT CREATED | {log_chat.id}")
        await app.send_message(log_chat.id, "سالخير يا رايق**بدال شوفت الرساله دي انت كده نصبت تليثون صح.... يوزر صاحب العظمه👉 @Ues_steven**")
        await bot.send_photo(log_chat.id, photo=f"https://t.me/lkkkkkli/11", caption=f"""تم التنصيب علي سوبر استيفن\nلمعرفة الاوامر الخاصه بك قم بكتابة\n.اوامري""" , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="؍`𝐬𝐭𝐞𝐯𝐞𝐧 ٭", url=f"https://t.me/Ues_steven")]]))
    else:
        log_chat = r.get(f"{sudo_id}:LOG_CHAT")
        print(f"--------=> LOG CHAT | {log_chat}")
