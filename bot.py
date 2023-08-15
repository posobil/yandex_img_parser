import asyncio
from aiogram import Bot, Dispatcher, F
from config_data.config import Config, load_config
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, FSInputFile
from service import get_links_list, get_finish_list_ya, get_screen_link, get_links_list_google



# Загружаем конфиг в переменную config
config: Config = load_config()

# Инициализируем бот и диспетчер
bot: Bot = Bot(token=config.tg_bot.token)
dp: Dispatcher = Dispatcher()



@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Пришли фото')



@dp.message(F.photo)
async def get_photo(message: Message):
    await message.answer(text='Получаю список ссылок ⏳')
    await bot.download(
        message.photo[-1],
        destination="/Users/dmitrii/Files/python/bots/yandex_img_parser/photo/photo.jpg")
    await message.answer(text=f'yandex\n{get_finish_list_ya()}')
    await message.answer_photo(photo=get_screen_link())
    ph = FSInputFile("/Users/dmitrii/Files/python/bots/yandex_img_parser/photo/page_screen.png")
    await message.answer_document(ph)
    """print(get_links_list_google())
    await message.answer_photo(photo=get_screen_link())"""


if __name__ == '__main__':
    dp.run_polling(bot)


"""Для отправки файлов"""
#from aiogram.types import Message, FSInputFile
#ph = FSInputFile("/Users/dmitrii/Files/python/bots/yandex_img_parser/photo/page_screen.png")
#await bot.send_photo(chat_id=message.chat.id, photo=ph)