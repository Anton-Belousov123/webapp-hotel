from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot(token='6215708830:AAGKSA7XfghK_TMBu3obT8-Vs7dbyk5Or2s')

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://hotel-bot.site/')))
    await message.answer('Привет мой друг!', reply_markup=keyboard)


executor.start_polling(dp)

