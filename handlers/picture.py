from aiogram import Router, types
from aiogram.filters import Command
import os
import random

picture_1 = Router()


@picture_1.message(Command('picture'))
async def random_pic_cmd(message: types.Message):
    img_dir = 'images'
    img_list = os.listdir(img_dir)
    img_path = os.path.join(img_dir, random.choice(img_list))
    file = types.FSInputFile(img_path)
    await message.answer_photo(photo=file)
