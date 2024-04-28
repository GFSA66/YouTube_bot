from io import BytesIO
from sclib import SoundcloudAPI, Track, Playlist
# 'https://soundcloud.com/itsmeneedle/sunday-morning'
api = SoundcloudAPI()  
def download_soundCloud_audio(url):
	try:
		track = api.resolve(url)
		assert type(track) is Track
		filename = f'./{track.artist} - {track.title}.mp3'
		with open(filename, 'wb+') as file:
			track.write_mp3_to(file)
		return filename
	except Exception as e:
		print(e)
		return e