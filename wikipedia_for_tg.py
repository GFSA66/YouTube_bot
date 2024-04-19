import telebot
import wikipedia
from telebot import types

async def send_info_from_wikipedia(message: types.Message):
    try:
        # Устанавливаем язык Wikipedia на русский
        wikipedia.set_lang("ru")
        # Получаем краткую информацию из Википедии
        search_result = wikipedia.summary(message.text)
        return search_result
    #except wikipedia.exceptions.DisambiguationError as e:
    #    # Если есть неоднозначность в запросе, то выводим возможные варианты
    #    result = f'Уточните ваш запрос. Возможно вы имели в виду: {', '.join(e.options)}'
    #    return result
    #    await bot.send_message(message, f"Уточните ваш запрос. Возможно вы имели в виду: {', '.join(e.options)}")
    #except wikipedia.exceptions.PageError:
    #    # Если страница не найдена, сообщаем об этом
    #    await bot.send_message(message, "Информация по вашему запросу не найдена.")
    except Exception as e:
        print(e)
        return e
