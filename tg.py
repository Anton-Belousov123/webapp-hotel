import time
import amo
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot(token='5750853621:AAGifNbBkrsfjs-pddUmcSwmdyzTxaGSYXA')

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def h_c(m: types.message):
    keyword = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyword.add(types.KeyboardButton('Зарегистрироваться в WebApp'))
    await m.answer('Привет мой друг!', reply_markup=keyword)


@dp.message_handler(lambda m: m.text == 'Зарегистрироваться в WebApp')
async def start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://hotel-bot.site/')))
    await message.answer('Открыть WebApp!', reply_markup=keyboard)


@dp.message_handler()
async def gr(message: types.Message):
    if 'Я хочу заказать ' in message.text:
        order = message.text.replace('Я хочу заказать ', '')
        print(message)
        amo.make_order(f"{message.from_user.username} {message.from_user.first_name} {message.from_user.last_name}")
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(
            types.InlineKeyboardButton('Подтвердить', url='https://api.whatsapp.com/send?phone=905398266855&text=Здравствуйте! Мне нужна информация о недвижимости'))
        await message.answer(f"Спасибо за ваш заказ! ({order})", reply_markup=keyboard)


executor.start_polling(dp)

