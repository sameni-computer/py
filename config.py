from telebot import *
import time

TOKEN = "834251861:AZlTHZCoxmCJ3AnjklV3z8LYftR4EG4XKVy6sjee"

salavat_box= telebot.types.InlineKeyboardMarkup(row_width=1)
salavat1 = telebot.types.InlineKeyboardButton(text="📿صلوات 5📿"   , callback_data="D5")
salavat2 = telebot.types.InlineKeyboardButton(text="📿صلوات 14📿"  , callback_data="D14")
salavat3 = telebot.types.InlineKeyboardButton(text="📿صلوات 110📿" , callback_data="D110")
salavat4 = telebot.types.InlineKeyboardButton(text="📿صلوات 313📿" , callback_data="D313")
salavat_box.add(salavat1 , salavat2 , salavat3 , salavat4)

