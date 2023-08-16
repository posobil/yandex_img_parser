import asyncio
from aiogram import F, Router, Bot
from config_data.config import Config, load_config
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, FSInputFile
from service import del_screens, get_finish_list_ya, get_screen_link, get_links_list_google

router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Пришли фото')



@router.message(F.photo)
async def get_photo(message: Message, bot: Bot):
    await message.answer(text='Получаю список ссылок ⏳')
    await bot.download(
        message.photo[-1],
        destination=f"/Users/dmitrii/Files/python/bots/yandex_img_parser/photo/photo{message.chat.id}.jpg")
    await message.answer(text=f'yandex\n{get_finish_list_ya(message.chat.id)}')
    await message.answer_photo(photo=get_screen_link(message.chat.id))
    ph = FSInputFile(f"/Users/dmitrii/Files/python/bots/yandex_img_parser/photo/page_screen{message.chat.id}.png")
    await message.answer_document(ph)
    """print(get_links_list_google())
    await message.answer_photo(photo=get_screen_link())"""
    del_screens(message.chat.id)



"""Для отправки файлов"""
#from aiogram.types import Message, FSInputFile
#ph = FSInputFile("/Users/dmitrii/Files/python/bots/yandex_img_parser/photo/page_screen.png")
#await bot.send_photo(chat_id=message.chat.id, photo=ph)