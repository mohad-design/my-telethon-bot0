from pyrogram import Client, filters
from config import *
from autotime import main_time

@Client.on_message(filters.me & (filters.regex('^.تفعيل الصوره الوقتيه') |filters.regex('^.تحديث الصوره الوقتيه')) )
async def photo_on(c,msg) :
    r.set(f"{sudo_id}photo_time",1)
    photos = [p async for p in app.get_chat_photos("me")]
    await app.download_media(photos[0].file_id,file_name='./old_photo.jpg')
    await msg.edit('• تم {}'.format(msg.text.replace('.','')))
    await main_time()

@Client.on_message(filters.me & filters.regex('^.تعطيل الصوره الوقتيه'))
async def photo_off(c,msg) :
    r.delete(f"{sudo_id}photo_time")
    await msg.edit('• تم تعطيل الصوره الوقتيه ')
    
