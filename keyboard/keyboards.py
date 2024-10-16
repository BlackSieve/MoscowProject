from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

board = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Игра "Тотем"'), KeyboardButton(text='Картинка животного')],
    [KeyboardButton(text='История'), KeyboardButton(text='Тех.поддержка Зоопарка')],
    [KeyboardButton(text='Опекун животных'), KeyboardButton(text='Навигация по мне')],
    [KeyboardButton(text='Оставить отзыв')]
],
    resize_keyboard=True,
    input_field_placeholder='Воспользуйтесь меню ниже')

back = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Главное меню')]
],
    resize_keyboard=True,
    input_field_placeholder='Воспользуйтесь меню ниже')

play = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Старт!')],
    [KeyboardButton(text='Главное меню')]
],
    resize_keyboard=True,
    input_field_placeholder='Воспользуйтесь меню ниже')

replay = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Ещё раз!')],
    [KeyboardButton(text='Главное меню')]
],
    resize_keyboard=True,
    input_field_placeholder='Воспользуйтесь меню ниже')

photo = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Хочу животного')],
    [KeyboardButton(text='Главное меню')]
],
    resize_keyboard=True,
    input_field_placeholder='Воспользуйтесь меню ниже')

game_final = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Узнать результат')],
    [KeyboardButton(text='Главное меню')]
],
    resize_keyboard=True,
    input_field_placeholder='Выберите ответ')

feedback = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Главное меню')]
],
    resize_keyboard=True,
    input_field_placeholder='Оставить отзыв')



guardian = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Опекун', url='https://moscowzoo.ru/about/guardianship')]
])

info_url = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Зоопарк', url='https://moscowzoo.ru')]
])
