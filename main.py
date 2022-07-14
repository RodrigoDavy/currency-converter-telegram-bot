from aiogram import Bot, Dispatcher, executor, types
from credentials import *
from currency_converter import CurrencyConverter
import json

bot = Bot(token=credentials['botToken'])
currency_converter = CurrencyConverter()
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Hi! I'm a bot and I do currency convertion! Press /help to know more")

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply("To do a currency conversion, just follow the example below:\n\n/convert 1 USD EUR\n\nP.S.: This converts 1 US dollar to the equivalent amount in Euros")

@dp.message_handler(commands=['convert'])
async def convert(message: types.Message):
    args = message.get_args().split(' ')
    data = currency_converter.convert(amount = float(args[0]), input_currency = args[1], output_currency = args[2])
    data = json.loads(data.text)
    
    if data['success']:
        reply_text = f"{data['result']}"
    else:
        print(data)
        reply_text = data['error']['info']
    await message.reply(reply_text)
    
executor.start_polling(dp)
