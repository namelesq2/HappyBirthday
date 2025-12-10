from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
import os
logging.basicConfig(level=logging.INFO)
TOKEN = "8255077780:AAEMFtr-3FP2BDwBdT15kPzOwaHMudZpR8I"  # <-- вставь токен бота
WEBAPP_URL = "https://your-domain.com/index.html"  # <-- ссылка на хостинг мини-приложения
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    text = (
        "Привет, хочу поздравить тебя с днём рождения от себя, я телеграм-бот, "
        "которого написал один очень хороший человек) "
        "Этот человек тебя очень любит и сделал очень необычный подарок, "
        "поэтому запускай мини приложение и смотри, что для тебя подготовил Артём)."
    )
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Открыть поздравление 🎁", web_app=types.WebAppInfo(url=WEBAPP_URL))
    kb.add(btn)
    await message.answer(text, reply_markup=kb)
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)