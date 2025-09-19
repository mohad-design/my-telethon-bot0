import asyncio
import random
from collections import deque

import requests
from pyrogram import Client, filters
from pyrogram.types import Message

def get_name(msg):
    if msg.from_user.last_name:
        last_name = msg.from_user.last_name
    else:
        last_name = ""
    if msg.from_user.first_name:
        first_name = msg.from_user.first_name
    else:
        first_name = ""
    return f"[{first_name} {last_name}](tg://user?id={msg.from_user.id})"


async def is_Admin(chat, id):
    admins = []
    async for m in app.get_chat_members(chat, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        admins.append(m.user.id)
    if id in admins:
        return True
    else:
        return False

@Client.on_message(filters.command("نادم$", prefixes=f".") & filters.me)
async def anem_1(c, msg):
    animation_interval = 1
    animation_ttl = range(20)
    animation_chars = [
        "⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⡇⠄⣿⣿⣿⡿⠋⣉⣉⣉⡙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⠃⠄⠹⠟⣡⣶⢟⣛⣛⡻⢿⣦⣩⣤⣬⡉⢻⣿⣿⣿⣿\n"
    "⣿⣿⣿⠄⢀⢤⣾⣿⣿⣿⡿⠿⠿⠿⢮⡃⣛⡻⢿⠈⣿⣿⣿⣿\n"
    "⣿⡟⢡⣴⣯⣿⣿⣿⠤⣤⣭⣶⣶⣶⣮⣔⡈⠛⢓⠦⠈⢻⣿⣿\n"
    "⠏⣠⣿⣿⣿⣿⣿⣿⣯⡪⢛⠿⢿⣿⣿⣿⡿⣼⣿⣿⣮⣄⠙⣿\n"
    "⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⡭⠴⣶⣶⣽⣽⣛⡿⠿⠿⠇⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣷⣝⣛⢛⢋⣥⣴⣿⣿\n"
    "⣿⣿⣿⣿⣿⢿⠱⣿⣛⠾⣭⣛⡿⢿⣿⣿⣿⣿⣿⡀⣿⣿⣿⣿\n"
    "⠑⠽⡻⢿⣮⣽⣷⣶⣯⣽⣳⠮⣽⣟⣲⠯⢭⣿⣛⡇⣿⣿⣿⣿\n"
    "⠄⠄⠈⠑⠊⠉⠟⣻⠿⣿⣿⣿⣷⣾⣭⣿⠷⠶⠂⣴⣿⣿⣿⣿\n"
    "⠄⠄⠄⠄⠄⠄⠄⠁⠙⠒⠙⠯⠍⠙⢉⣡⣶⣿⣿⣿⣿⣿⣿⣿\n"
    "⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 10])

# == == == == == == == == == == == == == == == == == == == ==
@Client.on_message(filters.command("صدمه$", prefixes=f".") & filters.me)
async def anem_2(c, msg):
    animation_interval = 1
    animation_ttl = range(20)
    animation_chars = [
          "⠄⠄⠄⠄⠄⣀⣀⣤⣶⣿⣿⣶⣶⣶⣤⣄⣠⣴⣶⣿⣶⣦⣄⠄\n"
    "⠄⣠⣴⣾⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦\n"
    "⢠⠾⣋⣭⣄⡀⠄⠙⠻⣿⣿⡿⠛⠋⠉⠉⠉⠙⠛⠿⣿⣿⣿⣿\n"
    "⡎⡟⢻⣿⣷⠄⠄⠄⠄⡼⣡⣾⣿⣿⣦⠄⠄⠄⠄⠄⠈⠛⢿⣿\n"
    "⡇⣷⣾⣿⠟⠄⠄⠄⢰⠁⣿⣇⣸⣿⣿⠄⠄⠄⠄⠄⠄⠄⣠⣼\n"
    "⣦⣭⣭⣄⣤⣤⣴⣶⣿⣧⡘⠻⠛⠛⠁⠄⠄⠄⠄⣀⣴⣿⣿⣿\n"
    "⢉⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿\n"
    "⡿⠛⠛⠛⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⡇⠄⠄⢀⣀⣀⠄⠄⠄⠄⠉⠉⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⠈⣆⠄⠄⢿⣿⣿⣷⣶⣶⣤⣤⣀⣀⡀⠄⠄⠉⢻⣿⣿⣿⣿⣿\n"
    "⠄⣿⡀⠄⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠄⢠⣿⣿⣿⣿⣿\n"
    "⠄⣿⡇⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄⢀⣼⣿⣿⣿⣿⣿\n"
    "⠄⣿⡇⠄⠠⣿⣿⣿⣿⣿⣿⣿⡿⠋⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿\n"
    "⠄⣿⠁⠄⠐⠛⠛⠛⠉⠉⠉⠉⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⠄⠻⣦⣀⣀⣀⣀⣀⣤⣤⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋\n"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 10])

# == == == == == == == == == == == == == == == == == == == ==
@Client.on_message(filters.command("معصب$", prefixes=f".") & filters.me)
async def anem_3(c, msg):
    animation_interval = 1
    animation_ttl = range(20)
    animation_chars = [
        "┈┈┈╭━━━━━╮┈┈┈┈┈\n"
    "┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈\n"
    "┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n"
    "┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n"
    "┈┈╭┻┊┊╰━┻━╮┈┈┈┈\n"
    "┈┈╰┳┊╭━━━┳╯┈┈┈┈\n"
    "┈┈┈┃┊┃╰━━┫┈I'm ضــايج\n"
    "┈┈┈┈┈┈┏━┓┈┈┈┈┈┈So لا تعصــبني\n"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 10])

# == == == == == == == == == == == == == == == == == == == ==
@Client.on_message(filters.command("فيل$", prefixes=f".") & filters.me)
async def anem_4(c, msg):
    animation_interval = 1
    animation_ttl = range(20)
    animation_chars = [
        "┈┈┈┈╱▔▔▔▔▔╲┈╱▔╲\n"
    "┈┈┈┈▏┈┈▏╭╮▕┈▏╳▕\n"
    "┈┈┈┈▏┈┈▏┈┈▕┈╲▂╱\n"
    "┈╱▔▔╲▂╱╲▂▂┈╲▂▏▏\n"
    "╭▏┈┈┈┈┈┈┈▏╲▂▂╱┈\n"
    "┃▏┈┈┈┈▏┈┈▏┈┈┈┈┈\n"
    "╯▏┈╲╱▔╲▅▅▏┈┈┈┈\n"
    "┈╲▅▅▏▕▔▔▔▔▏┈┈┈┈ν2.ο\n"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 10])

# == == == == == == == == == == == == == == == == == == == ==
@Client.on_message(filters.command("ثعلب$", prefixes=f".") & filters.me)
async def anem_5(c, msg):
    animation_interval = 1
    animation_ttl = range(20)
    animation_chars = [
        "╱▏┈┈┈┈┈┈ ▕╲▕╲┈┈┈\n"
    "▏▏┈┈┈┈┈┈ ▕▏▔▔╲┈┈\n"
    "▏╲┈┈┈┈┈┈╱┈▔┈ ▔ ╲┈\n"
    "╲▏▔▔▔▔▔▔╯╯╰┳━━▀\n"
    "┈▏╯╯╯╯╯╯╯╯╱┃┈┈┈\n"
    "┈┃┏┳┳━━━┫┣┳┃┈┈┈\n"
    "┈┃┃┃┃┈┈┈┃┃┃┃┈┈┈\n"
    "┈┗┛┗┛┈┈┈┗┛┗┛┈┈┈You are ثعلــب مــاكر\n"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 10])

# == == == == == == == == == == == == == == == == == == == ==
@Client.on_message(filters.command("خنزير$", prefixes=f".") & filters.me)
async def anem_8(c, msg):
    animation_interval = 1
    animation_ttl = range(20)
    animation_chars = [
        "┈┏━╮╭━┓┈╭━━━━╮\n"
        "┈┃┏┗┛┓┃╭┫U   خنـزيـر┃\n"
        "┈╰┓▋▋┏╯╯╰━━━━╯\n"
        "╭━┻╮╲┗━━━━╮╭╮┈\n"
        "┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
        "╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
        "┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
        "┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 10])

# == == == == == == == == == == == == == == == == == == == ==
@Client.on_message(filters.command("كلبي$", prefixes=f".") & filters.me)
async def anem_6(c, msg):
    animation_interval = 1
    animation_ttl = range(20)
    animation_chars = [
        "╭━┳━╭━╭━╮╮\n"
        "┃┈┈┈┣▅╋▅┫┃\n"
        "┃┈┃┈╰━╰━━━━━━╮\n"
        "╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣\n"
        "╲┃┈┈┈┈┈┈┈┈┈┈▉▉▉\n"
        "╲┃┈┈┈┈┈┈┈┈┈┈◥▉◤\n"
        "╲┃┈┈┈┈╭━┳━━━━╯\n"
        "╲┣━━━━━━┫You are كـلبي الــمدلل\n"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 10])

# == == == == == == == == == == == == == == == == == == == ==
@Client.on_message(filters.command("سبونج$", prefixes=f".") & filters.me)
async def anem_7(c, msg):
    animation_interval = 1
    animation_ttl = range(20)
    animation_chars = [
        "┈┈ ╱▔▔▔▔▔▔▔▔▔▔▔▏\n"
    "┈╱╭▏╮╭┻┻╮╭┻┻╮ ╭▏ \n"
    "▕╮╰▏╯┃╭╮┃┃╭╮┃ ╰▏ \n"
    "▕╯┈▏┈┗┻┻┛┗┻┻┻╮ ▏ \n"
    "▕╭╮▏╮┈┈┈┈┏━━━╯ ▏\n"
    "▕╰╯▏╯╰┳┳┳┳┳┳╯ ╭▏ \n"
    "▕┈╭▏╭╮┃┗┛┗┛┃┈ ╰▏ \n"
    "▕┈╰▏╰╯╰━━━━╯┈┈ ▏I'm سبـونـج بــوب\n"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 10])
