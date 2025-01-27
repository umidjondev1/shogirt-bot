from aiogram.fsm.state import StatesGroup, State

# Holatlar (FSM uchun)
class Form(StatesGroup):
    name = State()
    yosh = State()
    code = State()
    phone = State()
    region = State()
    money = State()
    kasb = State()
    time = State()
    maqsad = State()
      