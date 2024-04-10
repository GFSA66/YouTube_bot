from telebot import types

btn1 = types.KeyboardButton("/help (помощь)")
btn2 = types.KeyboardButton("/start (начать)")

menu = types.ReplyKeyboardMarkup()
menu.add(btn1,btn2)

resolutions = ['144', '240', '360', '480', '720', '1080']
download_choose = ['Video','Audio']
emojies = ["🎦",'🎧']

res = types.InlineKeyboardMarkup(row_width=2)
i=0
for resolution in download_choose:
    res.add(types.InlineKeyboardButton(emojies[i]+resolution, callback_data=resolution))
    i+=1