from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
from pathlib import Path
from database.database import Database


load_dotenv()
dev = getenv('DEV')
if not bool(dev):
        from aiogram.client.session.aiohttp import AiohttpSession

        print("Production ready")
        session = AiohttpSession(proxy=getenv('PROXY'))
        bot = Bot(token=getenv('BOT_TOKEN'), session=session)
else:
        bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()
database = Database(
    Path(__file__).parent / 'results.db'
)


async def set_my_menu():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Начало"),
        types.BotCommand(command="menu", description="Показать меню")
    ])