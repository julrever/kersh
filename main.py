import telebot
from funcs import *

bot = telebot.TeleBot('874668678:AAFiMpL4Vj6uIfN71Py8PRpXTFff-K9_qRc')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.lower() in MENU:
        send_menu(bot, message)
    for tea in TEA:
        if tea in message.text.lower():
            till_tea(bot, message)
            break
    if message.text.lower() in SUPPORT:
        need_support(bot, message)
    if 'денис' in message.text.lower():
        bot.send_message(message.chat.id, 'Денис, кстати, пидор')
    if message.text.lower() == 'йоу':
        #naruto(bot, message)
        pass
    if message.text.lower() == 'юля':
        bot.send_message(message.chat.id, 'Вы имели в виду Бля?')


bot.polling(none_stop=True, interval=0)


