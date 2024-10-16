from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

question1 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='A) В джунглях или лесу.'), KeyboardButton(text='B) В воде или возле водоёмов.')],
    [KeyboardButton(text='C) На открытых просторах.'), KeyboardButton(text='D) В уютной норке.')]
],
    resize_keyboard=True,
    input_field_placeholder='Выберите ответ снизу')

question2 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='A) Фрукты и овощи.'), KeyboardButton(text='B) Мясо и рыба.')],
    [KeyboardButton(text='C) Насекомые и мелкие животные.'), KeyboardButton(text='D) Всё, что можно найти.')]
],
    resize_keyboard=True,
    input_field_placeholder='Выберите ответ снизу')

question3 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='A) Высоко в деревьях или на скале.'),
     KeyboardButton(text='B) Глубоко под водой или возле неё.')],
    [KeyboardButton(text='C) На открытой равнине или в горах.'),
     KeyboardButton(text='D) В тёплой норке или уютной пещере.')]
],
    resize_keyboard=True,
    input_field_placeholder='Выберите ответ снизу')

question4 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='A) Изучать новые места и вещи.'),
     KeyboardButton(text='B) Плавать или заниматься водными видами спорта.')],
    [KeyboardButton(text='C) Бегать или заниматься активными видами спорта.'),
     KeyboardButton(text='D) Искать уютные уголки и отдыхать.')]
],
    resize_keyboard=True,
    input_field_placeholder='Выберите ответ снизу')

question5 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='A) Путешествия и приключения.'), KeyboardButton(text='B) Расслабление у воды.')],
    [KeyboardButton(text='C) Активные игры и соревнования.'), KeyboardButton(text='D) Спокойный отдых дома.')]
],
    resize_keyboard=True,
    input_field_placeholder='Выберите ответ снизу')

question6 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='A) Стараюсь уладить конфликт мирным путём.'),
     KeyboardButton(text='B) Защищаю себя и свою территорию.')],
    [KeyboardButton(text='C) Быстро реагирую и принимаю решения.'),
     KeyboardButton(text='D) Предпочитаю избегать конфликтов.')]
],
    resize_keyboard=True,
    input_field_placeholder='Выберите ответ снизу')

question7 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='A) Утро, когда всё просыпается.'),
     KeyboardButton(text='B) Вечер, когда можно расслабиться.')],
    [KeyboardButton(text='C) День, когда можно быть активным.'), KeyboardButton(text='D) Ночь, когда тихо и спокойно.')]
],
    resize_keyboard=True,
    input_field_placeholder='Выберите ответ снизу')
