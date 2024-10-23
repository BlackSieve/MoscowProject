from aiogram import F, Router
from aiogram.filters import CommandStart, Command

from aiogram.types import Message
import keyboard.keyboards as kb
from text.url_photo import photo_random
from text.offers import history_zoo, help_opekyn, start_hello, game_animal, give_photo, help_menu, information, feedback

from app.database import edit_profile, create_profile

router = Router()


@router.message(CommandStart())
async def start(massage: Message):
    await massage.answer(start_hello, reply_markup=kb.board)
    await create_profile(user_id=massage.from_user.id)
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
    await edit_profile(user_id=massage.from_user.id)


@router.message(F.text == 'Главное меню')
async def back_menu(massage: Message):
    await massage.answer('Хорошо мой друг', reply_markup=kb.board)
