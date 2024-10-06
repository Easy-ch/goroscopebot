from aiogram import Bot,Dispatcher,types
from aiogram.dispatcher.filters import CommandStart
from aiogram.utils.executor import start_webhook
from aiogram.types import ParseMode
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from bs4 import BeautifulSoup
import requests
from config import TOKEN


bot = Bot(token=TOKEN,parse_mode=ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot,storage=storage)


WEBHOOK_HOST = 'https://4fe6-188-243-182-2.ngrok-free.app'
WEBHOOK_PATH = f'/{TOKEN}'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = 'localhost'  # or ip
WEBAPP_PORT = 8000

async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(dp):
    await bot.delete_webhook()


@dp.message_handler(CommandStart())
async def start_message(message:types.Message):
    await message.answer("Привет " + message.from_user.first_name + " выбери свой знак зодиака" '\n' + """
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
""" )

@dp.message_handler(lambda msg: msg.text=='Овен')
async def oven(message:types.Message):
    url = 'https://horo.mail.ru/prediction/aries/today/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    find = soup.findAll('p')
    if find:
        result_text = find[0].get_text(strip=True)
        await message.answer(f'Вот, что говорят звезды про {message.text}:\n{result_text}')



@dp.message_handler(lambda msg: msg.text=='Телец')
async def oven(message:types.Message):
    url = 'https://horo.mail.ru/prediction/taurus/today/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    find = soup.findAll('p')
    if find:
        result_text = find[0].get_text(strip=True)
        await message.answer(f'Вот, что говорят звезды про {message.text}:\n{result_text}')


@dp.message_handler(lambda msg: msg.text=='Близнецы')
async def oven(message:types.Message):
    url = 'https://horo.mail.ru/prediction/gemini/today/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    find = soup.findAll('p')
    if find:
        result_text = find[0].get_text(strip=True)
        await message.answer(f'Вот, что говорят звезды про {message.text}:\n{result_text}')


@dp.message_handler(lambda msg: msg.text=='Рак')
async def oven(message:types.Message):
    url = 'https://horo.mail.ru/prediction/cancer/today/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    find = soup.findAll('p')
    if find:
        result_text = find[0].get_text(strip=True)
        await message.answer(f'Вот, что говорят звезды про {message.text}:\n{result_text}')


@dp.message_handler(lambda msg: msg.text=='Лев')
async def oven(message:types.Message):
    url = 'https://horo.mail.ru/prediction/leo/today/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    find = soup.findAll('p')
    if find:
        result_text = find[0].get_text(strip=True)
        await message.answer(f'Вот, что говорят звезды про {message.text}:\n{result_text}')

@dp.message_handler(lambda msg: msg.text=='Дева')
async def oven(message:types.Message):
    url = 'https://horo.mail.ru/prediction/virgo/today/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    find = soup.findAll('p')
    if find:
        result_text = find[0].get_text(strip=True)
        await message.answer(f'Вот, что говорят звезды про {message.text}:\n{result_text}')

@dp.message_handler(lambda msg: msg.text=='Весы')
async def oven(message:types.Message):
    url = 'https://horo.mail.ru/prediction/libra/today/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    find = soup.findAll('p')
    if find:
        result_text = find[0].get_text(strip=True)
        await message.answer(f'Вот, что говорят звезды про {message.text}:\n{result_text}')
    
@dp.message_handler(lambda msg: msg.text=='Скорпион')
async def oven(message:types.Message):
    url = 'https://horo.mail.ru/prediction/scorpio/today/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    find = soup.findAll('p')
    if find:
        result_text = find[0].get_text(strip=True)
        await message.answer(f'Вот, что говорят звезды про {message.text}:\n{result_text}')


@dp.message_handler(lambda msg: msg.text=='Стрелец')
async def oven(message:types.Message):
    url = 'https://horo.mail.ru/prediction/sagittarius/today/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    find = soup.findAll('p')
    if find:
        result_text = find[0].get_text(strip=True)
        await message.answer(f'Вот, что говорят звезды про {message.text}:\n{result_text}')


@dp.message_handler(lambda msg: msg.text=='Козерог')
async def oven(message:types.Message):
    url = 'https://horo.mail.ru/prediction/capricorn/today/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    find = soup.findAll('p')
    if find:
        result_text = find[0].get_text(strip=True)
        await message.answer(f'Вот, что говорят звезды про {message.text}:\n{result_text}')


@dp.message_handler(lambda msg: msg.text=='Водолей')
async def oven(message:types.Message):
    url = 'https://horo.mail.ru/prediction/aquarius/today/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    find = soup.findAll('p')
    if find:
        result_text = find[0].get_text(strip=True)
        await message.answer(f'Вот, что говорят звезды про {message.text}:\n{result_text}')


@dp.message_handler(lambda msg: msg.text=='Рыбы')
async def oven(message:types.Message):
    url = 'https://horo.mail.ru/prediction/pisces/today/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    find = soup.findAll('p')
    if find:
        result_text = find[0].get_text(strip=True)
        await message.answer(f'Вот, что говорят звезды про {message.text}:\n{result_text}')



if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )