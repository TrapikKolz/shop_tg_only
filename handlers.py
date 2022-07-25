from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters import Text, Command

from keyboards import keyboard, keyboard1, kotik_key, cb

from main import bot, dp
from config import chat_id

async def send_hello(dp):
    ''' On startup '''
    await bot.send_message(chat_id=chat_id, text='Hello\nДля старта нажми /cute_kitty')

@dp.message_handler(Command('start'))
async def show_shop(message: Message):
    await message.answer('Hello\nДля старта нажми /cute_kitty')


# Section: ReplyKeyboardMarkup
@dp.message_handler(Command('shop'))
async def show_shop(message: Message):
    await message.answer('Shop', reply_markup=keyboard)

@dp.message_handler(Text(equals=['btn1', 'btn2', 'btn3']))
async def get_goods(message: Message):
    await message.answer(message.text, reply_markup=ReplyKeyboardRemove())

# Section: InlineKeyboardMarkup
@dp.message_handler(Command('cute_kitty'))
async def show(message: Message):
    await message.answer(text='Хочешь увидеть красоту?', reply_markup=keyboard1)

@dp.callback_query_handler(text_contains='alina')
async def phone(call: CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer('Принцесса', reply_markup=kotik_key)

@dp.callback_query_handler(text_contains='cancel')
async def cancel(call: CallbackQuery):
    await call.answer('Отмена', show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)
