
import logging
from handlers.start import start_router
import asyncio
from config import dp, bot, set_my_menu, database
from handlers.menu import menu_router
from handlers.review import survey_router
from aiogram import Bot
from handlers.myinfo import info_router


async def on_startup(bot: Bot):
    await database.create_tables()


async def main():
    await set_my_menu()

    # запуск бота
    dp.include_router(start_router)
    dp.include_router(info_router)
    dp.include_router(menu_router)
    dp.include_router(survey_router)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')