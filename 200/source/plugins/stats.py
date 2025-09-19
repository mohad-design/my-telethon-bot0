from datetime import datetime

from pyrogram import Client, enums, filters
from pyrogram.types import Message



@Client.on_message(filters.command(["الاحصائيات", "status"], ".") & filters.me)
async def stats(client: Client, message: Message):
    Man = await message.edit_text("`اجمالي احصائيات حسابك...`")
    start = datetime.now()
    u = 0
    g = 0
    sg = 0
    c = 0
    b = 0
    a_chat = 0
    Meh = await client.get_me()
    async for dialog in client.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE:
            u += 1
        elif dialog.chat.type == enums.ChatType.BOT:
            b += 1
        elif dialog.chat.type == enums.ChatType.GROUP:
            g += 1
        elif dialog.chat.type == enums.ChatType.SUPERGROUP:
            sg += 1
            user_s = await dialog.chat.get_member(int(Meh.id))
            if user_s.status in (
                enums.ChatMemberStatus.OWNER,
                enums.ChatMemberStatus.ADMINISTRATOR,
            ):
                a_chat += 1
        elif dialog.chat.type == enums.ChatType.CHANNEL:
            c += 1

    end = datetime.now()
    ms = (end - start).seconds
    await Man.edit_text(
        """`احصائياتك في اخر {} ثانيه `
`انت تمتلك {} رساله في الخاص.`
`انت موجود في {} مجموعه .`
`انت موجود في {} مجموعه خارقه.`
`انت موجود في {} قناه.`
`انت ادمن في {} جروب.`
`البوتات = {}`""".format(
            ms, u, g, sg, c, a_chat, b
        )
    )

