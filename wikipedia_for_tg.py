import wikipedia
from telebot import types

async def send_info_from_wikipedia(message: types.Message):
    try:
        # Устанавливаем язык Wikipedia на русский
        wikipedia.set_lang("uk")
        # Получаем краткую информацию из Википедии
        search_result = wikipedia.summary(message.text)
        return search_result
    except Exception as e:
        print(e)
        return e