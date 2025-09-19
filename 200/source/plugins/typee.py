from pyrogram import Client, filters
from config import *

@Client.on_message(filters.me & filters.regex('^.اكتب (.*?)') & filters.reply)
async def type_on_gif(c,msg) :
    if not msg.reply_to_message.animation :
        return await msg.edit('• هذه ليست متحركه ..')
    message = await msg.edit('• جاري تحميل المتحركه')
    await msg.reply_to_message.download(f'./{msg.id}.mp4')
    await message.delete()
    text = msg.text.replace('.اكتب ','')
    r.set(f'{sudo_id}:user_chat:{msg.from_user.id}',str(msg.chat.id))
    r.set(f'{sudo_id}:user_vid:{msg.from_user.id}',str(msg.id) + '.mp4')
    r.set(f'{sudo_id}:user_text:{msg.from_user.id}',text)
    try :
        result = await c.get_inline_bot_results(bot_user,query="متحركه")
        await c.send_inline_bot_result(msg.chat.id, result.query_id, result.results[0].id)
    except :
        await msg.edit("• فعل الانلاين من @botFather")