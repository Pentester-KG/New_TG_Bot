
from aiogram import Router, F, types
from aiogram.filters import Command
from handlers.keyboard import start_keyboard


start_router = Router()


@start_router.message(Command('start'))
async def start_cmd(message: types.Message):
    await message.answer(f'Привет!, {message.from_user.first_name}', reply_markup=start_keyboard())


@start_router.callback_query(F.data == 'contacts')
async def contacts(call_back: types.CallbackQuery):
    await call_back.answer()
    await call_back.message.answer('+996 (551) 83 11 11')