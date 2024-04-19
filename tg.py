import telebot
import wikipedia
import asyncio

# Указываем токен, полученный у BotFather
TOKEN = 'api'
# Инициализируем бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
async def send_welcome(message):
    await bot.reply_to(message, "Привет! Я бот, который отправляет краткую информацию из Википедии. Просто отправь мне слово или фразу, о которой ты хочешь узнать.")

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
async def send_info_from_wikipedia(message):
    try:
        # Устанавливаем язык Wikipedia на русский
        wikipedia.set_lang("ru")
        # Получаем краткую информацию из Википедии
        search_result = wikipedia.summary(message.text)
        await bot.reply_to(message, search_result)
    except wikipedia.exceptions.DisambiguationError as e:
        # Если есть неоднозначность в запросе, то выводим возможные варианты
        await bot.reply_to(message, f"Уточните ваш запрос. Возможно вы имели в виду: {', '.join(e.options)}")
    except wikipedia.exceptions.PageError:
        # Если страница не найдена, сообщаем об этом
        await bot.reply_to(message, "Информация по вашему запросу не найдена.")
    except Exception as e:
        # Если возникает какая-то другая ошибка, выводим сообщение об ошибке
        await bot.reply_to(message, f"Произошла ошибка: {str(e)}")

# Запускаем бота
async def main():
	await bot.polling()

if __name__ == "__main__":
	asyncio.run(main())

asyncio.run(bot.polling(none_stop=True))