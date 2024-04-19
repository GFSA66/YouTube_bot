from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def weather(city):
    city = city.replace(" ", "+")
    res = requests.get(f'https://www.google.ru/search?q={city}+погода', headers=headers)
    print("Searching in google......\n")
    soup = BeautifulSoup(res.text, 'html.parser')   
    
    # Изменим селекторы, чтобы соответствовать измененной структуре страницы
    location = soup.select('.BNeawe.iBp4i.AP7Wnd')[0].getText().strip()  
    time = soup.select('.BNeawe.tAd8D.AP7Wnd')[0].getText().strip()       
    info = soup.select('.BNeawe.tAd8D.AP7Wnd')[1].getText().strip() 
    weather = soup.select('.BNeawe.iBp4i.AP7Wnd')[1].getText().strip()
    
    print(location)
    print(time)
    print(info)

print("Введите название города")
city = input()
weather(city)
