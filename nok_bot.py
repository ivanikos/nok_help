# -*- coding: utf8 -*-

import logging
import os
import csv
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.contrib.fsm_storage.memory import MemoryStorage




class CheckStigma(StatesGroup):
    wait_stigma = State()


bot = Bot(token='5914620881:AAGXJr10d1cCTOB4gd3A37p4ypNKjh_J1ak')  # Токен  бота checkwelder

dp: Dispatcher = Dispatcher(bot, storage=MemoryStorage())

logging.basicConfig(level=logging.INFO)

btnHlp = KeyboardButton('Help')
btnDon = KeyboardButton('Donate')

help_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).row(btnHlp)

greet_me = ['Хозяин', 'Иван Александрович']
boss_id = 799592984


@dp.message_handler(commands='start')
async def start_using(message: types.Message):
    if message.from_user.id == 799592984:
        await message.answer('Приветствую. Работает 09.09.22', reply_markup=help_kb)
    else:
        await message.answer('Привет. Пиши Код вопроса:', reply_markup=help_kb)
        await bot.send_message(799592984, f'Кто-то нажал старт user_id - {message.from_user.id}, \n'
                                          f'user_name - {message.from_user.username}')


@dp.message_handler()
async def help_command(message: types.Message):
    if message.text == 'Help':
        writeBtn = InlineKeyboardButton('Написать разработчику', url='telegram.me/ivanikos')

        write_kb = InlineKeyboardMarkup().add(writeBtn)
        await message.answer('Пока что это все, что можно выбрать:', reply_markup=write_kb)
    elif message.text == 'Donate':
        await message.answer('Пока не работает. Жми HELP.')
    else:
        try:
            photo = open(f".\\screen_questions\\{message.text}.png", "rb")
            await bot.send_photo(message.from_user.id, photo)
        except Exception as e:
            # print(e)
            await message.answer('Не пойму чего ты хочешь, пиши код вопроса:')



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)