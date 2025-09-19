import asyncio
import random
from collections import deque
from func.Force_join import FORCE_JOIN
import requests
from pyrogram import Client, filters
from pyrogram.types import Message

def get_name(msg):
    if msg.from_user.last_name:
        last_name = msg.from_user.last_name
    else:
        last_name = ""
    if msg.from_user.first_name:
        first_name = msg.from_user.first_name
    else:
        first_name = ""
    return f"[{first_name} {last_name}](tg://user?id={msg.from_user.id})"


async def is_Admin(chat, id):
    admins = []
    async for m in app.get_chat_members(chat, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        admins.append(m.user.id)
    if id in admins:
        return True
    else:
        return False


@Client.on_message(filters.regex("^.متحركات (.*)") & filters.me)
async def some(c, msg):
    count = 1
    if ";" in msg.text:
        inpt, count = msg.text.split(";")
    if 0 > int(count) > 20:
        await msg.edit("**- يجب عليك كتابة عدد المتحركات من عدد يبدأ من 1 الى 20"
        )
    jmthonmsg = await c.send_message(msg.chat.id, "- جار ارسال المتحركات انتظر قليلا")
    res = requests.get("https://giphy.com/")
    res = res.text.split("GIPHY_FE_WEB_API_KEY =")[1].split("\n")[0]
    api_key = res[2:-1]
    r = requests.get(
        f"https://api.giphy.com/v1/gifs/search?q={inpt}&api_key={api_key}&limit=50"
    ).json()
    list_id = [r["data"][i]["id"] for i in range(len(r["data"]))]
    rlist = random.sample(list_id, int(count))
    for items in rlist:
        await c.send_document(msg.chat.id,  f"https://media.giphy.com/media/{items}/giphy.gif",
                              reply_to_message_id=msg.id)


# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.regex("^.همسة (.*)") & filters.me)
async def wspr(c, msg:Message):
    rrrd7 = "@nnbbot"
    tap = await c.get_inline_bot_results(rrrd7, msg.text[6:])
    await tap[0].click(msg.chat.id)
    await msg.delete()


@Client.on_message(filters.command("م26$", prefixes=f".") & filters.me)
async def _(c, msg):
    if not msg.text[0].isalpha() and msg.text[0] not in ("/", "#", "@", "!"):
        await msg.edit(
            "⌯︙اوامر الهمسه واكس او \n\n✷︙الامر  ✷ `.همسة`\n✷︙الاستخدام  ✷ لكتابة همسه سرية لشخص في المجموعه \n\n⌯︙الامر ✷ `.الهمسة`\n⌯︙استخدامه ✷ لعرض كيفية كتابة همسة سرية\n\n⌯︙الامر ✷ `.اكس او `\n ⌯︙استخدامه ✷ ففط ارسل الامر لبدء لعبة اكس او\n\n⌯︙CH  - @Hx_x0")


@Client.on_message(filters.command("الهمسة$", prefixes=f".") & filters.me)
async def _(c, msg):
    if not msg.text[0].isalpha() and msg.text[0] not in ("/", "#", "@", "!"):
        await msg.edit(
            "**⌯︙شـرح كيـفية كـتابة همـسة سـرية**\n⌯︙اولا اكتب الامر  .همسة  بعدها الرسالة بعدها اكتب معرف الشخص\n⌯︙مـثال  :   `.همسة ههلا @Ues_steven`")


@Client.on_message(filters.command("اكس او$", prefixes=f".") & filters.me)
async def gamez(c, msg):
    jmusername = "@xoBot"
    uunzz = "play"
    tap = await app.get_inline_bot_results(jmusername, uunzz)
    await tap[0](msg.chat.id)
    await msg.delete()

# == == == == == == == == == == == == == == == == == == == ==


@Client.on_message(filters.command("هينه$", prefixes=f".") & filters.me)
async def permalink_heno(c, msg):
    heno = ['ده بغل مش مستآهل يتهان بالله 🧐😂', 'بس يآبطيخه اخرس خآلص 🤫']
    if not msg.reply_to_message:
        return
    if msg.reply_to_message.from_user.id == 5993309733:
        return await c.send_message(msg.chat.id, f"**- لا عمري ده مطور السورس مقدرش **")
    if msg.reply_to_message.from_user.id == 6751649015:
        return await c.send_message(msg.chat.id, f"**- ر**")
    if msg.reply_to_message.from_user.id == 5893261163:
        return await c.send_message(msg.chat.id, f"**- ن**")
    muh = msg.from_user.first_name.replace("\u2060", "") if msg.from_user.first_name else msg.from_user.id
    sos = random.choice(heno)
    await c.send_message(msg.chat.id, f"{sos} .")

# == == == == == == == == == == == == == == == == == == == ==


@Client.on_message(filters.command("نسبة الحب$", prefixes=f".") & filters.me)
async def permalink_hob(c, msg):
    roz = ['10', '20', '30','40','50','60','70','80','90','100']
    if not msg.reply_to_message:
        return
    muh = msg.from_user.first_name.replace("\u2060", "") if msg.from_user.first_name else msg.reply_to_message
    rza = random.choice(roz)
    await msg.edit( f"✷ العضو {get_name(msg.reply_to_message)} \n✷ نسبه الحب بينك وبينه هي {rza}"
    )



@Client.on_message(filters.command("نسبة الانوثة$", prefixes=f".") & filters.me)
async def permalink_onotha(c, msg):
    rr7 = ['10', '20', '30','40','50','60','70','80','90','100']
    if not msg.reply_to_message:
        return
    if msg.reply_to_message.from_user.id == 5993309733:
        return await msg.edit(f"**- اكتم ابوك ايطابي ازاي؟**")
    if msg.reply_to_message.from_user.id == 6751649015:
        return await msg.edit(f"**- بابا ليدر دا عيب**")
    if msg.reply_to_message.from_user.id == 5893261163:
        return await msg.edit(f"**- متجيش ع صعيدي بكتم علشان هيركبك**")
    muh = msg.from_user.first_name.replace("\u2060", "") if msg.from_user.first_name else msg.reply_to_message
    sos = random.choice(rr7)
    return await msg.edit( f" ✷ العضو {get_name(msg.reply_to_message)} \n✷ نسبة الانوثه هي {sos}"
    )



@Client.on_message(filters.command("نسبة الغباء$", prefixes=f".") & filters.me)
async def permalink_abaaa(c, msg):
    rr7 = ['10', '20', '30','40','50','60','70','80','90','100']
    if not msg.reply_to_message:
        return
    muh = msg.from_user.first_name.replace("\u2060", "") if msg.from_user.first_name else msg.reply_to_message
    rzona = random.choice(rr7)
    await msg.edit( f"✷ العضو {get_name(msg.reply_to_message)} \n✷ نسبه غبائه هي {rzona}"
    )



@Client.on_message(filters.command("نسبة الرجولة$", prefixes=f".") & filters.me)
async def permalink_rgola(c, msg):
    kz = ['10', '20', '30','40','50','60','70','80','90','100']
    if not msg.reply_to_message:
        return
    if msg.reply_to_message.from_user.id == 6751649015:
        return await msg.edit(f"**100%**")
    if msg.reply_to_message.from_user.id == 5993309733:
        return await msg.edit(f"**100%**")
    if msg.reply_to_message.from_user.id == 5893261163:
        return await msg.edit(f"**100%**")
    muh = msg.from_user.first_name.replace("\u2060", "") if msg.from_user.first_name else msg.reply_to_message
    sos = random.choice(kz)
    await msg.edit( f" ✷ العضو {get_name(msg.reply_to_message)} \n✷ نسبة رجولته هي {sos}"
    )

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("تحميل$", prefixes=f".") & filters.me)
async def dwn_1(c, msg):
    animation_interval = 0.3
    animation_ttl = range(20)
    animation_chars = ["▮", "▯", "▬", "▭", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 4])

# == == == == == == == == == == == == == == == == == == == ==


@Client.on_message(filters.command("مربع$", prefixes=f".") & filters.me)
async def squre_1(c, msg):
    animation_interval = 0.3
    animation_ttl = range(20)
    animation_chars = ["◧", "◨", "◧", "◨", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 4])

# == == == == == == == == == == == == == == == == == == == ==


@Client.on_message(filters.command("شرطه$", prefixes=f".") & filters.me)
async def up_1(c, msg):
    animation_interval = 0.3
    animation_ttl = range(20)
    animation_chars = ["╹", "╻", "╹", "╻", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 4])

# == == == == == == == == == == == == == == == == == == == ==


@Client.on_message(filters.command("دائره$", prefixes=f".") & filters.me)
async def circle_1(c, msg):
    animation_interval = 0.3
    animation_ttl = range(20)
    animation_chars = ["⚫", "⬤", "●", "∘", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 4])



@Client.on_message(filters.command("تهكير$", prefixes=f".") & filters.me)
async def tahker_1(c, msg):
    animation_interval = 2
    animation_ttl = range(11)
    animation_chars = [                "**🝳︙ جـاري الاتصـال بجهـاز الضحـية لأختـراقـة  📳**",     
           "**🝳︙ أختـراق جهـاز الضحـية الهـددف محـدد جـاري أختـراقـة ㊙️**",       
         "**🝳︙ تحـميل الاخـتراق  ㊙️ .. 0%**\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "**🝳︙ تحـميل الاخـتراق  ㊙️ .. 4%**\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",   
       "**🝳︙ تحـميل الاخـتراق  ㊙️ ..10%**\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",        
        "**🝳︙ تحـميل الاخـتراق  ㊙️ .. 20%**\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",         
       "**🝳︙ تحـميل الاخـتراق  ㊙️ .. 36%**\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",        
        "**🝳︙ تحـميل الاخـتراق  ㊙️ .. 52%**\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",        
        "**🝳︙ تحـميل الاخـتراق  ㊙️ .. 84%**\n█████████████████████▒▒▒▒ `",        
        "**🝳︙ تحـميل الاخـتراق  ㊙️ .. 100%**\n████████████████████████`",       
         "**🝳︙ تـم اخـتراق الضحـية 🆘 وتم سحب صوره وجهات اتصاله بنجاح ⚓🖕**",
            ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 11])
    await FORCE_JOIN(c)        
       
# == == == == == == == == == == == == == == == == == == == ==


@Client.on_message(filters.command("بشره$", prefixes=f".") & filters.me)
async def bshra_1(c, msg):
    animation_interval = 2
    animation_ttl = range(6)
    msg = await c.send_message(msg.chat.id, "ههلا لك....")
    animation_chars = ["😁🏿", "😁🏾", "😁🏽", "😁🏼", "‎😁", "**#بباي....**"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 6])

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("قرد$", prefixes=f".") & filters.me)
async def monkey_1(c, msg):
    animation_interval = 2
    animation_ttl = range(12)
    msg = await c.send_message(msg.chat.id, "خد قرود يرحقلبي 🤗😂")
    animation_chars = ["🐵", "🙉", "🙈", "🙊", "🖕‎🐵🖕", "**بباي...**"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 6])

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("قياس$", prefixes=f".") & filters.me)
async def herber_1(c, msg):
    animation_interval = 2
    animation_ttl = range(10)
    animation_chars = [
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_الاستخدام:** 10%\n\n    ●○○○○○○○○○\n\n    **🔹cpu core**\n\n        **🔹core_الاستخدام:** 5.9%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 8.13GB\n    **🔹used:** 33.77GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹الاستخدام:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 158.98GB\n    **🔹recv:** 146.27GB\n    **🔹sent_packets:** 84518799\n    **🔹recv_packets:** 159720314\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_الاستخدام:** 30%\n\n    ●●●○○○○○○○\n\n    **🔹cpu core**\n\n        **🔹core_الاستخدام:** 20.4%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 7.18GB\n    **🔹used:** 28.26GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●●●●\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹الاستخدام:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 146.27GB\n    **🔹recv:** 124.33GB\n    **🔹sent_packets:** 54635686\n    **🔹recv_packets:** 143565654\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_الاستخدام:** 60%\n\n    ●●●●●●○○○○\n\n    **🔹cpu core**\n\n        **🔹core_الاستخدام:** 60.9%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 6.52GB\n    **🔹used:** 35.78GB\n    **🔹total:** 60.0GB\n    \n    ●●●○○○○○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹الاستخدام:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 124.33GB\n    **🔹recv:** 162.48GB\n    **🔹sent_packets:** 25655655\n    **🔹recv_packets:** 165289456\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_الاستخدام:** 100%\n\n    ●●●●●●●●●●\n\n    **🔹cpu core**\n\n        **🔹core_الاستخدام:** 100.0%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 9.81GB\n    **🔹used:** 30.11GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●●●●\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹الاستخدام:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 162.48GB\n    **🔹recv:** 175.75GB\n    **🔹sent_packets:** 56565435\n    **🔹recv_packets:** 135345655\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_الاستخدام:** 70%\n\n    ●●●●●●●○○○\n\n    **🔹cpu core**\n\n        **🔹core_الاستخدام:** 80.4%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 5.76GB\n    **🔹used:** 29.35GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹الاستخدام:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 175.75GB\n    **🔹recv:** 118.55GB\n    **🔹sent_packets:** 36547698\n    **🔹recv_packets:** 185466554\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_الاستخدام:** 60%\n\n    ●●●●●●○○○○\n\n    **🔹cpu core**\n\n        **🔹core_الاستخدام:** 62.9%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 8.23GB\n    **🔹used:** 33.32GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●○○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹الاستخدام:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 118.55GB\n    **🔹recv:** 168.65GB\n    **🔹sent_packets:** 24786554\n    **🔹recv_packets:** 156745865\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_الاستخدام:** 30%\n\n    ●●●○○○○○○○\n\n    **🔹cpu core**\n\n        **🔹core_الاستخدام:** 30.6%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 9.75GB\n    **🔹used:** 36.54GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●●●●\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹الاستخدام:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 168.65GB\n    **🔹recv:** 128.35GB\n    **🔹sent_packets:** 56565435\n    **🔹recv_packets:** 1475823589\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_الاستخدام:** 10%\n\n    ●○○○○○○○○○\n\n    **🔹cpu core**\n\n        **🔹core_الاستخدام:** 10.2%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 10.20GB\n    **🔹used:** 25.40GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●○○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹الاستخدام:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 128.35GB\n    **🔹recv:** 108.31GB\n    **🔹sent_packets:** 54635686\n    **🔹recv_packets:** 157865426\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_الاستخدام:** 100%\n\n    ●●●●●●●●●●\n\n    **🔹cpu core**\n\n        **🔹core_الاستخدام:** 100.0%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 5.25GB\n    **🔹used:** 31.14GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●●●●\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹الاستخدام:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 108.31GB\n    **🔹recv:** 167.17GB\n    **🔹sent_packets:** 84518799\n    **🔹recv_packets:** 124575356\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_الاستخدام:** 70%\n\n    ●●●●●●●○○○\n\n    **🔹cpu core**\n\n        **🔹core_الاستخدام:** 76.2%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 8.01GB\n    **🔹used:** 33.27GB\n    **🔹total:** 60.0GB\n    \n    ●●●○○○○○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹الاستخدام:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 167.17GB\n    **🔹recv:** 158.98GB\n    **🔹sent_packets:** 36547698\n    **🔹recv_packets:** 165455856\n\n\n**===================**\n",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 10])

# == == == == == == == == == == == == == == == == == == == ==


@Client.on_message(filters.command("يد$", prefixes=f".") & filters.me)
async def yad_1(c, msg):
    animation_interval = 1
    animation_ttl = range(13)
    animation_chars = [
        "👈",
        "👉",
        "☝️",
        "👆",
        "🖕",
        "👇",
        "✌️",
        "🤞",
        "🖖",
        "🤘",
        "🤙",
        "🖐️",
        "👌",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 13])

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("العد التنازلي$", prefixes=f".") & filters.me)
async def down_t_1(c, msg):
    animation_interval = 1
    animation_ttl = range(12)
    animation_chars = [
        "🔟",
        "9️⃣",
        "8️⃣",
        "7️⃣",
        "6️⃣",
        "5️⃣",
        "4️⃣",
        "3️⃣",
        "2️⃣",
        "1️⃣",
        "0️⃣",
        "🆘",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 12])

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("قتل$", prefixes=f".") & filters.me)
async def dier_1(c, msg):
    ALIVE_NAME = (await c.get_users(msg.from_user.id)).mention
    if not msg.reply_to_message:
        name = "مات"
    else:
        name = (await c.get_users(msg.reply_to_message.from_user.id)).mention
    animation_interval = 0.7
    animation_ttl = range(8)
    msg = await c.send_message(msg.chat.id, f"**استعد ايها القائد **__{ALIVE_NAME}....")
    animation_chars = [
        "Ｆｉｉｉｉｉｒｅ",
        f"__**المقاتل **__{ALIVE_NAME}          \n\n_/﹋\_\n (҂`_´)\n <,︻╦╤─ ҉ - \n _/﹋\_\n",
        f"__**المقاتل **__{ALIVE_NAME}          \n\n_/﹋\_\n (҂`_´)\n  <,︻╦╤─ ҉ - -\n _/﹋\_\n",
        f"__**المقاتل **__{ALIVE_NAME}          \n\n_/﹋\_\n (҂`_´)\n <,︻╦╤─ ҉ - - -\n _/﹋\_\n",
        f"__**المقاتل **__{ALIVE_NAME}          \n\n_/﹋\_\n (҂`_´)\n<,︻╦╤─ ҉ - -\n _/﹋\_\n",
        f"__**المقاتل **__{ALIVE_NAME}          \n\n_/﹋\_\n (҂`_´)\n <,︻╦╤─ ҉ - \n _/﹋\_\n",
        f"__**المقاتل **__{ALIVE_NAME}         \n\n_/﹋\_\n (҂`_´)\n  <,︻╦╤─ ҉ - -\n _/﹋\_\n",
        f"__**المقاتل **__{ALIVE_NAME}          \n\n_/﹋\_\n (҂`_´)\n <,︻╦╤─ ҉ - - - {name}\n _/﹋\_\n",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 8])

# == == == == == == == == == == == == == == == == == == == ==



@Client.on_message(filters.command("معاكسه$", prefixes=f".") & filters.me)
async def eyes_1(c, msg):
    await msg.delete()
    animation_interval = 3
    animation_ttl = range(10)
    animation_chars = [
        "👁👁\n  👱🏻‍♂️  =====>اي يا مزه عمله اي ؟",
        "👁👁\n  👱🏻‍♀️  =====> انا تمام",
        "👁👁\n  👱🏻‍♂️  =====> اي القمر ده🤤",
        "👁👁\n  👱🏻‍♀️  =====> اي مالك",
        "👁👁\n  👱🏻‍♂️  =====> مستغرب جمالك 🤤",
        "👁👁\n  👱🏻‍♀️  =====> بسسس ",
        "👁👁\n  👱🏻‍♂️  =====> متت 😹",
        "👁👁\n  👱🏻‍♀️  =====> لا تضحك",
        "👁👁\n  👱🏻‍♂️  =====> والله مستغرب بس 😹🤤",
        "👁👁\n  👱🏻‍♀️  =====> بس لتضحك😭😒",
        "👁👁\n  👱🏻‍♂️  =====> مححح🤤",
        "👁👁\n  👱🏻‍♀️  =====> متبوصش بس",
        "👁👁\n  👱🏻‍♂️  =====> دولي",
        "👁👁\n  👱🏻‍♂️  =====> ماشي بايي",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 10])
    await asyncio.sleep(animation_interval)

# == == == == == == == == == == == == == == == == == == == ==


@Client.on_message(filters.command("عبقري$", prefixes=f".") & filters.me)
async def abkary_1(c, msg):
    animation_interval = 0.05
    animation_ttl = range(288)
    animation_chars = [
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "دا افكر 🙁😹 ",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 36])

# == == == == == == == == == == == == == == == == == == == ==


@Client.on_message(filters.command("افعي$", prefixes=f".") & filters.me)
async def aph3a_1(c, msg):
    animation_interval = 0.3
    animation_ttl = range(27)
    animation_chars = [
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "‎◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◻️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◼️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◼️◻️◼️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 27])

# == == == == == == == == == == == == == == == == == == == ==



@Client.on_message(filters.command("ولد$", prefixes=f".") & filters.me)
async def man_1(c, msg):
    animation_interval = 0.5
    animation_ttl = range(16)
    animation_chars = [
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛🚗\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛🚗⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛🚗⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🚗⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛🚗⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛🚗⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n🚗⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬜⬜⬜😊⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛😊⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬜⬛⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛😊⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬜⬛⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬛⬜⬛\n⬛⬛⬜⬛⬛⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛😊⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬜⬛⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬛😊⬛⬜⬛\n⬛⬛⬜⬜⬜⬛⬛\n⬛⬛⬛⬜⬛⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛😊⬛⬛⬛\n⬛⬛⬜⬜⬜⬛⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬜⬜⬜😊⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 16])

# == == == == == == == == == == == == == == == == == == == ==



@Client.on_message(filters.command("مايكرو$", prefixes=f".") & filters.me)
async def micro_1(c, msg):
    animation_interval = 0.3
    animation_ttl = range(28)
    animation_chars = [
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◻️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◻️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◻️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◻️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◻️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◻️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◻️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◻️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◻️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◻️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◻️◼️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◻️◻️◻️◼️\n◼️◼️◼️◼️◼️",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 28])

# == == == == == == == == == == == == == == == == == == == ==



@Client.on_message(filters.command("فايروس$", prefixes=f".") & filters.me)
async def vayros_1(c, msg):
    animation_interval = 1
    animation_ttl = range(30)
    animation_chars = [
        "🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
        "◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
        "◼️◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
        "◼️◼️◼️️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
        "◼️◼️◼️◼️🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
        "‎◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎??🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎??🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️🔴🔵🌕♓♎⛎◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🔴🔵🌕♓♎⛎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️",
        "◼️◼️◼️\n◼️◼️◼️\n◼️◼️◼️",
        "◼️◼️\n◼️◼️",
        "◼️",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 30])

# == == == == == == == == == == == == == == == == == == == ==



@Client.on_message(filters.command("قطار$", prefixes=f".") & filters.me)
async def train_1(c, msg):
    animation_interval = 0.2
    animation_ttl = range(30)
    animation_chars = [
        "**ت**",
        "**تو**",
        "**توتت**",
        "**تووووت**",
        "**توووت**",
        "**تووووت**",
        "**توووووت**",
        "**توووووت**",
        "**توووووووووت**",
        "**توووووووووووت**",
        "**اجه القطار 🚅**",
        "**وخر عن  🚅🚃🚃**",
        "**تووووت 🚅🚃🚃🚃**",
        "**جبنها وجت ويانه 🚅🚃🚃🚃🚃**",
        "**جبناها وجت ويانه 🚅🚃🚃🚃🚃🚃**",
        "**مطر 🚅🚃🚃🚃🚃🚃🚃**",
        "**بيباي 🚅🚃🚃🚃🚃🚃🚃🚃**",
        "**🚅🚃🚃🚃🚃🚃🚃🚃🚃**",
        "**🚅🚃🚃🚃🚃🚃🚃🚃🚃🚃**",
        "🚅🚃🚃🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃",
        "🚃🚃🚃",
        "🚃🚃",
        "🚃",
        "**مو قطار ضيم**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 30])

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("مصه$", prefixes=f".") & filters.me)
async def tikol_1(c, msg):
    animation_interval = 0.5
    animation_ttl = range(6)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(f"** ⣠⡶⠚⠛⠲⢄⡀\n⣼⠁      ⠀⠀⠀⠳⢤⣄\n⢿⠀⢧⡀⠀⠀⠀⠀⠀⢈⡇\n⠈⠳⣼⡙⠒⠶⠶⠖⠚⠉⠳⣄\n⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄\n⠀⠀⠀⠘⣆       ⠀⠀⠀⠀⠀⠈⠓⢦⣀\n⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⢤\n⠀⠀⠀⠀⠀⠀⠙⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧\n⠀⠀⠀⠀⠀⠀⠀    ⠓⠦⠀⠀⠀⠀**\n**🚹 ¦ 😂 **  ✷ بقولك يا  {get_name(msg.reply_to_message)} \nتعالي مصه يا لطخ")

# == == == == == == == == == == == == == == == == == == == ==


@Client.on_message(filters.command("موسيقى$", prefixes=f".") & filters.me)
async def music_1(c, msg):
    animation_interval = 1.5
    animation_ttl = range(11)
    animation_chars = [
        "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:00** ▱▱▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀ `🔂` `⏮️` `⏪️` `▶️` `⏩️` `⏭️`\n\n**الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",
        "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:01** ▰▱▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀ `🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",
        "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:02** ▰▰▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",
        "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:03** ▰▰▰▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀ `🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀ [مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:04** ▰▰▰▰▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n** الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:05** ▰▰▰▰▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n** الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:06** ▰▰▰▰▰▰▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n** الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:07** ▰▰▰▰▰▰▰▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n** الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:08** ▰▰▰▰▰▰▰▰▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n** الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:09** ▰▰▰▰▰▰▰▰▰▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n** الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[مشغل موسيقى](tg://user?id=916234223)\n\n⠀⠀⠀⠀**التشغيل الآن : شكل**\n\n**00:10** ▰▰▰▰▰▰▰▰▰▰ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏺️` `⏩️` `⏭️`\n\n** الأغنية التالية : ساجدة عبيد لطك روحي بحديدة **",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 11])

# == == == == == == == == == == == == == == == == == == == ==



@Client.on_message(filters.command("رسم$", prefixes=f".") & filters.me)
async def pain_1(c, msg):
    await asyncio.sleep(1)
    await msg.edit("╔═══════════════════╗ \n \t░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await msg.edit("╔═══════════════════╗ \n ░ \t░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await msg.edit("╔═══════════════════╗ \n ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await msg.edit("╔═══════════════════╗ \n ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await msg.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await msg.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await msg.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await msg.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await msg.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )
    await asyncio.sleep(1)
    await msg.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )
    await asyncio.sleep(1)
    await msg.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )
    await asyncio.sleep(1)
    await msg.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )
    await asyncio.sleep(1)
    await msg.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )
    await asyncio.sleep(1)
    await msg.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )

# == == == == == == == == == == == == == == == == == == == ==



@Client.on_message(filters.command("نجمه$", prefixes=f".") & filters.me)
async def star_1(c, msg):
    deq = deque(list("🦋✨🦋✨🦋✨🦋✨"))
    for _ in range(48):
        await asyncio.sleep(0.3)
        await msg.edit("".join(deq))
        deq.rotate(1)

# == == == == == == == == == == == == == == == == == == == ==



@Client.on_message(filters.command("مكعبات$", prefixes=f".") & filters.me)
async def mq3bat_1(c, msg):
    deq = deque(list("🟥🟧🟨🟩🟦🟪🟫⬛⬜"))
    for _ in range(50):
        await asyncio.sleep(0.3)
        await msg.edit("".join(deq))
        deq.rotate(1)

# == == == == == == == == == == == == == == == == == == == ==


@Client.on_message(filters.command("مطر$", prefixes=f".") & filters.me)
async def rain_1(c, msg):
    msg = await c.send_message(msg.chat.id, "`مطر.......`")
    deq = deque(list("🌬☁️🌩🌨🌧🌦🌥⛅🌤"))
    for _ in range(48):
        await asyncio.sleep(0.3)
        await msg.edit("".join(deq))
        deq.rotate(1)

# == == == == == == == == == == == == == == == == == == == ==# == == == == == == == == == == == == == == == == == == == ==


@Client.on_message(filters.command("تفريغ$", prefixes=f".") & filters.me)
async def tafreq_1(c, msg):
    # try:
    #     obj = msg.pattern_match.group(1)
    #     if len(obj) != 3:
    #         return await msg.edit("`Input length must be 3 or empty`")
    #     inp = " ".join(obj)
    # except IndexError:
    #     inp = "🥞 🎂 🍫"
    inp = "🥞 🎂 🍫"
    u, t, g, o, s, n = inp.split(), "🗑", "<(^_^ <)", "(> ^_^)>", "⠀ ", "\n"
    h = [(u[0], u[1], u[2]), (u[0], u[1], ""), (u[0], "", "")]
    for something in reversed(
            [
                y
                for y in (
                    [
                        "".join(x)
                        for x in (
                            f + (s, g, s + s * f.count(""), t),
                            f + (g, s * 2 + s * f.count(""), t),
                            f[:i] + (o, f[i], s * 2 + s * f.count(""), t),
                            f[:i] + (s + s * f.count(""), o, f[i], s, t),
                            f[:i] + (s * 2 + s * f.count(""), o, f[i], t),
                            f[:i] + (s * 3 + s * f.count(""), o, t),
                            f[:i] + (s * 3 + s * f.count(""), g, t),
                    )
                    ]
                    for i, f in enumerate(reversed(h))
            )
            ]
    ):
        for something_else in something:
            await asyncio.sleep(0.3)
            await msg.edit(something_else)

# == == == == == == == == == == == == == == == == == == == ==



@Client.on_message(filters.command("فليم$", prefixes=f".") & filters.me)
async def film_1(c, msg):
    animation_interval = 1
    animation_ttl = range(10)
    animation_chars = [
        "⬛⬛⬛\n⬛⬛⬛\n⬛⬛⬛",
        "⬛⬛⬛\n⬛🔄⬛\n⬛⬛⬛",
        "⬛⬆️⬛\n⬛🔄⬛\n⬛⬛⬛",
        "⬛⬆️↗️\n⬛🔄⬛\n⬛⬛⬛",
        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛⬛",
        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛↘️",
        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬇️↘️",
        "⬛⬆️↗️\n⬛🔄➡️\n↙️⬇️↘️",
        "⬛⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",
        "↖️⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",
    ]
    await asyncio.sleep(2)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 10])


love = [
    """
█▀███▀▀███▀▀███▀▀███▀▀███▀█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
█▒▒█▒▒▒▒▒███▒▒█▒▒▒█▒█████▒█
█▒▒█▒▒▒▒█▒▒▒█▒█▒▒▒█▒█▒▒▒▒▒█
█▒▒█▒▒▒▒█▒▒▒█▒▒█▒█▒▒█████▒█
█▒▒█▒▒▒▒█▒▒▒█▒▒█▒█▒▒█▒▒▒▒▒█
█▒▒████▒▒███▒▒▒▒█▒▒▒█████▒█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
█▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒█
█▒▒▒▒▒▒▒█──█▒████▒█──█▒▒▒▒█
█▒▒▒▒▒▒█──█─█────█─█──█▒▒▒█
█▒▒▒▒▒▒█─██───────███─█▒▒▒█
█▒▒▒▒▒▒█──────────────█▒▒▒█
█▒▒▒▒▒▒▒█────────────█▒▒▒▒█
█▒▒▒▒██▒▒█──██───██──█▒▒▒▒█
█▒▒▒█──█▒█──██───██──█▒▒▒▒█
█▒▒▒█──█▒█────███────█▒▒▒▒█
█▒▒▒█──█▒█───█───█──█▒▒▒▒▒█
█▒▒▒▒█──█─█───███──█▒▒▒▒▒▒█
█▒▒▒▒▒█────██────██▒▒▒▒▒▒▒█
█▒▒▒▒▒█──────████─██▒▒▒▒▒▒█
█▒▒▒▒▒▒█───────────█▒▒▒▒▒▒█
█▒▒▒▒▒▒▒███─────────█▒▒▒▒▒█
█▒▒▒▒▒▒▒▒▒█──────█───█▒▒▒▒█
█▒▒▒▒███▒▒█───────█───█▒▒▒█
█▒▒▒█──████─────████───█▒▒█
█▒▒▒█────█─────█────█─█▒▒▒█
█▒▒▒█─────█────█────██▒▒▒▒█
█▒▒▒█──────█───█──────█▒▒▒█
█▒▒▒▒█─────██████─────█▒▒▒█
█▒▒▒▒▒█──███▒▒▒▒█─────█▒▒▒█
█▒▒▒▒▒▒██▒▒▒▒▒▒▒▒█───█▒▒▒▒█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒█
█▒▒▒▒█▒▒▒▒█▒▒███▒▒█▒▒▒█▒▒▒█
█▒▒▒▒▒█▒▒█▒▒█▒▒▒█▒█▒▒▒█▒▒▒█
█▒▒▒▒▒▒██▒▒▒█▒▒▒█▒█▒▒▒█▒▒▒█
█▒▒▒▒▒▒█▒▒▒▒█▒▒▒█▒█▒▒▒█▒▒▒█
█▒▒▒▒▒█▒▒▒▒▒▒███▒▒▒███▒▒▒▒█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
█▄▄█▄▄██▄▄█▄▄█▄▄█▄▄██▄▄█▄▄█
""",
    """
╔══╗
╚╗╔╝
╔╝(¯`v´¯)
╚══`.¸.YOU
""",
    """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░▄▄▄▄▄▄░░░░▄▄▄░░░░▄▄▄░░░░░░
░░░▀████▀░░▄█████▄▄█████▄░░░░
░░░░░██░░░████████████████░░░
░░░░░██░░░████████████████░░░
░░░░░██░░░▀██████████████▀░░░
░░░░▄██▄░░░░▀██████████▀░░░░░
░░░██████░░░░░▀██████▀░░░░░░░
░░░░░░░░░░░░░░░░▀██▀░░░░░░░░░
░░░░░░░░░░░░░▄▄░░░░░░░░░░░░░░
░░▀███░███▀▄█▀▀█▄░▀██▀░▀██▀░░
░░░░▀█▄█▀░▄█░░░░█▄░██░░░██░░░
░░░░░░█░░░██░░░░██░██░░░██░░░
░░░░░░█░░░░█▄░░▄█░░██░░░██░░░
░░░░▄███▄░░░▀██▀░░░░▀███▀░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
""",
    """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░▄▄▄░░░░▄███▄▄███▄░░░░░░▄░░▄░░░░░░░░
░░░░█░░░░░██████████░░░░░░█░░█░░░░░░░░
░░░░█░░░░░░▀██████▀░░░░░░░█░░█░░░░░░░░
░░░▀▀▀░░░░░░░▀██▀░░░░░░░░░░▀▀░░░░░░░░░
░░░░░░░░░░░░▄░░░░░█░▄▀░░▄░░░░░░░░░░░░░
░░░░░░░░▄░░░▀▄▄▄▀█▀▀█▀▀▄█▄░█░░░░░░░░░░
░░░░░░░░░▀▄▄▀█░░░▀░░░░░░░░█▄░▄▀▀░░░░░░
░░░░░▀▀▄░█▀░░░░░░░░░▄▄▄▄▄▄░▀█░░░░░░░░░
░░░░░░▄▀▀░▄▄▀▀▀▄░░▄█▀░░░░▀▄░▄█▀▀▀▄░░░░
░░░▄▄██░░█░░░░░░█░█░░███░▄▀░░░██░█░░░░
░░█░▄█░░░█░███░▄▀░▀▀▄███▀░░░░░██░█░░░░
░░█░▀█▄░░▀▄███▄▀░░░░░░░░░░░░░▄█▄▀░░░░░
░░░▀▀▀▀█░░░░░░░░░░░░░░░▄█▀░░▄▀░░░░▄░░░
░░░░▄░░░▀▄░▀▀▄▄░░░░░▄▄▀▀░░▄▀░░░░▄█▀░░░
░░▄▄█▄░░░░▀▀▄▄░▀▀▀▀▀░▄▄▄▀▀░░▄▄▀▀▀█▀▀░░
░░▄█▀▀▀▀▄▄▄▄░░▀▀▀▀▀█▀░░░▄▄▀▀░░░░░░▀░░░
░░░░░░░░░░░░▀▀▀▀▀▄▄█▄▄▀▀░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░▀░░░░░░░░░░░░░░░░░░
""",
    """
────╪███████╪────╪███████
──╪███████████╪╪███████████
──██████████████████████████
─████████████████████████████
─████████████████████████████
─████████████████████████████
─████████████████████████████
──██████████████████████████
──╪████████████████████████
───╪██████████████████████
─────████████████████████
──────╪████████████████
────────╪████████████
──────────╪████████
─────────────╪██
████─╪███╪╪████████──████─████
╪███─╪███─████╪████──████─████
─███─╪███─████─╪███╪─████─████
─███╪╪██╪─████─╪███╪─████─████
─╪██████──████─╪███╪─████─████
──██████──████─╪███╪─████─████
──█████╪──████─╪███╪─████─████
──╪████───████─╪███╪─████─████
───████───████─╪███╪─████─████
──╪████───████─╪███╪─████─████
──╪████───████─╪███╪─████─████
──╪████───████─╪███╪─████─████
──╪████───█████████──█████████
───████────███████╪──╪███████
""",
    """
───▄▄▄▄▄▄─────▄▄▄▄▄▄
─▄█▓▓▓▓▓▓█▄─▄█▓▓▓▓▓▓█▄
▐█▓▓▒▒▒▒▒▓▓█▓▓▒▒▒▒▒▓▓█▌
█▓▓▒▒░╔╗╔═╦═╦═╦═╗░▒▒▓▓█
█▓▓▒▒░║╠╣╬╠╗║╔╣╩╣░▒▒▓▓█
▐█▓▓▒▒╚═╩═╝╚═╝╚═╝▒▒▓▓█▌
─▀█▓▓▒▒░░░░░░░░░▒▒▓▓█▀
───▀█▓▓▒▒░░░░░▒▒▓▓█▀
─────▀█▓▓▒▒░▒▒▓▓█▀
──────▀█▓▓▒▓▓█▀
────────▀█▓█▀
──────────▀
""",
    """
░███████░
░█╬╬╬╬╬█░
░██╬╬███░
░██╬╬███░
░██╬╬███░
░█╬╬╬╬╬█░
░███████░
░███████░
░███████░
░███████░
░█╬╬████░
░█╬╬████░
░█╬╬████░
░█╬╬████░
░█╬╬╬╬╬█░
░███████░
░█╬╬╬╬╬█░
░█╬███╬█░
░█╬███╬█░
░█╬███╬█░
░█╬╬╬╬╬█░
░███████░
░█╬╬█╬╬█░
░█╬╬█╬╬█░
░█╬╬█╬╬█░
░█╬╬█╬╬█░
░██╬╬╬██░
░███████░
░█╬╬╬╬╬█░
░█╬╬████░
░█╬╬╬╬██░
░█╬╬████░
░█╬╬╬╬╬█░
░███████░
░███████░
░███████░
░███████░
░███████░
░█╬╬█╬╬█░
░█╬╬█╬╬█░
░██╬╬╬██░
░██╬╬╬██░
░██╬╬╬██░
░███████░
░█╬╬╬╬╬█░
░█╬███╬█░
░█╬███╬█░
░█╬███╬█░
░█╬╬╬╬╬█░
░███████░
░█╬███╬█░
░█╬███╬█░
░█╬███╬█░
░█╬███╬█░
░█╬╬╬╬╬█░
░███████░
""",
    '''
                /'    `\./'    `\
               (  o  o  |  u  u  )
               ;`.  V  /"\  V  .';
       """"\."     __ ) ( __     "./""""/
        \   ;     aP""Y,_,P""Ya     ;   /
         `,; ._  d'    `"'    `b  _. ;,'
      ,,,,aaaaaa.8,  I  Love  ,8.aaaaaa,,,,
      I8\\\\\\\\\`Y,   You   ,P'/////////8I
       "Ya\\\\\\\\\"Y,     ,P"/////////aY"
         "Ya\\\\\\\\\"Y,_,P"/////////aP"
           `"Ya\\\\\\\\`Y'////////aP"'
              `"""""""""""""""""""'
''',
    """
                         %%%%%%%%%%%%%
                         %%%%%%%%%%%%%
                             %%%%%
                             %%%%%
                             %%%%%
                             %%%%%
                             %%%%%
                             %%%%%
                             %%%%%
                         %%%%%%%%%%%%%
                         %%%%%%%%%%%%%




  ::::          ::::::      ::::      ::::    :::::::::
  ::::        ::::  ::::    ::::      ::::    :::::::::
  ::::       ::::    ::::   ::::      ::::    ::::
  ::::       ::::    ::::    ::::    ::::     ::::::::
  ::::       ::::    ::::     ::::  ::::      ::::
  ::::       ::::    ::::      ::::::::       ::::
  ::::::::::  ::::  ::::        ::::::        :::::::::
  ::::::::::    ::::::           ::::         :::::::::


                   Y O U
""",
    """
           ..//``~~~~~-=+=-=+~~~~\\.      .//~~~~=-=+=-~~~~~''\\..
       ..//=+=-=+=-=+=-=+=-=+=-=+=-\\    //=+=-=+=-=+=-=+=-=+=-=+=\\..
      //+=-=+=-=+=-=+=-=+=-=+=-=+=-=+\\//=-=+=-=+=-=+=-=+=-=+=-=+=-=+\\
    //-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-\\
   ++=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=++
   ||~~\    /~~~\/~~~\   /~~~\/~~~\   /~~~\/~~~\   /~~~\/~~~\   /~~~\/~~||
   ||  /    \        /   \        /   \        /   \        /   \       ||
   ||/        \    /       \    /       \    /       \    /       \    /||
   ||           \/           \/           \/           \/           \/  ||
   ++=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=++
    \\-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=//
      `\\=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+//'
        |`\\+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=//'
        |   `\\=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=//''
        |      ``\\=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=//''
   _____|_____     ``\\=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=//''     
  |   I Love  |        ``\\=+=-=+=-=+=-=+=-=+=-=+=//''
  |    You.   |            ``\\=+=-=+=-=+=-=+=//''
  |   * HUG*  |                ``\\=+=-=+=//''
   ~~~~~~~~~~~                     ``\\//''
""",
    """
                  IIIIIIIIIII
                  IIIIIIIIIII
                      III
                      III
                      III
                      III
                      III
                  IIIIIIIIIII
                  IIIIIIIIIII

LLL          OOOOOOOO    VV       VV  EEEEEEEEEE
LLL         OOOOOOOOOO   VV       VV  EEEEEEEEEE
LLL         OO      OO   VV       VV  EE
LLL         OO      OO   VV       VV  EE
LLL         OO      OO   VV       VV  EEEEEEE
LLL         OO      OO    VV     VV   EE
LLL         OO      OO     VV   VV    EE
LLLLLLLLLL  OOOOOOOOOO      VV VV     EEEEEEEEEE
LLLLLLLLLL   OOOOOOOO         V       EEEEEEEEEE

        YY      YY   OOOOOOOO   UUU    UUU
         YY    YY   OOOOOOOOOO  UUU    UUU
          YY  YY    OO      OO  UUU    UUU
           YYYY     OO      OO  UUU    UUU
            YY      OO      OO  UUU    UUU
            YY      OO      OO  UUU    UUU
            YY      OO      OO  UUU    UUU
            YY      OOOOOOOOOO  UUUUUUUUUU
            YY       OOOOOOOO    UUUUUUUU
""",
    """
██─▄███▄███▄─██▄──▄██──▄███▄──██──██
██─█████████──▀████▀──██▀─▀██─██──██
██──▀█████▀─────██────██▄─▄██─██──██
██────▀█▀───────██─────▀███▀──▀████
""",
    '''
‎_/)______./¯"""/') ___/)___/)__,-----------’)_⌔ ___/)_/)__./¯/)/)
¯¯\)¯¯¯¯¯'\_„„„„\) ¯\)¯¯¯¯¯\)¯¯‘-----------.)¯⌔ ¯\)¯¯¯¯\)¯'\_\)\)
██░░░██░░░░▄███▄░░██░░░██░████░░░██░░██
██░░░██░░░██▀░▀██░██▄░▄██░██▄░░░░██░░██
██░░░██░░░██▄░▄██░░██▄██░░██▀░░░░██░░██
██░░░████░░▀███▀░░░░███░░░████░░░▀████▀
_/)______./¯"""/') ___/)___/)__,-----------’)_⌔ ___/)_/)__./¯/)/)
¯¯\)¯¯¯¯¯'\_„„„„\) ¯\)¯¯¯¯¯\)¯¯‘-----------.)¯⌔ ¯\)¯¯¯¯\)¯'\_\)\)
''',
    """
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒░░░░░░═░░▒▒▒▒░░░░░░▒▒▒░░░░═░▒▒▒▒▒▒
▒▒▒▒▒▒░████████▓░▒▒░░█████░══█████▓═░▒▒▒▒
▒▒▒▒▒░▓█████████░▒░█████████████████░▒▒▒▒
▒▒▒▒▒▒░░░▒███░▒░▒░▒██████████████████═▒▒▒
▒▒▒▒▒▒▒░░═███═░▒▒░███████████████████░▒▒▒
▒▒▒▒▒▒▒▒▒░███░▒▒▒░███████████████████░▒▒▒
▒▒▒▒▒▒▒▒▒░███═▒▒▒░▒██████████████████░▒▒▒
▒▒▒▒▒▒▒▒▒░███░▒▒▒▒═█████████████████═▒▒▒▒
▒▒▒▒▒▒▒▒▒░███░▒▒▒▒▒─███████████████░░▒▒▒▒
▒▒▒▒▒▒▒▒░═███═░▒▒▒▒▒─█████████████═░▒▒▒▒▒
▒▒▒▒▒▒░░░▒███░▒░▒▒▒▒▒░░█████████▒═▒▒▒▒▒▒▒
▒▒▒▒▒░▒█████████═▒▒▒▒▒░═░█████▒═░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒░████████▒░▒▒░░░▒▒░═░▓▒═░▒▒▒▒░▒▒▒▒▒
▒▒▒▒▒▒░░░░░░░░░░▒▒░░░░░░░▒░░═░░░░░░░░░▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░█████████─██████████░▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░█████████═▒████████░░▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░─███▒─▒░─███░═░░░▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒─███▒░─███░░▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒─███═███▒░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒─█████▒░▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒─████═▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░███═▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░─███═══░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░█████████▒░▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░█████████▓░▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░──────═░░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░═▓█████▒═░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒═▒█████████░░▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒═█████░░░████▒░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░███═░░▒░═░███═▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒═███░░▒▒▒▒▒░▓███░▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░███═▒▒▒▒▒▒░░███░▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░███░░▒▒▒▒▒░▒███░▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒███─░▒▒░░═███░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒═████▒══░▓████░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒─██████████▓═▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░███████═░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░═───░───═░░░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▓██████─███████░▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░███████─███████░▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒═▒███░░▒░░████─▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░███═░▒▒░▒██▒░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒███░▒▒▒░▓██▓░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒███░▒▒▒░▓██▓░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒███░▒▒▒░▒███░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒███─░▒░═███▓░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒═████░░░████═▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒─█████████═▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒═▒█████▓─▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░═░░▒▒▒▒▒▒▒▒▒▒
""",
    """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░▄▄▄▄▄▄░░░░░░░░░▄▄▄▄▄▄░░░░░░░░
░░░░▄▄▄▄░░░░▄▄▄▄░░░▄▄▄▄░░░░▄▄▄▄░░░░░
░▄▄▄▄░░░░░░░░░░░▄░▄░░░░░░░░░░░▄▄▄▄░░
▄▄░░░░░░░░░░░░░░░▄░░░░░░░░░░░░░░░▄▄░
▄▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄░
▄▄░▐█▀▀██▀▀▀█▀█▀█▀▀█▄▄▄▄▄▄▄▄▄▄▄▄░▄▄░
▄▄░▐█──██─█─█─█─█─▀█─█─█─█▀█─█─█░▄▄░
▄▄░▐█──██─▀─█▄─▄█─▀█──█──█▄█─█▄█░▄▄░
▄▄░▐█▄▄▄█▀▀▀▀▀▀▀▀▀▀▀████████████░▄▄░
░▄▄▄▄░░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄░░
░░░▄▄▄▄░░░░░░░░░░░░░░░░░░░░░▄▄▄▄░░░░
░░░░░░▄▄▄▄░░░░░░░░░░░░░░░▄▄▄▄░░░░░░░
░░░░░░░░░▄▄▄▄░░░░░░░░░▄▄▄▄░░░░░░░░░░
░░░░░░░░░░░░▄▄▄▄░░░▄▄▄▄░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▄▄▄▄▄░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▄▄▄░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░▄░░░░░░░░░░░░░░░░░░
""",
]

# == == == == == == == == == == == == == == == == == == == ==



@Client.on_message(filters.command("طائره$", prefixes=f".") & filters.me)
async def plan_1(c, msg):
    msg = await c.send_message(msg.chat.id, "انتظر الطائره...")
    await msg.edit("✈-------------")
    await msg.edit("-✈------------")
    await msg.edit("--✈-----------")
    await msg.edit("---✈----------")
    await msg.edit("----✈---------")
    await msg.edit("-----✈--------")
    await msg.edit("------✈-------")
    await msg.edit("-------✈------")
    await msg.edit("--------✈-----")
    await msg.edit("---------✈----")
    await msg.edit("----------✈---")
    await msg.edit("-----------✈--")
    await msg.edit("------------✈-")
    await msg.edit("-------------✈")
    await asyncio.sleep(3)

# == == == == == == == == == == == == == == == == == == == ==


@Client.on_message(filters.command("شرطه$", prefixes=f".") & filters.me)
async def offeser_1(c, msg):
    if not msg.reply_to_message:
        return
    animation_interval = 0.3
    animation_ttl = range(12)
    mention = (await c.get_users(msg.reply_to_message.from_user.id)).mention
    animation_chars = [
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴??\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        f"{mention} **Police iz Here**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 12])

# == == == == == == == == == == == == == == == == == == == ==



@Client.on_message(filters.command("اذكار الصباح$", prefixes=f".") & filters.me)
async def jio_2(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
#اذكار_الصباح
«أعُوذُ بِكَلِمَاتِ اللهِ التَّامَّاتِ مِنْ شَرِّ مَا خَلَقَ»

- ٣ مرَّات.

-----------------------‐

«اللَّهُمَّ بِكَ أمْسَيْنَا ، وَبِكَ أصْبَحْنَا ، وَبِكَ نَحْيَا ، وَبِكَ نَمُوتُ ، وَإلَيْكَ المَصِيرُ»

-----------------------‐

«اللَّهُمَّ مَا أمْسَى بِي مِنْ نِعْمَةٍ أوْ بِأحَدٍ مِنْ خَلْقِكَ فَمِنْكَ وَحْدَكَ لَا شَرِيكَ لَكَ ، فَلَكَ الحَمْدُ وَلَكَ الشُّكْرُ»

-----------------------‐

«اللَّهُمَّ إنِّي أمْسَيْتُ أُشْهِدُكَ ، وَأُشْهِدُ حَمَلَةَ عَرْشِكَ ، وَمَلَائِكَتَكَ ، وَجَمِيعَ خَلْقِكَ ، أنَّكَ أنْتَ اللهُ لَا إلَهَ إلَّا أنْتَ وَحْدَكَ لَا شَرِيكَ لَكَ ، وَأنَّ مُحَمَّدًا عَبْدُكَ وَرَسُولُكَ»

- ٤ مرَّات.

-----------------------‐

«أمْسَيْنَا وَأمْسَى المُلْكُ للهِ رَبِّ العَالَمِينَ ،
اللَّهُمَّ إنِّي أسْألُكَ خَيْرَ هَذِهِ اللَّيْلَةِ ، فَتْحَهَا ، وَنَصْرَهَا ، وَنُورَهَا ، وَبَرَكَتَهَا ، وَهُدَاهَا ، وَأعُوذُ بِكَ مِنْ شَرِّ مَا فِيهَا وَشَرِّ مَا بَعْدَهَا»

-----------------------‐

«أمْسَيْنَا عَلَى فِطْرَةِ الإسْلَامِ ، وَعَلَى كَلِمَةِ الإخْلَاصِ ، وَعَلَى دِينِ نَبِيِّنَا مُحَمَّدٍ صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ ، وَعَلَى مِلَّةِ أبِينَا إبْرَاهِيمَ ، حَنِيفًا مُسْلِمًا وَمَا كَانَ مِنَ المُشْرِكِينَ»

-----------------------‐

«أمْسَيْنَا وأمْسَى المُلْكُ للهِ والحَمْدُ للهِ ، لَا إلَهَ إلَّا اللهُ وَحْدَهُ لَا شَرِيكَ لَهُ ، لَهُ المُلْكُ وَلَهُ الحَمْدُ وَهُوَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ ،
رَبِّ أسْألُكَ خَيْرَ مَا فِي هَذِهِ اللَّيْلَةِ وَخَيْرَ مَا بَعْدَهَا ، وَأعُوذُ بِكَ مِنْ شَرِّ مَا فِي هَذِهِ اللَّيْلةِ وَشَرِّ مَا بَعْدَهَا ،
رَبِّ أعُوذُ بِكَ مِنَ الكَسَلِ وَسُوءِ الكِبَرِ ، رَبِّ أعُوذُ بِكَ مِنْ عَذَابٍ فِي النَّارِ وَعَذَابٍ فِي القَبْرِ» .
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])
        
        
        

# == == == == == == == == == == == == == == == == == == == ==
@Client.on_message(filters.command("اذكار المساء$", prefixes=f".") & filters.me)
async def jio_1(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
"""
#اذكار_المساء
«الحَمْدُ للهِ وَحْدَهُ ، وَالصَّلَاةُ وَالسَّلَامُ عَلَى مَنْ لَا نَبِيَّ بَعْدَهُ»

-----------------------‐

بِسْمِ اللهِ الرَّحْمَنِ الرَّحِيمِ :

﴿اللهُ لَا إِلَهَ إِلَّا هُوَ الْحَيُّ الْقَيُّومُ لَا تَأْخُذُهُ سِنَةٌ وَلَا نَوْمٌ لَّهُ مَا فِي السَّمَاوَاتِ وَمَا فِي الْأَرْضِ مَن ذَا الَّذِي يَشْفَعُ عِندَهُ إِلَّا بِإِذْنِهِ يَعْلَمُ مَا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ وَلَا يُحِيطُونَ بِشَيْءٍ مِّنْ عِلْمِهِ إِلَّا بِمَا شَاءَ وَسِعَ كُرْسِيُّهُ السَّمَاوَاتِ وَالْأَرْضَ وَلَا يَئُودُهُ حِفْظُهُمَا وَهُوَ الْعَلِيُّ الْعَظِيمُ﴾

-----------------------‐

بِسْمِ اللهِ الرَّحْمَنِ الرَّحِيمِ :

﴿قُلْ هُوَ اللهُ أَحَدٌ ۝ اللهُ الصَّمَدُ ۝ لَمْ يَلِدْ وَلَمْ يُولَدْ ۝ وَلَمْ يَكُن لَّهُ كُفُوًا أَحَدٌ﴾

بِسْمِ اللهِ الرَّحْمَنِ الرَّحِيمِ :

﴿قُلْ أَعُوذُ بِرَبِّ الفَلَقِ ۝ مِن شَرِّ مَا خَلَقَ ۝ وَمِن شَرِّ غَاسِقٍ إِذَا وَقَبَ ۝ وَمِن شَرِّ النَّفَّاثَاتِ فِي العُقَدِ ۝ وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ﴾

بِسْمِ اللهِ الرَّحْمَنِ الرَّحِيمِ :

﴿قُلْ أَعُوذُ بِرَبِّ النَّاسِ ۝ مَلِكِ النَّاسِ ۝ إِلَهِ النَّاسِ ۝ مِن شَرِّ الوَسْوَاسِ الخَنَّاسِ ۝ الَّذِي يُوَسْوِسُ فِي صُدُورِ النَّاسِ ۝ مِنَ الجِنَّةِ وَالنَّاسِ﴾

-----------------------‐

«أصْبَحْنَا وَأصْبَحَ المُلْكُ للهِ والحَمْدُ للهِ ، لَا إلهَ إلَّا اللهُ وَحْدَهُ لَا شَرِيكَ لَهُ ، لَهُ المُلْكُ وَلَهُ الحَمْدُ وَهُوَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ ،
رَبِّ أسْألُكَ خَيْرَ مَا فِي هَذَا اليَوْمِ وَخَيْرَ مَا بَعْدَهُ ، وَأعُوذُ بِكَ مِنْ شَرِّ مَا فِي هَذَا اليَوْمِ وَشَرِّ مَا بَعْدَهُ ،
رَبِّ أعُوذُ بِكَ مِنَ الكَسَلِ وَسُوءِ الكِبَرِ ، رَبِّ أعُوذُ بِكَ مِنْ عَذَابٍ فِي النَّارِ وعَذَابٍ فِي القَبْرِ»

- وإذا أمسى يقول :

«أمْسَيْنَا وأمْسَى المُلْكُ للهِ والحَمْدُ للهِ ، لَا إلهَ إلَّا اللهُ وَحْدَهُ لَا شَرِيكَ لَهُ ، لَهُ المُلْكُ وَلَهُ الحَمْدُ وَهُوَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ ،
رَبِّ أسْألُكَ خَيْرَ مَا فِي هَذِهِ اللَّيْلَةِ وَخَيْرَ مَا بَعْدَهَا ، وَأعُوذُ بِكَ مِنْ شَرِّ مَا فِي هَذِهِ اللَّيْلةِ وَشَرِّ مَا بَعْدَهَا ،
رَبِّ أعُوذُ بِكَ مِنَ الكَسَلِ وَسُوءِ الكِبَرِ ، رَبِّ أعُوذُ بِكَ مِنْ عَذَابٍ فِي النَّارِ وَعَذَابٍ فِي القَبْرِ»

-----------------------‐

«اللَّهُمَّ بِكَ أصْبَحْنَا ، وَبِكَ أمْسَيْنَا ، وَبِكَ نَحْيَا ، وَبِكَ نَمُوتُ ، وَإلَيْكَ النُّشُورُ»

- وإذا أمسى يقول :

«اللَّهُمَّ بِكَ أمْسَيْنَا ، وَبِكَ أصْبَحْنَا ، وَبِكَ نَحْيَا ، وَبِكَ نَمُوتُ ، وَإلَيْكَ المَصِيرُ»

-----------------------‐

«اللَّهُمَّ أنْتَ رَبِّي لَا إلَهَ إلَّا أنْتَ ،
خَلَقْتَنِي وَأنَا عَبْدُكَ ، وَأنَا عَلَى عَهْدِكَ وَوَعْدِكَ مَا اسْتَطَعْتُ ، أعُوذُ بِكَ مِنْ شَرِّ مَا صَنَعْتُ ،
أبُوءُ لَكَ بِنِعْمَتِكَ عَلَيَّ ، وَأبُوءُ بِذَنْبِي فَاغْفِرْ لِي ؛ فَإنَّهُ لَا يَغْفِرُ الذُّنُوبَ إلَّا أنْتَ»

-----------------------‐

«اللَّهُمَّ إنِّي أصْبَحْتُ أُشْهِدُكَ ، وَأُشْهِدُ حَمَلَةَ عَرْشِكَ ، وَمَلائِكَتَكَ ، وَجَمِيعَ خَلْقِكَ ، أنَّكَ أنْتَ اللهُ لَا إلَهَ إلَّا أنْتَ وَحْدَكَ لَا شَرِيكَ لَكَ ، وَأنَّ مُحَمَّدًا عَبْدُكَ وَرَسُولُكَ»

- ٤ مرَّات.

- وإذا أمسى يقول :

«اللَّهُمَّ إنِّي أمْسَيْتُ أُشْهِدُكَ ، وَأُشْهِدُ حَمَلَةَ عَرْشِكَ ، وَمَلائِكَتَكَ ، وَجَمِيعَ خَلْقِكَ ، أنَّكَ أنْتَ اللهُ لَا إلَهَ إلَّا أنْتَ وَحْدَكَ لَا شَرِيكَ لَكَ ، وَأنَّ مُحَمَّدًا عَبْدُكَ وَرَسُولُكَ»

- ٤ مرَّات.

-----------------------‐

«اللَّهُمَّ مَا أصْبَحَ بِي مِنْ نِعْمَةٍ أوْ بِأحَدٍ مِنْ خَلْقِكَ فَمِنْكَ وَحْدَكَ لَا شَرِيكَ لَكَ ، فَلَكَ الحَمْدُ وَلَكَ الشُّكْرُ»

- وإذا أمسى يقول :

«اللَّهُمَّ مَا أمْسَى بِي مِنْ نِعْمَةٍ أوْ بِأحَدٍ مِنْ خَلْقِكَ فَمِنْكَ وَحْدَكَ لَا شَرِيكَ لَكَ ، فَلَكَ الحَمْدُ وَلَكَ الشُّكْرُ»

-----------------------‐

«اللَّهُمَّ عَافِنِي فِي بَدَنِي ، اللَّهُمَّ عَافِنِي فِي سَمْعِي ، اللَّهُمَّ عَافِنِي فِي بَصَرِي ، لَا إلَهَ إلَّا أنْتَ ،
اللَّهُمَّ إنِّي أعُوذُ بِكَ مِنَ الكُفْرِ وَالفَقْرِ ، وَأعُوذُ بِكَ مِنْ عَذَابِ القَبْرِ ، لَا إلَهَ إلَّا أنْتَ»

- ٣ مرَّات.
"""
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])

@Client.on_message(filters.command("النظام الشمسي$", prefixes=f".") & filters.me)
async def sun_sys_1(c, msg):
    animation_interval = 0.1
    animation_ttl = range(80)
    animation_chars = [
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 8])

# == == == == == == == == == == == == == == == == == == == ==


@Client.on_message(filters.command("افكر$", prefixes=f".") & filters.me)
async def guess_1(c, msg):
    deq = deque(list("🤔🧐🤔🧐🤔🧐"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await msg.edit("".join(deq))
        deq.rotate(1)

# == == == == == == == == == == == == == == == == == == == ==



@Client.on_message(filters.command("متت$", prefixes=f".") & filters.me)
async def mttt_1(c, msg):
    deq = deque(list("😹🤣😂😹🤣😂"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await msg.edit("".join(deq))
        deq.rotate(1)

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("زعلت$", prefixes=f".") & filters.me)
async def dayeg_1(c, msg):
    deq = deque(list("😕😞🙁☹️😕😞🙁"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await msg.edit("".join(deq))
        deq.rotate(1)

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("ساعه$", prefixes=f".") & filters.me)
async def clock_1(c, msg):
    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await msg.edit("".join(deq))
        deq.rotate(1)

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("مح$", prefixes=f".") & filters.me)
async def moh_1(c, msg):
    deq = deque(list("😗😙😚😚💋😚😘"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await msg.edit("".join(deq))
        deq.rotate(1)

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("جيم$", prefixes=f".") & filters.me)
async def game_11(c, msg):
    deq = deque(list("🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await msg.edit("".join(deq))
        deq.rotate(1)

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("الارض$", prefixes=f".") & filters.me)
async def ard_1(c, msg):
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await msg.edit("".join(deq))
        deq.rotate(1)


# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("قمر$", prefixes=f".") & filters.me)
async def qamr_1(c, msg):
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await msg.edit("".join(deq))
        deq.rotate(1)

# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command(["قمر$","اقمار$"],prefixes=f".") & filters.me )
async def moon(c,msg):
  listt = [        "🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗",
        "🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘",
        "🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑",
        "🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒",
        "🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓",
        "🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔",
        "🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕",
        "🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖",
        ]
  for x in range(1,15):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(0.5)
      except :
        pass


# == == == == == == == == == == == == == == == == == == == ==

@Client.on_message(filters.command("قمور$", prefixes=f".") & filters.me)
async def qmor_1(c, msg):
    animation_interval = 0.2
    animation_ttl = range(96)
    await msg.edit("قمور..")
    animation_chars = [
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 32])
    await FORCE_JOIN(c)

# == == == == == == == == == == == == == == == == == == == ==
