from telebot import types
from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

async def weather_scrap(message: types.Message):
    city = message.text.replace(" ", "+")
    res = requests.get(f'https://www.google.ru/search?q={city}+погода', headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')   
    
    # Изменим селекторы, чтобы соответствовать измененной структуре страницы
    location = soup.select('.BNeawe.iBp4i.AP7Wnd')[0].getText().strip()  
    time = soup.select('.BNeawe.tAd8D.AP7Wnd')[0].getText().strip()       
    info = soup.select('.BNeawe.tAd8D.AP7Wnd')[1].getText().strip() 
    weather = soup.select('.BNeawe.iBp4i.AP7Wnd')[1].getText().strip()
    return f'{location}\n{time}\n{info}\n'
    