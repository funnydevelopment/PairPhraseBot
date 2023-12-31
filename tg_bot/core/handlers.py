import logging

from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from .states import PhraseBotState
from . import message_texts as texts
from . import keyboards as kb
from . import utils

router = Router()

logger = logging.getLogger(__name__)


async def get_all_data(message: types.Message, state: FSMContext):
    data = await state.get_data()
    first_language_text, second_language_text = "", ""
    if data["first_word_language"] == "rus":
        first_language_text += texts.RUSSIAN_TEXT
        second_language_text += texts.TUVAN_TEXT
    else:
        first_language_text += texts.TUVAN_TEXT
        second_language_text += texts.RUSSIAN_TEXT
    await message.answer(
        text=texts.ALL_USER_DATA_TEXT.format(
            first_language_text=first_language_text,
            second_language_text=second_language_text,
            first_word=data["first_word"],
            second_word=data["second_word"],
            user_name=data["user_name"],
        ),
        reply_markup=kb.make_accept_decline_kb(),
    )


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


@router.message(F.text.lower() == "статистика")
async def get_user_stat(message: types.Message, state: FSMContext):
    # todo: через новый сервис и получить с бэкенда статистику
    fullname = message.from_user.full_name
    await message.answer(
        text=texts.USER_STAT_TEXT.format(user_name=fullname, count=None)
    )
    await state.set_state(PhraseBotState.main_state)


@router.message(F.text.lower() == "предложить перевод")
async def start_getting_words(message: types.Message, state: FSMContext):
    await message.answer(
        text=texts.CHOOSE_LANGUAGE_TEXT, reply_markup=kb.make_choose_language_kb()
    )


@router.message(F.text.lower() == "введенные данные корректны")
async def send_data_to_server(message: types.Message, state: FSMContext):
    # todo: отправить данные на бэкенд и проверить есть ли данная пара слов
    await message.answer(
        text=texts.ACCEPT_DATA_TEXT, reply_markup=kb.make_main_menu_kb()
    )
    await state.clear()
    await state.set_state(PhraseBotState.main_state)


@router.message(F.text.lower() == "ввести данные заново")
async def recall_start_getting_words(message: types.Message, state: FSMContext):
    await state.clear()
    await start_getting_words(message, state)


@router.message(F.text.lower() == "отменить перевод")
async def decline_user_data(message: types.Message, state: FSMContext):
    await message.answer(
        text=texts.DECLINE_DATA_TEXT, reply_markup=kb.make_main_menu_kb()
    )
    await state.clear()
    await state.set_state(PhraseBotState.main_state)


@router.message(PhraseBotState.first_word)
async def get_first_word(message: types.Message, state: FSMContext):
    is_valid_word = await utils.is_cyrillic_with_hyphen_string(message.text)
    if is_valid_word:
        await state.update_data(first_word=message.text.lower())
        await message.answer(text=texts.SECOND_WORD_TEXT)
        await state.set_state(state=PhraseBotState.second_word)
    else:
        await message.answer(text=texts.NOT_VALID_TEXT)
        await state.set_state(PhraseBotState.first_word)


@router.message(PhraseBotState.second_word)
async def get_second_word(message: types.Message, state: FSMContext):
    is_valid_word = await utils.is_cyrillic_with_hyphen_string(message.text)
    if is_valid_word:
        await state.update_data(second_word=message.text.lower())
        await message.answer(text=texts.NAME_INPUT_TEXT)
        await state.set_state(state=PhraseBotState.input_name)
    else:
        await message.answer(text=texts.NOT_VALID_TEXT)
        await state.set_state(state=PhraseBotState.second_word)


@router.message(F.text.lower() == "ввести русское слово")
async def choose_russian_language(message: types.Message, state: FSMContext):
    await message.answer(
        text=texts.RUSSIAN_LANGUAGE_TEXT, reply_markup=types.ReplyKeyboardRemove()
    )
    await state.update_data(first_word_language="rus")
    await state.set_state(state=PhraseBotState.first_word)


@router.message(F.text.lower() == "ввести тувинское слово")
async def choose_russian_language(message: types.Message, state: FSMContext):
    await message.answer(
        text=texts.TUVAN_LANGUAGE_TEXT, reply_markup=types.ReplyKeyboardRemove()
    )
    await state.update_data(first_word_language="tuv")
    await state.set_state(state=PhraseBotState.first_word)


@router.message(PhraseBotState.input_name)
async def get_user_name(message: types.Message, state: FSMContext):
    await state.update_data(user_name=message.text, user_id=message.from_user.id)
    await state.set_state(PhraseBotState.accept_state)
    await get_all_data(message, state)


@router.message()
async def handle_no_state(message: types.Message, state: FSMContext):
    await message.answer(
        text=texts.NO_HANDLE_STATE_TEXT,
        reply_markup=kb.make_main_menu_kb(),
    )
    await state.set_state(PhraseBotState.main_state)
