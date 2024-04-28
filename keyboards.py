from telebot import types

btn1 = types.KeyboardButton("/help (помощь)")
btn2 = types.KeyboardButton("/start (начать)")

menu = types.ReplyKeyboardMarkup()
menu.add(btn1,btn2)

resolutions = ['144', '240', '360', '480', '720', '1080']
download_choose = ['Video','Audio']
emojies = ['🎦','🎧']

choose_what_you_wanna_do = ['YouTube','Weather','Wikipedia', 'GoogleNews']

res = types.InlineKeyboardMarkup(row_width=2)
yourchoose = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

for index, resolution in enumerate(download_choose):
    res.add(types.InlineKeyboardButton(emojies[index]+resolution, callback_data=resolution))
for index, choose in enumerate(choose_what_you_wanna_do):
    yourchoose.add(types.KeyboardButton(choose))