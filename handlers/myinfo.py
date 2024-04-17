from aiogram import Router, types
from aiogram.filters import Command

info_router = Router()


@info_router.message(Command('myinfo'))
async def myinfo_cmd(message: types.Message):
    user = message.from_user
    info_message = f'Ваш id: {user.id}\nВаше имя: {user.first_name}\n'
    if user.username:
        info_message += f'Ваш никнейм: @{user.username}'
    await message.answer(info_message)
