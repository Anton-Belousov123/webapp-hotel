import time
import amo
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

import ggl

bot = Bot(token='5750853621:AAGifNbBkrsfjs-pddUmcSwmdyzTxaGSYXA')

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://hotel-bot.site/')))
    await message.answer('Открыть WebApp!', reply_markup=keyboard)


@dp.message_handler()
async def gr(message: types.Message):
    if 'Я хочу заказать ' in message.text:
        order = message.text.replace('Я хочу заказать ', '')
        print(message)
        print(order)
        amo.make_order(f"{message.from_user.username} {message.from_user.first_name} {message.from_user.last_name}",
                       order)
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(
            types.InlineKeyboardButton('Подтвердить',
                                       url=f'https://api.whatsapp.com/send?phone={ggl.read_message_preview().replace("!order!", order)}'))
        await message.answer(f"Спасибо за ваш заказ! ({order})", reply_markup=keyboard)


executor.start_polling(dp)
