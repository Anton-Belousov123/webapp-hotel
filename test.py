import random

import telebot
from aiogram.types import InputMessageContent
from telebot.types import InlineQueryResultArticle, InputTextMessageContent

def send_answer(data):
    try:
        API_TOKEN = '6215708830:AAGKSA7XfghK_TMBu3obT8-Vs7dbyk5Or2s'
        bot = telebot.TeleBot(API_TOKEN, parse_mode="HTML")
        text = f'Я хочу заказать {data["title"]} стоимостью {data["price"]}.'
        bot.answer_web_app_query(
            web_app_query_id=data['query_id'],
            result=InlineQueryResultArticle(
                id=random.randint(10000, 100000),
                title=text,
                input_message_content=InputTextMessageContent(
                    message_text=text
                )
            )
        )
    except:
        pass
