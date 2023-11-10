from aiogram.fsm.state import State, StatesGroup


class PhraseBotState(StatesGroup):
    main_state = State()
    first_word = State()
    second_word = State()
    input_name = State()
    accept_state = State()
