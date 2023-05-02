from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hlink,hcode,hbold,hunderline
from main import check_news_updates
from aiogram.dispatcher.filters import Text
import json

bot = Bot(token='6068000308:AAHuDvOZdrfzYyredshfUXQPRTFp2sYXKe0', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ['Все новости', 'Последняя новость', 'Свежие новости']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer('Лента новостей', reply_markup=keyboard)

@dp.message_handler(Text(equals='Все новости'))
async def get_all_news(message: types.Message):
    with open('news_dict.json') as file:
        news_dict = json.load(file)

    for k, v in sorted(news_dict.items()):
        news = f"Дата новости:{hbold(v['news_date_time'])}\n" \
               f"{hlink(v['news_title'], v['news_url'])}"
        await message.answer(news)

@dp.message_handler(Text(equals='Последняя новость'))
async def get_all_news(message: types.Message):
    with open('news_dict.json') as file:
        news_dict = json.load(file)

    for k, v in sorted(news_dict.items())[-1:]:
        news = f"Дата новости:{hbold(v['news_date_time'])}\n" \
               f"{hlink(v['news_title'], v['news_url'])}"
        await message.answer(news)

@dp.message_handler(Text(equals='Свежие новости'))
async def get_new_news(message: types.Message):
    fresh_news = check_news_updates()

    if len(fresh_news) >= 1:
        for k, v in (fresh_news.items()):
            news = f"Дата новости:{hbold(v['news_date_time'])}\n" \
                   f"{hlink(v['news_title'], v['news_url'])}"
            await message.answer(news)

    else:
        await message.answer('Пока свежих новостей нету :(')


if __name__ == '__main__':
    executor.start_polling(dp)
