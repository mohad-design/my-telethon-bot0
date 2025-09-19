from config import *


owner = {}
kick= {}
@bot.on_raw_update()
async def deletadmin(client, update, users, chats):
  try:
   try:
    chat_id = int(f"-100{update.channel_id}")
   except:
     return
   if update.new_participant.kicked_by == client.me.id: return
   if not owner.get(chat_id):
     owner[chat_id] = "Not Found"
     async for m in client.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
          if m.status == enums.ChatMemberStatus.OWNER: owner[chat_id] = m.user.id
   if owner[chat_id] == update.new_participant.kicked_by: return
   if not kick.get(update.new_participant.kicked_by):
       kick[update.new_participant.kicked_by] = []
   kick[update.new_participant.kicked_by].append(update.prev_participant.user_id)
   kam = len(kick[update.new_participant.kicked_by])
   xx = 3 - kam
   if not kam > 3:
     user = await client.get_chat(update.new_participant.kicked_by)
     await client.send_message(chat_id, f"قام احد المشرفين بطرد مستخدم\nUser : {user.first_name} \nUser id : {update.new_participant.kicked_by} \nعدد الاشخاص الذي طردهم : {kam}\nعدد التحذيرات المتبقيه : {xx}")
     return
   else:
      await app.resolve_peer(chat_id)
      await app.resolve_peer(update.new_participant.kicked_by)
      await app.ban_chat_member(chat_id, update.new_participant.kicked_by)
      user = await client.get_chat(update.new_participant.kicked_by)
      await client.send_message(chat_id, f"قام احد المشرفين بطرد مستخدم\nUser : {user.first_name} \nUser id : {update.new_participant.kicked_by} \nعدد الاشخاص الذي طردهم : {kam}\n\nتم إزالة المستخدم من هنا بواسطة البوت\n@{client.me.username} ✨♥️")
  except:
    pass
      
