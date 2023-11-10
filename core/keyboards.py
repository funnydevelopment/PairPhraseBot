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
