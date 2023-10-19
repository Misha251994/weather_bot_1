from aiogram.utils.keyboard import ReplyKeyboardBuilder

def take_choice_kb():
    kb = ReplyKeyboardBuilder()
    kb.button(text="Write city name")
    kb.button(text="Send location", request_location=True)
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=True,
                        input_field_placeholder="Choose one button")
