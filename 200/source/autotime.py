from asyncio import sleep
from time import strftime
from config import *
from pyrogram.errors import FloodWait
from PIL import Image, ImageDraw, ImageFont
import random
from os import remove 

def type_on_photo(path, output, text):
    image = Image.open(path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 60)
    fill_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    shadow_color = (0, 0, 0, 100)
    shadow_offset = (2, 2)
    text_width, text_height = draw.textsize(text, font=font)
    max_x = image.width - text_width
    max_y = image.height - text_height
    min_x = text_width
    min_y = text_height
    x = random.randint(min_x, max_x)
    y = random.randint(min_y, max_y)
    draw.text((x, y), text, font=font, fill=fill_color, stroke_width=2, stroke_fill=shadow_color)
    image.save(output)
    return output



async def main_time():
   ay = None
   while r.get(f"{sudo_id}photo_time") :
      time = strftime("%I:%M")
      try:
         if ay != time:
            ay = time
            photos = [p async for p in app.get_chat_photos("me")]
            new_photo = type_on_photo('./old_photo.jpg','new_photo.jpg',time)
            await app.delete_profile_photos(photos[0].file_id)
            await app.set_profile_photo(photo="./new_photo.jpg")
            remove('./new_photo.jpg')
         else:
            await sleep(0)
      except FloodWait as e:
         await sleep(e.value)
         await sleep(7)
