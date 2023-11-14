from aiogram import types


def make_main_menu_kb():
    kb = [
        [types.KeyboardButton(text="Предложить перевод")],
        [types.KeyboardButton(text="Инструкция")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


def make_accept_decline_kb():
    kb = [
        [types.KeyboardButton(text="Введенные данные корректны")],
        [types.KeyboardButton(text="Ввести данные заново")],
        [types.KeyboardButton(text="Отменить перевод")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


def make_choose_language_kb():
    kb = [
        [types.KeyboardButton(text="Ввести русское слово")],
        [types.KeyboardButton(text="Ввести тувинское слово")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard
