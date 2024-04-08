from telebot import types
from config import TOKEN
btn1 = types.KeyboardButton("/help (помощь)")
btn2 = types.KeyboardButton("/start (начать)")

import main

menu = types.ReplyKeyboardMarkup()
menu.add(btn1,btn2)

p144 = types.InlineKeyboardButton('144',callback_data="144")
p240 = types.InlineKeyboardButton('240',callback_data="240")
p360 = types.InlineKeyboardButton('360',callback_data="360")
p480 = types.InlineKeyboardButton('480',callback_data="480")
p720 = types.InlineKeyboardButton('720',callback_data="720")
p1080= types.InlineKeyboardButton('1080',callback_data="1080")

res = types.InlineKeyboardMarkup(row_width=2)
res.add(p144,p240,p360,p480,p720,p1080)

@main.bot.callback_query_handler(func = lambda call:True)
async def call_streams(call):
    if call.data =='link':
        await main.bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id,text= "Choose: ",reply_markup=res)
