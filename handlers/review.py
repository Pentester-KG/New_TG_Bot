from aiogram import Router, types, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from handlers.keyboard import quality
from config import database

survey_router = Router()


class FoodReview(StatesGroup):
    name = State()
    phone_num = State()
    visit_date = State()
    quality_food = State()
    cleanliness = State()
    comment = State()


@survey_router.callback_query(F.data == 'review')
async def start_survey(call_back: types.CallbackQuery, state: FSMContext):
    await call_back.answer()
    await state.set_state(FoodReview.name)
    await call_back.message.answer("Как вас зовут?")


@survey_router.message(FoodReview.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(FoodReview.phone_num)
    await message.answer(f" Ваш номер телефона или инстаграм?")


@survey_router.message(FoodReview.phone_num)
async def num_of_phone(message: types.Message, state: FSMContext):
    await state.update_data(num_of_phone=message.text)
    await state.set_state(FoodReview.visit_date)
    await message.answer('Когда вы посещали чайхану?(введите цифрами)')


@survey_router.message(FoodReview.visit_date)
async def show_date(message: types.Message, state: FSMContext):
    await state.update_data(date_visit=message.text)
    date_of_visit = message.text
    if not date_of_visit.isdigit():
        await message.answer('Введите в числовом формате!\nНапример: (01012024)')
        return
    await state.set_state(FoodReview.quality_food)
    await message.answer('Как оцениваете качество еды', reply_markup=quality)


@survey_router.message(FoodReview.quality_food)
async def quality_dish(message: types.Message, state: FSMContext):
    await state.update_data(quality=message.text)
    await state.set_state(FoodReview.cleanliness)
    await message.answer(f"Как оцениваете чистоту заведения?", reply_markup=quality)


@survey_router.message(FoodReview.cleanliness)
async def clean(message: types.Message, state: FSMContext):
    await state.update_data(purity=message.text)
    await state.set_state(FoodReview.comment)
    await message.answer("Напишите ваше предложение ли жалобу.")


@survey_router.message(FoodReview.comment)
async def wrote_comment(message: types.Message, state: FSMContext):
    await state.update_data(commentarii=message.text)
    data = await state.get_data()
    await database.execute(
        "INSERT INTO review (name, number, date_of_visit, quality_food, quality_clean) VALUES (?, ?, ?, ?, ?)",
        (data["name"], data["num_of_phone"], data["date_visit"], data["quality"], data["purity"])
    )
    await message.answer("Спасибо за пройденный опрос!")
    await state.clear()
    await message.answer('Спасибо за отзыв!')