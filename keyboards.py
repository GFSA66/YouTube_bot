from telebot import types

btn1 = types.KeyboardButton("/help (помощь)")
btn2 = types.KeyboardButton("/start (начать)")

menu = types.ReplyKeyboardMarkup()
menu.add(btn1,btn2)

resolutions = ['144', '240', '360', '480', '720', '1080']

res = types.InlineKeyboardMarkup(row_width=2)

for resolution in resolutions:
    res.add(types.InlineKeyboardButton(resolution, callback_data=resolution))

