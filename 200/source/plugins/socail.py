from pyrogram import Client, filters
from config import *
import asyncio
import requests, re

@app.on_message(filters.command("سوش", prefixes=f".") & filters.me)
async def msong(app, msg):
    if msg.reply_to_message:
       yad = msg.reply_to_message.id
    else:
       yad = None
    link = msg.text.split(None, 1)[1]
    if not link :
        return
    if "https://www.instagram.com/" in link :
        await msg.edit(f"• جاري البحث... \n•")
        rr = insts(link)
        if rr["status"] == "Done":
            vedio = rr["vedio"]
            await msg.edit("• جاري الرفع... ")
            copy=f"• BY : " + app.me.mention
            try:
                await app.send_video(
                msg.chat.id,
                video=vedio,
                duration="instagram",
                file_name="video",
                reply_to_message_id=yad,
                caption=copy ,
                )
                await msg.delete()
            except Exception as e:
                await message.edit(f"• خطأ في التحميل.\n•")
        else:
            await msg.edit("• اللينك غير مدعوم.")
    elif "https://" in link and "." in link:
        await msg.edit(f"• جاري البحث... \n•")
        rr = social(link)
        if rr["status"] == "Done":
            vedio = rr["vedio"]
            await msg.edit("• جاري الرفع... ")
            copy=f"• BY : " + app.me.mention
            await msg.delete()
            try:
                await app.send_video(
                msg.chat.id,
                video=vedio,
                duration="socialmedia",
                file_name="video",
                reply_to_message_id=yad,
                caption=copy ,
                )
                await msg.delete()
            except Exception as e:
                await msg.edit(f"• خطأ في التحميل.\n•")
    else:
        await msg.edit(f"• عذرا هذا الرابط غير صحيح!!")

def insts(link):
    headers = {
    'Host': 'igdownloader.app',
    # 'content-length': '113',
    'sec-ch-ua': 'Google',
    'accept': '*/*',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': 'Android',
    'origin': 'https://igdownloader.app',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://igdownloader.app/en/download-instagram-video',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    # 'cookie': '_ga_KP3KQR5T5P=GS1.1.1686573885.1.0.1686573885.0.0.0; _ga=GA1.1.20796359.1686573886; __gads=ID=917ea61f7469b86b-2220c8d1a5b400e6:T=1686570336:RT=1686570336:S=ALNI_MZXZoXB-yB7GbQPZPDrCpKQidGjEA; __gpi=UID=00000c4a5a972bf6:T=1686570336:RT=1686570336:S=ALNI_MYoItZvCIIz2S_cBxoNrmC7HW_7Ng',
}

    data = {
    'recaptchaToken': '',
    'q': link,
    't': 'media',
}


    res = requests.post('https://igdownloader.app/api/ajaxSearch', headers=headers, data=data).json()
    if res["status"] == "ok":
        dataa = res["data"]
        vedio = re.findall('href=\"(.*?)" class=\"abutton is-success is-fullwidth  btn-premium mt-3\" rel=\"nofollow\" title=\"Download Video\">',dataa)[0]
        return {"status":"Done","vedio":vedio,"POWEREDBY":"@Ues_steven"}
    else:
        return {"status":"none","POWEREDBY":"@Ues_steven"}
def social(link):
    headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
}

    data = {
    'url': link,
    'token': '8415931073:AAElnLUzNw0Q8C_saz3tEZG3VHim4gKUcCw',
}


    response = requests.post('https://www.cole13.com/vidgrab/wp-json/aio-dl/video-data/',  headers=headers, data=data)
    if "error" in response.text:
        return {"status":"none","POWEREDBY":"@Ues_steven"}
    else:
        z = len(response.json()["medias"])
        if  1 < z < 5:
            vedio = response.json()["medias"][z-2]["url"]
            return {"status":"Done","vedio":vedio,"POWEREDBY":"@Ues_steven"}
        elif  1 == z:
            vedio = response.json()["medias"][0]["url"]
            return {"status":"Done","vedio":vedio,"POWEREDBY":"@Ues_steven"}
            