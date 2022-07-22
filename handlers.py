from aiogram.types import Message
from random import randint

from main import bot, dp
from config import chat_id

async def start_message(dp):
    await bot.send_message(chat_id=chat_id, text='Hello')

@dp.message_handler()
async def send_messege(message: Message):
    text = message.text
    await message.answer(text=text)