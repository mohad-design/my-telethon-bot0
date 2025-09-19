from pyrogram.filters import create
from pyrogram import Client, filters, enums
from pyrogram.types import Message
from config import *
import asyncio
import re

def FONT_TYPING_(_, __, m: Message):
  if r.get(f'{sudo_id}:FONT_TYPING'):
    return True
  else:
    return False

FONT_TYPING = create(FONT_TYPING_)

@Client.on_message(filters.command("تعطيل تعديل الخط$", prefixes=f".") & filters.me)
async def FONT_TYPING_disable(c, msg):
    r.delete(f'{sudo_id}:FONT_TYPING')
    await msg.edit("✷ تم تعطيل تعديل الخط")

@Client.on_message(filters.command("تفعيل تعديل الخط$", prefixes=f".") & filters.me)
async def FONT_TYPING_enableH(c, msg):
    await msg.edit(
       "✷ معلش احنا بنتكلم لو عاوز تستخدم الامر صح يبقا كدا"
       "\n"
       "✷ `.تفعيل تعديل الخط + رقم نوع الخط`"
       "\n\n"
       "✷ انواع الخطوط والارقام الداله عليها :"
       "\n"
       "1 - **خط غامق**"
       " او فاتح هخو هخو"
       "\n"
       "2 - __خط معووج__"
       " نصيحه متستخدمهوش عشان عدوك كدا مش هيحتار فيك"
       "\n"
       "3 - --خط تحته خط--"
       " مش لاقي تعليق والله الي عنده يبقا يقول"
       "\n"
       "4 - ~~خط فيه خط~~"
       " مش لاقي تعليق الي عنده يبقا يقول بردو"
       "\n"
       "5 - ||خط فاسد||"
       " متسالش لي اسمو فاسد لاني مترجمها من جوجل كدا بس عن نفسي انا مسميه الخط البضان والي بيستخدمه بضان زيه يلا فعله بقا عشان ترضي بضانك يبضين"
       "\n\n"
       "✷ مثال :"
       "\n"
       "`.تفعيل تعديل الخط 2`"
       "\n."
    )

@Client.on_message(filters.regex("^.تفعيل تعديل الخط [1-5]+$") & filters.me)
async def FONT_TYPING_enable(c, msg):
    regex = re.findall(".تفعيل تعديل الخط (.*)", msg.text)
    num = int(regex[0])
    r.set(f'{sudo_id}:FONT_TYPING', num)
    if num == 1:
       FONT = "**خط غامق**"
    elif num == 2:
       FONT = "__خط معووج__"
    elif num == 3:
       FONT = "--خط تحته خط--"
    elif num == 4:
       FONT = "~~خط فيه خط~~"
    elif num == 5:
       FONT = "||خط فاسد||"
    await msg.edit(f"✷ تم تفعيل تعديل الخط ( {FONT} )")

@Client.on_message(~filters.regex(r"^\.(.*)") & filters.me & filters.text & FONT_TYPING)
async def FONT_TYPING_RUN(c, msg):
   FONT = int(r.get(f'{sudo_id}:FONT_TYPING'))
   
   if FONT == 1:
       await msg.edit(f"<b>{msg.text}</b>", parse_mode=enums.ParseMode.HTML)
   elif FONT == 2:
      await msg.edit(f"<i>{msg.text}</i>", parse_mode=enums.ParseMode.HTML)
   elif FONT == 3:
      await msg.edit(f"<u>{msg.text}</u>", parse_mode=enums.ParseMode.HTML)
   elif FONT == 4:
      await msg.edit(f"<s>{msg.text}</s>", parse_mode=enums.ParseMode.HTML)
   elif FONT == 5:
       await msg.edit(f"<spoiler>{msg.text}</spoiler>", parse_mode=enums.ParseMode.HTML)
