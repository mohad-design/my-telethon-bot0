from pyrogram import Client, filters,enums
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from config import *
import asyncio
import re

async def UTag(c, user_id):
    get = await app.get_chat(user_id)
    name = get.first_name
    user_id_ = get.id
    Tag = f"[{name}](tg://user?id={user_id_})"
    return Tag


@bot.on_inline_query(filters.regex("^الاوامر$") )
async def answer(client, inline_query):
    reply_markup = InlineKeyboardMarkup(
            [[
             InlineKeyboardButton("✷ م1",callback_data="help1"),
             InlineKeyboardButton("✷ م2",callback_data="help2"),
             ],
             [
             InlineKeyboardButton("✷ م3",callback_data="help3"),
             InlineKeyboardButton("✷ م4",callback_data="help4"),
             ],
             [
             InlineKeyboardButton("✷ م5",callback_data="help5"),
             InlineKeyboardButton("✷ م6",callback_data="help6"),
             ],
             [
             InlineKeyboardButton("◜᥉᥆ᖇᥴ꧖◞",url="https://t.me/Hx_x0"),
             ],
             [
             InlineKeyboardButton("◜ꪔY ժᥱ᥎◞",url="https://t.me/Ues_steven"),
             ]]
             )
    await inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="اوامر البوت",
                input_message_content=InputTextMessageContent(
                    "↯︙❬ م1 ❭ اوامر الخاص\n↯︙❬ م2 ❭ اوامر القنوات والمجموعات\n↯︙❬ م3 ❭ اوامر اليوتيوب\n↯︙❬ م4 ❭ اوامر الاذاعه\n↯︙❬ م5 ❭ اوامر التسليه\n↯︙ ❬ م6 ❭ اوامر اضافيه"
                ),
                url="https://t.me/Ues_steven",
                description="؍`𝐬𝐭𝐞𝐯𝐞𝐧 ٭",
                reply_markup=reply_markup
            ),
        ],
        cache_time=1
    )

@bot.on_inline_query(filters.regex("^change_clock$") )
async def change_clock_answer(client, inline_query):
    reply_markup = InlineKeyboardMarkup(
            [[
             InlineKeyboardButton("₁₂:₃₄",callback_data="style:0"),
             InlineKeyboardButton("𝟏𝟐:𝟑𝟒",callback_data="style:1"),
             ],
             [
             InlineKeyboardButton("𝟭𝟮:𝟯𝟰",callback_data="style:2"),
             InlineKeyboardButton("①②:③④",callback_data="style:3"),
             ],
             [
             InlineKeyboardButton("❶❷:❸❹",callback_data="style:4"),
             InlineKeyboardButton("𝟙𝟚:𝟛𝟜",callback_data="style:5"),
             ],
             [
             InlineKeyboardButton("１２:３４",callback_data="style:6"),
             InlineKeyboardButton("𝟷𝟸:𝟹𝟺",callback_data="style:7"),
             ],
             [
             InlineKeyboardButton("◜᥉᥆ᖇᥴ꧖◞",url="https://t.me/Hx_x0"),
             ],
             [
             InlineKeyboardButton("◜ꪔY ժᥱ᥎◞",url="https://t.me/Ues_steven"),
             ]]
             )
    await inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="change clock style",
                input_message_content=InputTextMessageContent(
                    "↯︙قم باختيار شكل الخط للساعه \n↯"
                ),
                url="https://t.me/Ues_steven",
                description="؍`𝐬𝐭𝐞𝐯𝐞𝐧 ٭",
                reply_markup=reply_markup
            ),
        ],
        cache_time=1
    )

@Client.on_callback_query(filters.regex('^style:(.*)'))
async def change_clock_selecte(c, q):
    if int(sudo_id) == int(q.from_user.id):
        num = re.findall("^style:(\\d+)", q.data)[0]
        r.set(f"{sudo_id}:TIME_STYLE", num)
        await c.edit_inline_text(q.inline_message_id, "↯︙تم اختيار الشكل بنجاح\n↯")

@bot.on_inline_query(filters.regex("^othello$") )
async def answer_othello(client, q):
    answers = []
    name = q.from_user.first_name
    OTHELLO_KEY = [
            [
                InlineKeyboardButton(
                    "العب 👀",
                    callback_data=f"strat-{q.from_user.id}-{name}"
                )
            ]
        ]
    answers.append(
            InlineQueryResultArticle(
                title=".يلا بينا نلعب يابن خالتي 🕹",
                input_message_content=InputTextMessageContent(message_text="دوس ع الزرار عشان تلاعبه 😉."),
                reply_markup=InlineKeyboardMarkup(OTHELLO_KEY)
            )
        )
    await q.answer(results=answers, cache_time=0)
    return

@Client.on_inline_query()
async def inline_by_anubis(c, q):
    answers = []
    if re.findall("^hmsa (\\d+)", q.query):
        rand = re.findall("^hmsa (\\d+)", q.query)[0]
        HMSA_KEY = [
            [
                InlineKeyboardButton(
                    "اهمس 👀",
                    url=f"http://t.me/{bot_user}?start=hmsa{rand}"
                )
            ]
        ]
        answers.append(
            InlineQueryResultArticle(
                title="اهمس",
                input_message_content=InputTextMessageContent(message_text="انتظر بيعملك همسه 😉.."),
                reply_markup=InlineKeyboardMarkup(HMSA_KEY)
            )
        )
        await q.answer(results=answers, cache_time=0)
        return

    if re.findall("^send_hmsa (\\d+)", q.query):
        rand = re.findall("^send_hmsa (\\d+)", q.query)[0]
        S_HMSA_KEY = [
            [
                InlineKeyboardButton(
                    "افتح 📬",
                    callback_data=f"hmsa:{rand}"
                )
            ]
        ]
        from_id = r.get(f"{sudo_id}:hmsa:{rand}:from")
        from_ = await UTag(app, from_id)
        m_text = f"- ازيك 👋🏻\n- عندك همسه من {from_} "
        answers.append(
            InlineQueryResultArticle(
                title="اهمس",
                input_message_content=InputTextMessageContent(message_text=m_text),
                reply_markup=InlineKeyboardMarkup(S_HMSA_KEY)
            )
        )
        await q.answer(results=answers, cache_time=0)
        return
    
@Client.on_callback_query(filters.regex('^hmsa:(.*)'))
async def HMSA_Callback(c, q):
    rand = re.findall("^hmsa:(.*)", q.data)[0]
    to_id = r.get(f"{sudo_id}:hmsa:{rand}:to")
    from_id = r.get(f"{sudo_id}:hmsa:{rand}:from")
    hmsa_text = r.get(f"{sudo_id}:hmsa:{rand}:text")
    if (int(to_id) == int(q.from_user.id)) or (int(from_id) == int(q.from_user.id)):
        O_HMSA_KEY = [
            [
                InlineKeyboardButton(
                    "افتح 📭",
                    callback_data=f"hmsa:{rand}"
                )
            ]
        ]
        from_ = await UTag(app, from_id)
        m_text = f"- ازيك 👋🏻\n- عندك همسه من {from_} "
        await q.answer(hmsa_text, show_alert=True)
        if int(to_id) == int(q.from_user.id):
            try:
                await c.edit_inline_text(q.inline_message_id, m_text, reply_markup=InlineKeyboardMarkup(O_HMSA_KEY))
            except Exception as e:
                pass
    else:
        await q.answer("وانت مالك ياخي الهمسه مش ليك", show_alert=True)
        
@bot.on_inline_query(filters.regex("^متحركه$") )
async def gif_typee(client, inline_query):
    reply_markup=InlineKeyboardMarkup([
         [InlineKeyboardButton("أبيض",callback_data="col/white"),InlineKeyboardButton("أسود",callback_data="col/black")],
         [InlineKeyboardButton("أحمر",callback_data="col/red"),InlineKeyboardButton("أزرق",callback_data="col/blue")],
         [InlineKeyboardButton("أخضر",callback_data="col/green"),InlineKeyboardButton("أصفر",callback_data="col/yellow")],
         [InlineKeyboardButton("cyan",callback_data="col/cyan"),InlineKeyboardButton("magenta",callback_data="col/magenta")],
    ])
    await inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="كتابه علي المتحركه",
                input_message_content=InputTextMessageContent(
                    "• اختر لون النص الان"
                ),
                url="https://t.me/Hx_x0",
                description="𝙨𝙤𝙪𝙧𝙘𝙚 𝐬𝐭𝐞𝐯𝐞𝐧",
                reply_markup=reply_markup
            ),
        ],
        cache_time=1
    )