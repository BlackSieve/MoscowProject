import random
from aiogram import F, Router
from aiogram.types import Message
import game.game_keyboard as gk
import keyboard.keyboards as kk
from text.offers import end_game, replay_game
from text.animals import animals_low, animals_max, animals_medium
from game.questions_game import questions1, questions2, questions3, questions4, questions5, questions6, questions7

game = Router()
points = 0


# Старт самой игры
@game.message(F.text == 'Старт!')
async def question1(massage: Message):
    await massage.answer(questions1, reply_markup=gk.question1)


# Обработчик ответов
@game.message()
async def aho(massage: Message):
    global points
    if massage == 'A) В джунглях или лесу.':
        points += 1
        await massage.answer(questions2, reply_markup=gk.question2)
    elif massage == 'B) В воде или возле водоёмов.':
        points += 2
        await massage.answer(questions2, reply_markup=gk.question2)
    elif massage == 'C) На открытых просторах.':
        points += 3
        await massage.answer(questions2, reply_markup=gk.question2)
    elif massage == 'D) В уютной норке.':
        points += 4
        await massage.answer(questions2, reply_markup=gk.question2)
    # Обработка ответов на 2 вопрос
    elif massage == 'A) Фрукты и овощи.':
        points += 1
        await massage.answer(questions3, reply_markup=gk.question3)
    elif massage == 'B) Мясо и рыба.':
        points += 2
        await massage.answer(questions3, reply_markup=gk.question3)
    elif massage == 'C) Насекомые и мелкие животные.':
        points += 3
        await massage.answer(questions3, reply_markup=gk.question3)
    elif massage == 'D) Всё, что можно найти.':
        points += 4
        await massage.answer(questions3, reply_markup=gk.question3)
    # Обработка ответов на 3 вопрос
    elif massage == 'A) Высоко в деревьях или на скале.':
        points += 1
        await massage.answer(questions4, reply_markup=gk.question4)
    elif massage == 'B) Глубоко под водой или возле неё.':
        points += 2
        await massage.answer(questions4, reply_markup=gk.question4)
    elif massage == 'C) На открытой равнине или в горах.':
        points += 3
        await massage.answer(questions4, reply_markup=gk.question4)
    elif massage == 'D) В тёплой норке или уютной пещере.':
        points += 4
        await massage.answer(questions4, reply_markup=gk.question4)
    # Обработка ответов на 4 вопрос
    elif massage == 'A) Изучать новые места и вещи.':
        points += 1
        await massage.answer(questions5, reply_markup=gk.question5)
    elif massage == 'B) Плавать или заниматься водными видами спорта.':
        points += 2
        await massage.answer(questions5, reply_markup=gk.question5)
    elif massage == 'C) Бегать или заниматься активными видами спорта.':
        points += 3
        await massage.answer(questions5, reply_markup=gk.question5)
    elif massage == 'D) Искать уютные уголки и отдыхать.':
        points += 4
        await massage.answer(questions5, reply_markup=gk.question5)
    # Обработка ответов на 5 вопрос
    elif massage == 'A) Путешествия и приключения.':
        points += 1
        await massage.answer(questions6, reply_markup=gk.question6)
    elif massage == 'B) Расслабление у воды.':
        points += 2
        await massage.answer(questions6, reply_markup=gk.question6)
    elif massage == 'C) Активные игры и соревнования.':
        points += 3
        await massage.answer(questions6, reply_markup=gk.question6)
    elif massage == 'D) Спокойный отдых дома.':
        points += 4
        await massage.answer(questions6, reply_markup=gk.question6)
    # Обработка ответов на 6 вопрос
    elif massage == 'A) Стараюсь уладить конфликт мирным путём.':
        points += 1
        await massage.answer(questions7, reply_markup=gk.question7)
    elif massage == 'B) Защищаю себя и свою территорию.':
        points += 2
        await massage.answer(questions7, reply_markup=gk.question7)
    elif massage == 'C) Быстро реагирую и принимаю решения.':
        points += 3
        await massage.answer(questions7, reply_markup=gk.question7)
    elif massage == 'D) Предпочитаю избегать конфликтов.':
        points += 4
        await massage.answer(questions7, reply_markup=gk.question7)
    # Обработка ответов на 7 вопрос
    elif massage == 'A) Утро, когда всё просыпается.':
        points += 1
        await massage.answer(end_game, reply_markup=kk.game_final)
    elif massage == 'B) Вечер, когда можно расслабиться.':
        points += 2
        await massage.answer(end_game, reply_markup=kk.game_final)
    elif massage == 'C) День, когда можно быть активным.':
        points += 3
        await massage.answer(end_game, reply_markup=kk.game_final)
    elif massage == 'D) Ночь, когда тихо и спокойно.':
        points += 4
        await massage.answer(end_game, reply_markup=kk.game_final)
    # Конец игры
    elif massage == 'Узнать результат':
        if points <= 22:
            animal_low = random.choice(animals_low)
            await massage.answer(f'Иии так твое тотемное животное это {animal_low["name"]}'
                                 f'\n {animal_low["about_animal"]}')
            await massage.answer(replay_game, reply_markup=kk.replay)
        elif points >= 35:
            animal_medium = random.choice(animals_medium)
            await massage.answer(f'Иии так твое тотемное животное это {animal_medium["name"]}'
                                 f'\n {animal_medium["about_animal"]}')
            await massage.answer(replay_game, reply_markup=kk.replay)
        elif points <= 44:
            animal_max = random.choice(animals_max)
            await massage.answer(f'Иии так твое тотемное животное это {animal_max["name"]}'
                                 f'\n {animal_max["about_animal"]}')
            await massage.answer(replay_game, reply_markup=kk.replay)
