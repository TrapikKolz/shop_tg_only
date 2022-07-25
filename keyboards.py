from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from config import KOTIK

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='btn1'),
            KeyboardButton(text='btn2')
        ],
        [
            KeyboardButton(text='btn3')
        ]
    ],
    resize_keyboard=True
)

cb = CallbackData('buy', 'id', 'name', 'price')

keyboard1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Кошечка', callback_data='buy:0:alina:infinity')
        ],
        [
            InlineKeyboardButton(text='Cancel', callback_data='cancel')
        ]
    ]
)

kotik_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Посмотреть', url=KOTIK)
        ]
    ]
)
