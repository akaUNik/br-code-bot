import logging
from aiogram import Bot, Dispatcher, executor, types
import brcode

API_TOKEN = '5036082476:AAGcfex_VXJvzw_F32B_s0xYmHzRHmbEurA'
embeded_image = 'logo_stroke.png' # изображение, которое будет помещено в центр qr-code

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Привет!\nЯ braindo_qrcode_bot!\nPowered by Parabellum.")

@dp.message_handler(regexp='(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)')
async def send_brcode(message: types.Message):
    with brcode.BRCode() as qr:
        img = qr.make_image(message.text, embeded_image)
        #with open('br-code.png', 'rb') as photo:
        await message.reply_photo(img, caption='Вот твой br-code')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)