from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import keyboard.keyboards as kb
from text.url_photo import photo_random
from text.offers import history_zoo, help_opekyn, start_hello, game_animal, give_photo, help_menu, information, feedback

# from game.questions_game import questions1, questions2, questions3, questions4, questions5, questions6, questions7

router = Router()


@router.message(CommandStart())
async def start(massage: Message):
    await massage.answer(start_hello, reply_markup=kb.board)
    await massage.delete()


@router.message(F.text == 'Навигация по мне')
async def help(massage: Message):
    await massage.answer(help_menu, reply_markup=kb.back)


@router.message(F.text == 'Опекун животных')
async def me(massage: Message):
    await massage.answer(help_opekyn, reply_markup=kb.guardian)


@router.message(F.text == 'История')
async def history(massage: Message):
    await massage.answer(history_zoo, reply_markup=kb.info_url)


@router.message(F.text == 'Тех.поддержка Зоопарка')
async def inform(massage: Message):
    await massage.answer(information, reply_markup=kb.back)


@router.message(F.text == 'Игра "Тотем"')
async def game(massage: Message):
    await massage.answer(game_animal, reply_markup=kb.play)


@router.message(F.text == 'Картинка животного')
async def picture(massage: Message):
    await massage.answer(give_photo, reply_markup=kb.photo)


# Выдает фото
@router.message(F.text == 'Хочу животного')
async def give_image(massage: Message):
    await massage.answer('Ииии так тебе выпал это животное.'
                         '\n Как думаешь кто это?🤔 Напиши в мне и я сохраню твое мнение😏')
    await massage.answer_photo(
        photo=photo_random)


@router.message(F.text == 'Оставить отзыв')
async def feedback(massage: Message):
    await massage.answer(feedback, reply_markup=kb.feedback)


@router.message(F.text == 'Ещё раз!')
async def replay_game(massage: Message):
    await massage.answer('')
    # доделать повтор игры


@router.message(F.text == 'Главное меню')
async def back_menu(massage: Message):
    await massage.answer('Хорошо мой друг', reply_markup=kb.board)

# @router.message(F.text == 'Старт!')
# async def question1(massage: Message):
#     global points
#     await massage.answer(questions1, reply_markup=kb.answer_quize)
#     if massage.text == 'A':
#         points += 1
#         await massage.answer(questions2, reply_markup=kb.answer_quize)
#     elif massage.text == 'B':
#         points += 2
#         await massage.answer(questions2, reply_markup=kb.answer_quize)
#     elif massage.text == 'C':
#         points += 3
#         await massage.answer(questions2, reply_markup=kb.answer_quize)
#     elif massage.text == 'D':
#         points += 4
#         await massage.answer(questions2, reply_markup=kb.answer_quize)
