from aiogram import types


def start_keyboard():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш адрес", url="https://navat.kg/branches-bishkek.html?block"
                                                                 "=rec666375674")
            ],
            [
                types.InlineKeyboardButton(text="Наш инстаграм", url="https://www.instagram.com/navat_kg/")
            ],
            [
                types.InlineKeyboardButton(text="О нас", url="https://navat.kg/?ysclid=lumhkk1gjb761511759"
                                                             "#rec666375402")
            ],
            [
                types.InlineKeyboardButton(text="Контакты", callback_data="contacts")
            ],
            [
                types.InlineKeyboardButton(text='Отзывы', url="https://yandex.ru/maps/org/chaykhana_navat/"
                                                              "230215048592/reviews/?ll=74.596227%2C42.874087&z=16")
            ],
            [
                types.InlineKeyboardButton(text='Оставить отзыв', callback_data='review')
            ]
        ]
    )
    return kb


kb_menu = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text='Европейская кухня')
        ],
        [
            types.KeyboardButton(text='Десерты'),
            types.KeyboardButton(text='Салаты')
        ],
        [
            types.KeyboardButton(text="Восточная кухня"),
            types.KeyboardButton(text="Напитки")
        ]
    ],
    resize_keyboard=True, one_time_keyboard=True
)

f1 = "https://mir-s3-cdn-cf.behance.net/project_modules/1400/80f05068842953.5b6b329a45b56.jpg"
f3 = "https://image.isu.pub/110112115448-20f721acc5e94901b1ec52883355719a/jpg/page_4.jpg"
f4 = "https://i.ytimg.com/vi/Q0Zpn57MDIM/maxresdefault.jpg"
f5 = "https://old.peretz-group.ru/files/uploads/japengo/desert/desrt01.jpg"
f6 = "https://gcdn.tomesto.ru/img/place/000/023/021/kafe-shooga-na-pulkovskom-shosse_f0eb6_full-186443.jpg"


quality = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text='Ужасно')
        ],
        [
            types.KeyboardButton(text="Удовлетворительно")
        ],
        [
            types.KeyboardButton(text="Хорошо")
        ],
        [
            types.KeyboardButton(text="Отлично")
        ]

    ], resize_keyboard=True, one_time_keyboard=True
)
