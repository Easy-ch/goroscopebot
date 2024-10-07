from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from bs4 import BeautifulSoup
import requests
from config import TOKEN
from aiogram.client.default import DefaultBotProperties
import asyncio

bot = Bot(token=TOKEN,default=DefaultBotProperties(parse_mode='HTML'))
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)
    
async def on_shutdown(dp):
    await bot.delete_webhook()


@dp.message(CommandStart())
async def start_message(message: types.Message):
    await message.answer(
        "Привет " + message.from_user.first_name + " выбери свой знак зодиака" '\n' + """
        ♈️ Овен \n
        ♉ Телец \n
        ♊ Близнецы \n
        ♋️ Рак \n
        ♌ Лев \n
        ♍ Дева \n
        ♎ Весы\n
        ♏ Скорпион \n
        ♐ Стрелец \n
        ♑ Козерог \n
        ♒ Водолей\n
        ♓ Рыбы \n
    """
    )

async def fetch_horoscope(sign: str, url: str):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    find = soup.findAll('p')
    return find[0].get_text(strip=True) if find else "Информация недоступна"

# Define message handlers for each zodiac sign
@dp.message(F.text == 'Овен')
async def oven(message: types.Message):
    result_text = await fetch_horoscope('Овен', 'https://horo.mail.ru/prediction/aries/today/')
    await message.answer(f'Вот, что говорят звезды про {message.text}:\n{result_text}')

@dp.message(F.text == 'Телец')
async def taurus(message: types.Message):
    result_text = await fetch_horoscope('Телец', 'https://horo.mail.ru/prediction/taurus/today/')
    await message.answer(f'Вот, что говорят звезды про {message.text}:\n{result_text}')

@dp.message(F.text == 'Близнецы')
async def gemini(message: types.Message):
    result_text = await fetch_horoscope('Близнецы', 'https://horo.mail.ru/prediction/gemini/today/')
    await message.answer(f'Вот, что говорят звезды про {message.text}:\n{result_text}')

@dp.message(F.text == 'Рак')
async def cancer(message: types.Message):
    result_text = await fetch_horoscope('Рак', 'https://horo.mail.ru/prediction/cancer/today/')
    await message.answer(f'Вот, что говорят звезды про {message.text}:\n{result_text}')

@dp.message(F.text == 'Лев')
async def leo(message: types.Message):
    result_text = await fetch_horoscope('Лев', 'https://horo.mail.ru/prediction/leo/today/')
    await message.answer(f'Вот, что говорят звезды про {message.text}:\n{result_text}')

@dp.message(F.text == 'Дева')
async def virgo(message: types.Message):
    result_text = await fetch_horoscope('Дева', 'https://horo.mail.ru/prediction/virgo/today/')
    await message.answer(f'Вот, что говорят звезды про {message.text}:\n{result_text}')

@dp.message(F.text == 'Весы')
async def libra(message: types.Message):
    result_text = await fetch_horoscope('Весы', 'https://horo.mail.ru/prediction/libra/today/')
    await message.answer(f'Вот, что говорят звезды про {message.text}:\n{result_text}')

@dp.message(F.text == 'Скорпион')
async def scorpio(message: types.Message):
    result_text = await fetch_horoscope('Скорпион', 'https://horo.mail.ru/prediction/scorpio/today/')
    await message.answer(f'Вот, что говорят звезды про {message.text}:\n{result_text}')

@dp.message(F.text == 'Стрелец')
async def sagittarius(message: types.Message):
    result_text = await fetch_horoscope('Стрелец', 'https://horo.mail.ru/prediction/sagittarius/today/')
    await message.answer(f'Вот, что говорят звезды про {message.text}:\n{result_text}')

@dp.message(F.text == 'Козерог')
async def capricorn(message: types.Message):
    result_text = await fetch_horoscope('Козерог', 'https://horo.mail.ru/prediction/capricorn/today/')
    await message.answer(f'Вот, что говорят звезды про {message.text}:\n{result_text}')

@dp.message(F.text == 'Водолей')
async def aquarius(message: types.Message):
    result_text = await fetch_horoscope('Водолей', 'https://horo.mail.ru/prediction/aquarius/today/')
    await message.answer(f'Вот, что говорят звезды про {message.text}:\n{result_text}')

@dp.message(F.text == 'Рыбы')
async def pisces(message: types.Message):
    result_text = await fetch_horoscope('Рыбы', 'https://horo.mail.ru/prediction/pisces/today/')
    await message.answer(f'Вот, что говорят звезды про {message.text}:\n{result_text}')


if __name__ == '__main__':
    
