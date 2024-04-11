import keyboards
from config import TOKEN
from telebot import types
from telebot.async_telebot import AsyncTeleBot
from time import sleep 
from datetime import datetime
import asyncio
from pytube import *
from youtubesearchpython import *
import os
import requests
from io import BytesIO
from pytube.cli import on_progress


#  https://t.me/Youtubescr_bot
#  https://t.me/Youtubescr_bot
#  https://t.me/Youtubescr_bot
#  https://t.me/Youtubescr_bot

bot = AsyncTeleBot(TOKEN)

ids = list()
names = list()

@bot.message_handler(commands = ["start"])
async def start(message: types.Message):
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
@bot.message_handler(commands = ["help"])
async def help(message: types.Message):
	await bot.send_message(message.chat.id, '''Привет! Здесь ты сможешь скачать видео с YouTube или анимешку, \n\nВидео не должно быть: 
						Слишком длинным
						Высокого качества(2к или 4к)
						Просто жди пока оно загрузиться
						Если что то пойдёт не так, то тебе об этом напишет''',reply_markup=keyboards.menu)


@bot.message_handler()
async def handle_youtube_link(message: types.Message):
	searchList = VideosSearch(message.text, limit = 10).result()['result']
	keyboard = list()
	for element in searchList:
		a = [types.InlineKeyboardButton(text=element['title'], callback_data=element['link'])]
		keyboard.append(a)
	choose_markup =  types.InlineKeyboardMarkup(keyboard,1)
	await bot.send_message(message.chat.id, 'Найденные варианты:', reply_markup=choose_markup)

@bot.callback_query_handler(func = lambda call:True)
async def call_streams(call: types.CallbackQuery):
	global data1
	try:
		if "youtube.com" in call.data or "youtu.be" in call.data:
			print(call.data)
			data1 = call.data
			await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=call.data) 
			await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.id,reply_markup=keyboards.res)
		if call.data == 'Video':
			call.data = data1
			await download_youtube_video(call.data, call.message.chat.id)
		if call.data == 'Audio':
			call.data = data1
			await download_youtube_audio_only(call.data, call.message.chat.id)
	except Exception as e:
		print(e)
		await bot.send_message(chat_id=call.message.chat.id, message_id=call.message.id, text=f"Ошибка при скачивании или отправке видео: \n{str(e)}")

async def download_youtube_video(url, chat_id):
	try:
		yt = YouTube(url)
		stream = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()
		buffer = BytesIO()
		stream.stream_to_buffer(buffer)
		await bot.send_video(chat_id, buffer.getvalue())
		buffer.flush()
	except Exception as e:
		print(e)
		await bot.send_message(chat_id, f"Ошибка при скачивании или отправке видео: \n{str(e)}")
		
async def download_youtube_audio_only(url, chat_id):
	try:
		yt = YouTube(url)
		stream = yt.streams.filter(only_audio=True).first()
		buffer = BytesIO()
		stream.stream_to_buffer(buffer)
		await bot.send_audio(chat_id, buffer.getvalue()) # filename = f"{yt.title}"
		buffer.flush()
	except Exception as e:
		print(e)
		await bot.send_message(chat_id, f"Ошибка при скачивании или отправке аудио: \n{str(e)}")
		
async def main():
	await bot.polling()

if __name__ == "__main__":
	asyncio.run(main())

asyncio.run(bot.polling(none_stop=True))

# updater = Updater(token='TOKEN', request_kwargs={'read_timeout': 1000, 'connect_timeout': 1000})