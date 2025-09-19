import asyncio
from datetime import timezone, datetime, timedelta
import pytz
from asyncio import sleep
from time import strftime
from config import *
from pyrogram.errors import FloodWait

def zhrf_time(time):
  time_style = r.get(f"{sudo_id}:TIME_STYLE") or 1
  time = str(time)
  repl = [
     ["₀","₁","₂","₃","₄","₅","₆","₇","₈","₉"],
     ["𝟎","𝟏","𝟐","𝟑","𝟒","𝟓","𝟔","𝟕","𝟖","𝟗"],
     ["𝟬","𝟭","𝟮","𝟯","𝟰","𝟱","𝟲","𝟳","𝟴","𝟵"],
     ["⓪","①","②","③","④","⑤","⑥","⑦","⑧","⑨"],
     ["⓿","❶","❷","❸","❹","❺","❻","❼","❽","❾"],
     ["𝟘","𝟙","𝟚","𝟛","𝟜","𝟝","𝟞","𝟟","𝟠","𝟡"],
     ["０","１","２","３","４","５","６","７","８","９"],
     ["𝟶","𝟷","𝟸","𝟹","𝟺","𝟻","𝟼","𝟽","𝟾","𝟿"]
     ]
  curn = ["0","1","2","3","4","5","6","7","8","9"]
  for i in range(0,10):
    time = time.replace(curn[i], repl[int(time_style)][i])
  return time

async def main():
   ay = None
   while r.get(f"{sudo_id}clockk") :
      time_zone = r.get(f"{sudo_id}:TIME_ZONE") or 'Africa/Cairo'
      try:
         time = datetime.now(pytz.timezone(time_zone)).strftime('%I:%M')
      except Exception:
         time = datetime.now(pytz.timezone('Africa/Cairo')).strftime('%I:%M')
      my_name = r.get(f"{sudo_id}clockk")
      try:
         if ay != time:
            ay = time
            await app.update_profile(first_name=f'{zhrf_time(time)}' ,last_name=my_name)
         else:
            await sleep(0)
      except FloodWait as e:
         await sleep(e.value)
         await sleep(7)

async def time_bio_():
   ay = None
   while r.get(f"{sudo_id}kbio") :
      time_zone = r.get(f"{sudo_id}:TIME_ZONE") or 'Africa/Cairo'
      try:
         time = datetime.now(pytz.timezone(time_zone)).strftime('%I:%M')
      except Exception:
         time = datetime.now(pytz.timezone('Africa/Cairo')).strftime('%I:%M')
      CHANNEL = r.get(f"{sudo_id}:CHANNEL") or "Hx_x0"
      CHANNEL = CHANNEL.replace('@', '')
      try:
         if ay != time:
            ay = time
            await app.update_profile(bio=f'@{CHANNEL} | {zhrf_time(time)}')
         else:
            await sleep(0)
      except FloodWait as e:
         await sleep(e.value)
         await sleep(7)
   else:
      return

def time_bio():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(time_bio_())
    loop.close()

