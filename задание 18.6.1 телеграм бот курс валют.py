import telebot
import requests
import json

TOKEN = '6251950792:AAE0fefbi5ZSmUcU4JrLAb9wLgjDO6Qmi3I'

bot = telebot.TeleBot(TOKEN)

keys = {
  '����':'EUR',
  '������':'USD',
  '�����':'RUB',
}

class ConvertionExeption(Exception):
  pass


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = '����� ������ ������ ������� �������� ���� � ��������� �������: \n<��� ������>\n<� ����� ������ ���������> \n<���������� ����������� ������> \n������� ������ ���� ��������� �����: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
  text = '��������� ������'
  for key in keys.keys():
     text = '\n'.join((text, key, ))
  bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
  values =  message.text.split(' ')
  
  if len(values) != 3:
    bot.reply_to(message,'�� ������ ���������� ����������. ����� 3' )
    raise ConvertionExeption('�� ������ ���������� ����������. ����� 3')
    
    
  quote, base, amount = values

  if quote == base:
    bot.reply_to(message,f'���������� ��������� ���������� ������ {base}' )
    raise ConvertionExeption(f'���������� ��������� ���������� ������ {base}')

  try:
    quote_ticker = keys[quote]
  except KeyError:
    bot.reply_to(message,f'�� ������� ���������� ������ {quote}' )
    raise ConvertionExeption(f'�� ������� ���������� ������ {quote}')

  try:
    base_ticker = keys[base]
  except KeyError:
    bot.reply_to(message,f'�� ������� ���������� ������ {base}')
    raise ConvertionExeption(f'�� ������� ���������� ������ {base}')
  
  try:
    amount = float(amount)
  except ValueError:
    bot.reply_to(message,f'�� ������� ���������� ���������� {amount}')
    raise ConvertionExeption(f'�� ������� ���������� ���������� {amount}')

  r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
  total_base = json.loads(r.content)[keys[base]]
  text = f'���� {amount} {quote} � {base} - {total_base*amount}' 
  '''��� ������������ total_base �� �mount ����� ��������� �����'''
  bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)

