import telebot
from utils import *
from weather import *

bot = telebot.TeleBot('874668678:AAFiMpL4Vj6uIfN71Py8PRpXTFff-K9_qRc')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    text = message.text.lower()
    chat_id = message.chat.id

    if text in MENU:
        bot.send_chat_action(chat_id, 'typing')
        send_menu(bot, chat_id)

    for tea in TEA:
        if tea in text:
            till_tea(bot, message)
            break

    if text[0] == 'ч' and text[-1] == 'й' and text != 'чай':
        only_a = True
        for i in range(1, len(text)-1):
            if text[i] != 'а':
                only_a = False
        if only_a:
            till_tea(bot, message)

    for support in SUPPORT:
        if support in text:
            bot.send_chat_action(chat_id, 'typing')
            need_support(bot, message)
            break

    """if 'денис' in text:
        if random.choice((True, False)):
            bot.send_message(chat_id, 'Денис, кстати, пидор')"""

    if 'обидно вообще-то' in text:
        bot.send_chat_action(chat_id, 'typing')
        bot.send_message(chat_id, 'Блин, прости')
        if random.choice((True, False)):
            bot.send_sticker(chat_id, 'CAADAgADLAEAAlcuIwvSO0Q78q3rzAI')

    if text == 'йоу':
        #naruto(bot, message)
        pass

    if text == 'юля':
        if random.choice((True, False)):
            bot.send_message(chat_id, 'Вы имели в виду Бля?')

    if text == 'что?' or text == 'че?' or text == 'что' or text == 'што':
        bot.send_chat_action(chat_id, 'typing')
        bot.send_message(chat_id, 'Там написано, что ты сучара.')

    if text == 'нет':
        bot.send_chat_action(chat_id, 'typing')
        no = ('Пидора ответ, хахаха', 'Дениса ответ')
        bot.send_message(chat_id, random.choice(no))

    if 'погод' in text:
        bot.send_chat_action(chat_id, 'typing')
        if 'сейчас' in text or 'ща' in text:
            weather_now(bot, chat_id)
        if 'сегодня' in text or 'седня' in text:
            weather_day(bot, chat_id, 0)
        if 'послезавтра' in text:
            weather_day(bot, chat_id, 2)
        elif 'завтра' in text:
            weather_day(bot, chat_id, 1)

    if text == 'куда жрать':
        bot.send_chat_action(chat_id, 'typing')
        where_to_eat(bot, message)

    if 'болот' in text:
        bot.send_chat_action(chat_id, 'typing')
        bot.send_audio(chat_id, audio=open('swamp.mp3', 'rb'), caption=None, duration=None,
                       performer="Ker", title="Sh", timeout=2000, reply_to_message_id=message.message_id)

    if 'бунд' in text or 'бунт' in text:
        bot.send_chat_action(chat_id, 'typing')
        bot.send_message(chat_id, 'Селама Ашал\'анорэ!')

    if 'прогноз' in text:
        bot.send_chat_action(chat_id, 'typing')
        weather_week(bot, chat_id)

    if text[0:6] == 'рандом':
        bot.send_message(chat_id, random.choice(message.text[7:].split(',')))

    if text[0:3] == 'рнд':
        bot.send_message(chat_id, random.choice(message.text[4:].split(',')))

    if 'когда-то давно' in text:
        bot.send_message(chat_id, 'Когда-то давно еще 4 народа жили в мире')

    if random.randint(0, 20) == 15:
        bot.send_message(chat_id, 'Денис, кстати, пидор')

    if 'как дела' in text or 'а у тебя' in text or 'а ты как' in text:
        bot.send_message(chat_id, random.choice(('Хорошо, ', 'Нормально, ', 'Неплохо, ',
                                                 'Ниче, ', 'Пойдет, ', 'Ну так, ')) +
                                  random.choice(('а у тебя как?', 'а ты как?')))


bot.polling(none_stop=True, interval=0)


