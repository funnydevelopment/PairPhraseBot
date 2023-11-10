import logging

from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from .states import PhraseBotState
from . import message_texts as texts
from . import keyboards as kb

router = Router()

logger = logging.getLogger(__name__)


@router.message(Command("start"))
async def start_command(message: types.Message, state: FSMContext):
    user_id, user_fullname = message.from_user.id, message.from_user.full_name
    if not user_fullname:
        user_fullname += "пользователь"
    await message.answer(
        text=texts.START_MESSAGE_TEXT.format(user_name=user_fullname),
        reply_markup=kb.make_main_menu_kb(),
    )
    await state.set_state(state=PhraseBotState.main_state)


@router.message(F.text.lower() == "инструкция")
async def help_command(message: types.Message, state: FSMContext):
    await message.answer(
        text=texts.HELP_MESSAGE_TEXT, reply_markup=kb.make_main_menu_kb()
    )
    await state.set_state(state=PhraseBotState.main_state)


@router.message(F.text.lower() == "предложить перевод")
async def start_getting_words(message: types.Message, state: FSMContext):
    await message.answer(text="Вы начали процесс добавление перевода")
    await state.set_state(state=PhraseBotState.main_state)
