'''Это оригинальный код с видео до разделения на разные файлы и создания класса Exeption. 
Я добавил в каждом Exeption вывод сообщения в телеграмм
для этого задаяния я поменял только словарь и адрес get реквеста'''

import telebot
import requests
import json

TOKEN = '6251950792:AAE0fefbi5ZSmUcU4JrLAb9wLgjDO6Qmi3I'

bot = telebot.TeleBot(TOKEN)

keys = {
  'евро':'EUR',
  'доллар':'USD',
  'рубль':'RUB',
}

class ConvertionExeption(Exception):
  pass


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите комманду боту в следующем формате: \n<имя валюты>\n<в какую валюту перевести> \n<количество переводимой валюты> \nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
  text = 'Доступные валюты'
  for key in keys.keys():
     text = '\n'.join((text, key, ))
  bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
  values =  message.text.split(' ')
  
  if len(values) != 3:
    bot.reply_to(message,'Не верное количество параметров. Нужно 3' )
    raise ConvertionExeption('Не верное количество параметров. Нужно 3')
    
    
  quote, base, amount = values

  if quote == base:
    bot.reply_to(message,f'Невозможно перевести одинаковые валюты {base}' )
    raise ConvertionExeption(f'Невозможно перевести одинаковые валюты {base}')

  try:
    quote_ticker = keys[quote]
  except KeyError:
    bot.reply_to(message,f'Не удалось обработать валюту {quote}' )
    raise ConvertionExeption(f'Не удалось обработать валюту {quote}')

  try:
    base_ticker = keys[base]
  except KeyError:
    bot.reply_to(message,f'Не удалось обработать валюту {base}')
    raise ConvertionExeption(f'Не удалось обработать валюту {base}')
  
  try:
    amount = float(amount)
  except ValueError:
    bot.reply_to(message,f'Не удалось обработать количество {amount}')
    raise ConvertionExeption(f'Не удалось обработать количество {amount}')

  r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
  total_base = json.loads(r.content)[keys[base]]
  text = f'Цена {amount} {quote} в {base} - {total_base*amount}' 
  '''Тут перемножение total_base на аmount чтобы считалась сумма'''
  bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)

