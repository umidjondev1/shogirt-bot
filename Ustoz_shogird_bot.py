import re
import logging
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from Config import Token
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from in_but import  region_menu , main_menu
from aiogram.fsm.state import StatesGroup, State


      
logging.basicConfig(level=logging.INFO)

# Bot tokeningizni shu yerga kiriting

CHANNEL_ID = -1002433430416 # Kanal ID
bot = Bot(token=Token)
dp = Dispatcher()

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





@dp.message(CommandStart())
async def start_bot(message: Message):
    await message.answer(
        f"Assalom alaykum, {message.from_user.full_name}! 👋\n"
        "Ushbu bot orqali ustoz yoki shogird topishingiz mumkin. Menyudan tanlang:",
        reply_markup=main_menu
    )


### **Ustoz kerak uchun**
@dp.message(F.text == "Ustoz kerak")
async def ustoz_needed(message: Message, state: FSMContext):
    await message.answer(
        "Ustoz topish uchun ariza berish jarayoniga xush kelibsiz! 🧑‍🏫\n"
        "Ism va familiyangizni kiriting:"
    )
    await state.set_state(Form.name)


### **Shogird kerak uchun**
@dp.message(F.text == "Shogird kerak")
async def shogird_needed(message: Message, state: FSMContext):
    await message.answer(
        "Shogird topish uchun ariza berish jarayoniga xush kelibsiz! 👩‍💻\n"
        "Ism va familiyangizni kiriting:"
    )
    await state.set_state(Form.name)


### **O‘quv kurslari uchun**
@dp.message(F.text == "O'quv kurslari")
async def oqituvchi_courses(message: Message):
    await message.answer(
        "📚 Bizda hozir O‘quv kurslari yoq:\n"
       
    )


### **Ish joyi kerak uchun**
@dp.message(F.text == "Ish joyi kerak")
async def job_needed(message: Message):
    await message.answer(
        "🧑‍💼 Ish topish uchun quyidagi platformalardan foydalanishingiz mumkin:\n"
        "3. Telegram kanallarimiz: @https://t.me/Umidjonqwert"
    )


### **Yordam uchun**
@dp.message(F.text == "Yordam")
async def help_menu(message: Message):
    await message.answer(
        "❓ Botdan foydalanish bo‘yicha savollaringiz bo‘lsa, admin bilan bog‘laning:\n"
        "👉 @umidjon_01_09\n\n"
        "Boshqa savollaringiz bo‘lsa, bu yerni bosing: /start"
    )


### **Ma'lumot yig'ish va tasdiqlash**
@dp.message(F.text, Form.name)
async def set_name(message: Message, state: FSMContext):
    name = message.text.strip()
    await state.update_data(name=name)
    await message.answer("🕑 Yoshingizni kiriting. Masalan: 19")
    await state.set_state(Form.yosh)


@dp.message(F.text, Form.yosh)
async def set_age(message: Message, state: FSMContext):
    age = message.text.strip()
    if age.isdigit():
        await state.update_data(age=age)
        await message.answer("📚 Texnologiyalarni kiriting. Masalan: Python, Java")
        await state.set_state(Form.code)
    else:
        await message.answer("Yoshingizni faqat raqam bilan kiriting!")


@dp.message(F.text, Form.code)
async def set_code(message: Message, state: FSMContext):
    code = message.text.strip()
    await state.update_data(code=code)
    await message.answer("📞 Telefon raqamingizni kiriting. Masalan: +998 90 123 45 67")
    await state.set_state(Form.phone)


@dp.message(F.text, Form.phone)
async def set_phone(message: Message, state: FSMContext):
    phone = message.text.strip()
    pattern = r"^\+998 [0-9]{2} [0-9]{3} [0-9]{2} [0-9]{2}$"
    if re.match(pattern, phone):
        await state.update_data(phone=phone)
        await message.answer("🌍 Hududingizni tanlang:", reply_markup=region_menu)
    else:
        await message.answer("Telefon raqam noto‘g‘ri formatda! Qaytadan kiriting.")


@dp.callback_query(F.data.startswith("region:"))
async def set_region(callback: CallbackQuery, state: FSMContext):
    region = callback.data.split(":")[1]
    await state.update_data(region=region)
    await callback.message.answer("💰 Tolov qilasizmi yoki tekinmi? Summani yozing.")
    await state.set_state(Form.money)


@dp.message(F.text, Form.money)
async def set_money(message: Message, state: FSMContext):
    money = message.text.strip()
    await state.update_data(money=money)
    await message.answer("💼 Kasbingizni yozing:")
    await state.set_state(Form.kasb)


@dp.message(F.text, Form.kasb)
async def set_job(message: Message, state: FSMContext):
    job = message.text.strip()
    await state.update_data(job=job)
    await message.answer("🕰 Murojaat vaqtingizni yozing. Masalan: 9:00 - 18:00")
    await state.set_state(Form.time)

@dp.message(F.text, Form.time)
async def set_time(message: Message, state: FSMContext):
    time = message.text.strip()
    await state.update_data(time=time)
    await message.answer("🔎 Maqsadingizni yozing:")
    await state.set_state(Form.maqsad)


@dp.message(F.text, Form.maqsad)
async def confirm_submission(message: Message, state: FSMContext):
    data = await state.get_data()
    
    # 'maqsad' kaliti mavjudligini tekshirish
    maqsad = data.get('maqsad', 'Maqsad kiritilmagan')

    summary = (
        f"🎓 Ism: {data['name']}\n"
        f"🕑 Yosh: {data['age']}\n"
        f"📚 Texnologiyalar: {data['code']}\n"
        f"📞 Telefon: {data['phone']}\n"
        f"🌍 Hudud: {data['region']}\n"
        f"💰 Tolov: {data['money']}\n"
        f"💼 Kasb: {data['job']}\n"
        f"🕰 Murojaat vaqti: {data['time']}\n"
        f"🔎 Maqsad: {maqsad}"  # 'maqsad'ni default qiymat bilan chiqarish
    )
    try:
        await bot.send_message(CHANNEL_ID, summary, parse_mode=ParseMode.HTML)
        await message.answer("Ma'lumotlar yuborildi! ✅")
    except Exception as e:
        logging.error(f"Xatolik yuz berdi: {e}")
        await message.answer("Ma'lumot yuborishda xatolik yuz berdi.")
    finally:
        await state.clear()


async def main():
    await bot.send_message(chat_id=6321339720, text="Bot ishga tushdi")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
