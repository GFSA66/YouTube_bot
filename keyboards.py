from telebot import types

btn1 = types.KeyboardButton("/help (помощь)")
btn2 = types.KeyboardButton("/start (начать)")

menu = types.ReplyKeyboardMarkup()
menu.add(btn1,btn2)

resolutions = ['144', '240', '360', '480', '720', '1080']
download_choose = ['Video','Audio']
emojies = ['🎦','🎧']
choose_what_you_wanna_do = ['YouTube','Weather']

res = types.InlineKeyboardMarkup(row_width=2)
yourchoose = types.InlineKeyboardMarkup()
i=0
a=0
for resolution in download_choose:
    res.add(types.InlineKeyboardButton(emojies[i]+resolution, callback_data=resolution))
    i+=1
for resolution in choose_what_you_wanna_do:
    yourchoose.add(types.InlineKeyboardButton(resolution, callback_data=resolution))
    a+=1