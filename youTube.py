from telebot import types
from pytube import YouTube
from youtubesearchpython import VideosSearch
from io import BytesIO

async def search_youtube_content(message: types.Message):
	searchList = VideosSearch(message.text, limit = 10).result()['result']
	keyboard = list()
	for element in searchList:
		a = [types.InlineKeyboardButton(text=element['title'], callback_data=element['link'])]
		keyboard.append(a)
	choose_markup =  types.InlineKeyboardMarkup(keyboard,1)
	return choose_markup

async def download_youtube_video(url):
	try:
		yt = YouTube(url)
		stream = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()
		buffer = BytesIO()
		stream.stream_to_buffer(buffer)
		return buffer
	except Exception as e:
		print(e)
		return e
		
async def download_youtube_audio_only(url):
	try:
		yt = YouTube(url)
		stream = yt.streams.filter(only_audio=True).first()
		buffer = BytesIO()
		stream.stream_to_buffer(buffer)
		return buffer
	except Exception as e:
		print(e)
		return e