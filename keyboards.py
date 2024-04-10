from telebot import types

btn1 = types.KeyboardButton("/help (помощь)")
btn2 = types.KeyboardButton("/start (начать)")

menu = types.ReplyKeyboardMarkup()
menu.add(btn1,btn2)

resolutions = ['144', '240', '360', '480', '720', '1080']
download_choose = ['video','audio','video + audio']

res = types.InlineKeyboardMarkup(row_width=2)

for resolution in download_choose:
    res.add(types.InlineKeyboardButton(resolution, callback_data=resolution))