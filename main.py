import keyboards
from config import TOKEN
from telebot import types
from telebot.async_telebot import AsyncTeleBot
from time import sleep 
from datetime import datetime
import asyncio
from pytube import *
from youtubesearchpython import VideosSearch
import os
import requests

bot = AsyncTeleBot(TOKEN)

ids = list()
names = list()

@bot.message_handler(commands = ["start"])
async def start(message):
    userid = message.from_user.id
    if not userid in ids:
        ids.append(userid)
    try:
        current_datetime = datetime.now()
        username = message.from_user.username
        if username == None:
            username = message.from_user.first_name,message.from_user.last_name
        if not username in names:
            names.append(username)
            
    except:
        username = "UserHaveNoName("
        if not username in names:
            names.append(username)
    print("ID: "+str(userid)+";","username: "+str(username)+";","time: "+ str(current_datetime.hour)+":"+ str(current_datetime.minute)+ ":"+str(current_datetime.second))
    print(ids,names)
    await bot.send_message(message.chat.id, "Привет! Здесь ты сможешь скачать видео с YouTube или анимешку, а если что-то не понятно то просто напиши'/help'",reply_markup=keyboards.menu)
    await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAIrIGYTCo3qRYeGuVFXVYABqO_m3sNBAAIFAAPANk8T-WpfmoJrTXU0BA")

@bot.message_handler()
async def handle_youtube_link(message: types.Message):
    searchList = VideosSearch(message.text, limit = 5).result()['result']
    keyboard = list()
    for element in searchList:
        keyboard.append([types.InlineKeyboardButton(text=element['title'], callback_data=element['link'])])
    choose_markup =  types.InlineKeyboardMarkup(keyboard, 1)
    await bot.send_message(message.chat.id, 'Найденные варианты:', reply_markup=choose_markup)

#@bot.message_handler()
#async def search_on_youtube(message: types.Message):
#    global yt
#    yt = YouTube(message.text)
#    yt.streams
#    keyboard = list()
#    await bot.send_message(message.chat.id,yt.streams.filter(file_extension='mp4'),reply_markup=keyboards.res)
#@bot.callback_query_handler(func = lambda call:True)
#async def call_streams(call):
#    if call.data =='144':
#        stream = yt.streams.get_by_itag(160)
#        stream.download()
#    if call.data =='240':
#        stream = yt.streams.get_by_itag(133)
#        stream.download()
#    if call.data =='360':
#        stream = yt.streams.get_by_itag(18)
#        stream.download()
#    if call.data =='480':
#        stream = yt.streams.get_by_itag(135)
#        stream.download()
#    if call.data =='720':
#        stream = yt.streams.get_by_itag(22)
#        stream.download()
#    if call.data =='1080':
#        stream = yt.streams.get_by_itag(137)
#        stream.download()

async def main():
    await bot.polling()

if __name__ == "__main__":
    asyncio.run(main())

asyncio.run(bot.polling(none_stop=True))