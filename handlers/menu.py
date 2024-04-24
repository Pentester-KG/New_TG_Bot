from aiogram import Router, F, types
from aiogram.filters import Command
from handlers.keyboard import kb_menu
from config import database


menu_router = Router()


@menu_router.message(Command('menu'))
async def menu(message: types.Message):
    await message.answer('Наше меню', reply_markup=kb_menu)


f1 = "https://mir-s3-cdn-cf.behance.net/project_modules/1400/80f05068842953.5b6b329a45b56.jpg"
f3 = "https://image.isu.pub/110112115448-20f721acc5e94901b1ec52883355719a/jpg/page_4.jpg"
f4 = "https://i.ytimg.com/vi/Q0Zpn57MDIM/maxresdefault.jpg"
f5 = "https://old.peretz-group.ru/files/uploads/japengo/desert/desrt01.jpg"
f6 = "https://gcdn.tomesto.ru/img/place/000/023/021/kafe-shooga-na-pulkovskom-shosse_f0eb6_full-186443.jpg"


categories = ['салаты', 'европейская кухня', 'восточная кухня', 'напитки', 'десерты']


@menu_router.message(F.text.lower().in_(categories))
async def show_category(message: types.Message):
    category = message.text
    data = await database.fetch(
       """
       SELECT Dishes.* FROM Dishes
       JOIN category ON Dishes.category_id = category.id
       WHERE category.name = ?
       """, (category,), fetch_type='all'
    )

    await message.answer(f'Наше меню📕 {category}')
    for dish in data:
        price = dish['price']
        name = dish['name']
        photo = types.FSInputFile(dish['picture'])
        await message.answer_photo(photo=photo, caption=f'Название: {name}\nЦена: {price}')

# @menu_router.message(F.text.lower() == 'салаты')
# async def show_salads(message: types.Message):
#     await message.answer_photo(photo=f1, caption='Меню салатов')
#
#
# @menu_router.message(F.text.lower() == 'европейская кухня')
# async def show_eu_kitchen(message: types.Message):
#     await message.answer_photo(photo=f3, caption='Европейская кухня')
#
#
# @menu_router.message(F.text.lower() == 'восточная кухня')
# async def show_east_kitchen(message: types.Message):
#     await message.answer_photo(photo=f4, caption='Восточная кухня')
#
#
# @menu_router.message(F.text.lower() == 'напитки')
# async def show_juices(message: types.Message):
#     await message.answer_photo(photo=f6, caption='Напитки')
#
#
# @menu_router.message(F.text.lower() == 'десерты')
# async def show_deserts(message: types.Message):
#     await message.answer_photo(photo=f5, caption='Десерты')
