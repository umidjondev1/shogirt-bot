from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# Reply Keyboard
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ustoz kerak"), KeyboardButton(text="Shogird kerak")],
        [KeyboardButton(text="O'quv kurslari"), KeyboardButton(text="Ish joyi kerak")],
        [KeyboardButton(text="Yordam")],
    ],
    resize_keyboard=True
)

# Inline Keyboard (Hududlar uchun)
regions = [
    "Toshkent", "Samarqand", "Buxoro", "Xorazm", 
    "Andijon", "Farg'ona", "Namangan", "Navoiy",
    "Qashqadaryo", "Surxondaryo", "Jizzax", "Sirdaryo", "Qoraqalpog'iston"
]

region_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=region, callback_data=f"region:{region}")] for region in regions
    ]
)
