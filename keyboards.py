from telebot import types
btn1 = types.KeyboardButton("/help (помощь)")
btn2 = types.KeyboardButton("/start (начать)")

menu = types.ReplyKeyboardMarkup()
menu.add(btn1,btn2)

p144 = types.InlineKeyboardButton('144')
p240 = types.InlineKeyboardButton('240')
p360 = types.InlineKeyboardButton('360')
p480 = types.InlineKeyboardButton('480')
p720 = types.InlineKeyboardButton('720')
p1080= types.InlineKeyboardButton('1080')

res = types.InlineKeyboardMarkup(row_width=2)
res.add(p144,p240,p360,p480,p720,p1080)
