from config import TOKEN
from telebot import types
from telebot.async_telebot import AsyncTeleBot
import asyncio
from datetime import datetime
from pytube.innertube import _default_clients
from io import BytesIO
import keyboards
from youTube import download_youtube_audio_only, download_youtube_video, search_youtube_content
from weatherScraper import weather_scrap
from wikipedia_for_tg import send_info_from_wikipedia

_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]

#  https://t.me/Youtubescr_bot
#  https://t.me/Youtubescr_bot
#  https://t.me/Youtubescr_bot
#  https://t.me/Youtubescr_bot

bot = AsyncTeleBot(TOKEN)

ids = list()
names = list()

storage = {}

@bot.message_handler(commands = ["start"])
async def start(message: types.Message):
	try:
		userid = message.from_user.id
		if not userid in ids:
			ids.append(userid)
		storage[userid] = None
		current_datetime = datetime.now()
		username = message.from_user.username
		if not username:
			if message.from_user.last_name == None:
				message.from_user.last_name = ''
			username = f"{message.from_user.first_name} {message.from_user.last_name}"
		if not username in names:
			names.append(username)
		print("ID: "+str(userid)+";","username: "+str(username)+";","time: "+ str(current_datetime.hour)+":"+ str(current_datetime.minute)+ ":"+str(current_datetime.second))
		print(ids,names)
		await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAIrIGYTCo3qRYeGuVFXVYABqO_m3sNBAAIFAAPANk8T-WpfmoJrTXU0BA")
		await bot.send_message(message.chat.id, "Привет! Здесь ты сможешь скачать видео с YouTube или анимешку, а если что-то не понятно то просто напиши'/help'",reply_markup=keyboards.yourchoose)
	except Exception as e:
		print(e)
		await bot.send_message(chat_id=message.chat.id, message_id=message.id, text=f"Ошибка: \n{str(e)}")

@bot.message_handler(commands = ["help"])
async def help(message: types.Message):
	await bot.send_message(message.chat.id, '''Привет! Здесь ты сможешь скачать видео с YouTube или анимешку, \n\nВидео не должно быть: 
						Слишком длинным
						Высокого качества(2к или 4к)
						Просто жди пока оно загрузиться
						Если что то пойдёт не так, то тебе об этом напишет''',reply_markup=keyboards.menu)
	
@bot.message_handler(commands = ["choose"])
async def help(message: types.Message):
	await bot.send_message(message.chat.id, "Выбери, что хочешь получить:",reply_markup=keyboards.yourchoose)
# YOTUBECONTENT

@bot.message_handler()
async def query(message: types.Message): # ,call: types.CallbackQuery
	try:
		if message.text == "Weather":
			storage[message.from_user.id] = message.text
			return await bot.send_message(message.chat.id, "Weather")
		if message.text == "YouTube":
			storage[message.from_user.id] = message.text
			return await bot.send_message(message.chat.id, "YouTube")
		if message.text == "Wikipedia":
			storage[message.from_user.id] = message.text
			return await bot.send_message(message.chat.id, "Wikipedia")
		if not storage[message.from_user.id]:
			return await bot.send_message(message.chat.id, "Сделайте выбор") # ,reply_markup=keyboards.yourchoose
		if storage[message.from_user.id] == "YouTube":
			await bot.send_message(message.chat.id, 'Найденные варианты:', reply_markup=await search_youtube_content(message))
		if storage[message.from_user.id] == "Weather":
			await bot.send_message(message.chat.id, text=await weather_scrap(message))
		if storage[message.from_user.id] == "Wikipedia":
			await bot.send_message(message.chat.id, text=await send_info_from_wikipedia(message))
	except Exception as e:
		print(e)
		await bot.send_message(chat_id=message.chat.id, message_id=message.id, text=f"Ошибка: \n{str(e)}")



@bot.callback_query_handler(func = lambda call:True)
async def call_streams(call: types.CallbackQuery):
	try:
		if "youtube.com" in call.data or "youtu.be" in call.data:
			await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=call.data) 
			await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=keyboards.res)
		if call.data == 'Video':
			buffer: BytesIO = await download_youtube_video(call.message.text)
			await bot.send_video(call.message.chat.id, buffer.getvalue())
			buffer.flush()
		if call.data == 'Audio':
			buffer: BytesIO = await download_youtube_audio_only(call.message.text)
			await bot.send_audio(call.message.chat.id, buffer.getvalue())
			buffer.flush()
	except Exception as e:
		print(e)
		await bot.send_message(chat_id=call.message.chat.id, message_id=call.message.id, text=f"Ошибка: \n{str(e)}")

		
async def main():
	await bot.polling()

if __name__ == "__main__":
	asyncio.run(main())

asyncio.run(bot.polling(none_stop=True))

# updater = Updater(token='TOKEN', request_kwargs={'read_timeout': 1000, 'connect_timeout': 1000})