from aiogram import Router, types, F
from aiogram.filters import Command
from parser.crawler import HouseCrawler
from handlers.keyboard import start_keyboard
import asyncio


info_router = Router()


@info_router.message(Command('myinfo'))
async def myinfo_cmd(message: types.Message):
    user = message.from_user
    info_message = f'Ваш id: {user.id}\nВаше имя: {user.first_name}\n'
    if user.username:
        info_message += f'Ваш никнейм: @{user.username}'
    await message.answer(info_message)


@info_router.callback_query(F.data == 'send_links')
async def send_link(callback: types.CallbackQuery):
    await callback.answer()
    crawler = HouseCrawler()
    # await crawler.get_page()
    # await crawler.get_house()
    house_links = await crawler.get_house()
    for link in house_links:
        await callback.message.answer(link)
