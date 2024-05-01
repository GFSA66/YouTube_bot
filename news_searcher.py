from GoogleNews import GoogleNews, ResultSet
from telebot import types

async def search_news(message: types.Message):
    try:
        print("ok")
        googlenews = GoogleNews(lang='uk', period='d', region='Ukraine')
        googlenews.search(message)
        result = googlenews.result()[0]
        return f"{result.get('link').lower()}"
    except Exception as e:
        print(e)
        return e