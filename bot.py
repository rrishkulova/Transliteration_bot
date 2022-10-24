import os
import logging

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN) 
dp = Dispatcher(bot) 


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message): 
    user_name = message.from_user.full_name 
    user_id = message.from_user.id
    text = f'Привет! Давай транслитерируем твои ФИО. Напиши ФИО на кириллице, а я верну тебе значения на латинице'
    logging.info(f"{user_name=} {user_id=} sent_message: {message.text}")
    await message.reply(text)

@dp.message_handler()
async def send_echo(message: types.Message): 
    user_name = message.from_user.full_name 
    user_id = message.from_user.id
    original_text = message.text
    dictionary = {'А':'A', 'Б':'B', 'В':'V', 'Г':'G', 'Д':'D', 'Е':'E', 'Ё':'E', 'Ж':'Zh', 'З':'Z', 'И':'I', 'Й':'I', 
                  'К':'K', 'Л':'L', 'М':'M', 'Н':'N', 'О':'O', 'П':'P', 'Р':'R', 'С':'S', 'Т':'T', 'У':'U', 'Ф':'F', 
                  'Х':'Kh', 'Ц':'Ts', 'Ч':'Ch', 'Ш':'Sh', 'Щ':'Shch', 'Ы':'Y', 'Ъ':'Ie', 'Э':'E', 'Ю':'Iu', 'Я':'Ia',
                  'а':'a', 'б':'b', 'в':'v', 'г':'g', 'д':'d', 'е':'e', 'ё':'e', 'ж':'zh', 'з':'z', 'и':'i', 'й':'i', 
                  'к':'k', 'л':'l', 'м':'m', 'н':'n', 'о':'o', 'п':'p', 'р':'r', 'с':'s', 'т':'t', 'у':'u', 'ф':'f', 
                  'х':'kh', 'ц':'ts', 'ч':'ch', 'ш':'sh', 'щ':'shch', 'ы':'y', 'ъ':'ie', 'ь':'', 'э':'e', 'ю':'iu', 'я':'ia'}
    
    translation = original_text
    for key in dictionary.keys():
        translation = translation.replace(key, str(dictionary[key]))
    
     
    logging.info(f"{user_name=} {user_id=} sent_message: {original_text} {translation}")
    await bot.send_message(user_id, translation)



if __name__ == '__main__':
    executor.start_polling(dp)