from pyrogram import Client, filters
from pyrogram.types import Message



@Client.on_message(filters.command("انشاء", ".") & filters.me)
async def create_(c, m):
    if len(m.command) < 3:
        await m.edit(
            "• لاستخدام الامر :"
            "\n"
            ".انشاء مجموعه + اسم المجموعه"
            "\n"
            ".انشاء قناه + اسم القناه"
        )
    group_type = m.command[1]
    split = m.command[2:]
    group_name = " ".join(split)
    msg = await m.edit("⚡️")
    desc = "BY : " + c.me.first_name
    if group_type == "مجموعه": 
        _id = await c.create_supergroup(group_name, desc)
        link = await c.get_chat(_id.id)
        await msg.edit(
            f"**• تم انشاء المجموعه : [{group_name}]({link.invite_link})**",
            disable_web_page_preview=True,
        )
    elif group_type == "قناه":
        _id = await c.create_channel(group_name, desc)
        link = await c.get_chat(_id.id)
        await msg.edit(
            f"**• تم انشاء القناه : [{group_name}]({link.invite_link})**",
            disable_web_page_preview=True,
        )
 
