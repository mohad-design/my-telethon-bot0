from pyrogram import Client, enums, filters
from pyrogram.types import Message



@Client.on_message(
    filters.command(["انضم"], ".") & (filters.me)
)
async def join(client: Client, message: Message):
    tex = message.command[1] if len(message.command) > 1 else message.chat.id
    g = await message.reply_text("`جاري⚡...`")
    try:
        await client.join_chat(tex)
        await g.edit(f"**نجح الانضمام الي** `{tex}`")
    except Exception as ex:
        await g.edit(f"**ERROR:** \n\n{str(ex)}")


@Client.on_message(
    filters.command(["غادر"], ".") & (filters.me)
)
async def leave(client: Client, message: Message):
    xd = message.command[1] if len(message.command) > 1 else message.chat.id
    xv = await message.reply_text("`جاري التنفيذ...`")
    try:
        await xv.edit_text(f"{client.me.first_name} غادر المجموعه باي 🖐️")
        await client.leave_chat(xd)
    except Exception as ex:
        await xv.edit_text(f"**ERROR:** \n\n{str(ex)}")


@Client.on_message(
    filters.command(["غادر الجروبات"], ".") & (filters.me)
)
async def kickmeall(client: Client, message: Message):
    tex = await message.reply_text("`جاري مغادرة المحادثات...`")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await tex.edit(
        f"**نجح المغادره من{done} مجموعه, فشل المغادره من{er} مجموعه**"
    )


@Client.on_message(filters.command(["غادر القنوات"], ".") & filters.me)
async def kickmeallch(client: Client, message: Message):
    ok = await message.reply_text("`جاري مغادرة المحادثات...`")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.CHANNEL):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await ok.edit(
        f"**نجح المغادره من{done} قناه, فشل المغادره من{er} قناه**"
    )


