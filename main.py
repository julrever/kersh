import telebot
from funcs import *

bot = telebot.TeleBot('874668678:AAFiMpL4Vj6uIfN71Py8PRpXTFff-K9_qRc')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    text = message.text.lower()

    if text in MENU:
        send_menu(bot, message)

    for tea in TEA:
        if tea in text:
            till_tea(bot, message)
            break

    for support in SUPPORT:
        if support in text:
            need_support(bot, message)
            break

    if 'денис' in text:
        bot.send_message(message.chat.id, 'Денис, кстати, пидор')

    if text == 'йоу':
        #naruto(bot, message)
        pass

    if text == 'юля':
        bot.send_message(message.chat.id, 'Вы имели в виду Бля?')

    if text == 'что?' or text == 'че?':
        bot.send_message(message.chat.id, 'Там написано, что ты сучара.')

    if 'погод' in text:
        if 'сегодня' in text or 'седня' in text:
            get_weather_today(bot, message)
        if 'послезавтра' in text:
            pass
        elif 'завтра' in text:
            get_weather_tomorrow(bot, message)


bot.polling(none_stop=True, interval=0)


