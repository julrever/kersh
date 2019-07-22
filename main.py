import telebot
import time
from multiprocessing import Process
from utils.cinema import now_in_cinemas
from utils.weather import *
from utils.support import need_support
from utils.time import *
from utils.food import *
from advice import *

bot = telebot.TeleBot('874668678:AAFiMpL4Vj6uIfN71Py8PRpXTFff-K9_qRc')


@bot.message_handler(content_types=['left_chat_participant'])
def left_chat(message):
    bot.send_sticker(message.chat.id, 'CAADAgADcgQAAqtWmgwrxk5UbREMewI')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    text = message.text.lower()
    chat_id = message.chat.id

    if text in MENU:
        bot.send_chat_action(chat_id, 'typing')
        send_menu(bot, chat_id)

    for tea in TEA:
        if tea in text:
            till_what(bot, chat_id)
            break

    if text[0] == 'ч' and text[-1] == 'й' and text != 'чай':
        only_a = True
        for i in range(1, len(text)-1):
            if text[i] != 'а':
                only_a = False
        if only_a:
            till_what(bot, chat_id)

    for support in SUPPORT:
        if support in text:
            bot.send_chat_action(chat_id, 'typing')
            need_support(bot, chat_id)
            break

    if 'обидно вообще-то' in text:
        bot.send_chat_action(chat_id, 'typing')
        bot.send_message(chat_id, 'Блин, прости')
        if random.choice((True, False)):
            bot.send_sticker(chat_id, 'CAADAgADLAEAAlcuIwvSO0Q78q3rzAI')

    if text == 'юля':
        if random.choice((True, False)):
            bot.send_message(chat_id, 'Возможно, вы имели в виду Бля')

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

    if text == 'куда жрать' or text == 'куда кушать' or text == 'где кушать':
        bot.send_chat_action(chat_id, 'typing')
        where_to_eat(bot, chat_id)

    if 'болот' in text:
        bot.send_chat_action(chat_id, 'typing')
        bot.send_audio(chat_id, audio=open('swamp.mp3', 'rb'), caption=None, duration=None,
                       performer="Ker", title="Sh", timeout=2000, reply_to_message_id=message.message_id)

    if 'бунд' in text or 'бунт' in text:
        bot.send_chat_action(chat_id, 'typing')
        bot.send_message(chat_id, 'Энергия. Сила. Мои люди без них не могут... Эта зависимость возникла '
                                  'после уничтожения Солнечного Колодца. Добро пожаловать... в будущее. '
                                  'Мне очень жаль, но вы не сможете ничего изменить. Теперь меня никто '
                                  'не остановит! Селама Ашал\'анорэ!')

    if 'прогноз' in text:
        bot.send_chat_action(chat_id, 'typing')
        weather_week(bot, chat_id)

    if text[0:6] == 'рандом':
        bot.send_message(chat_id, random.choice(message.text[7:].split(',')))

    if text[0:3] == 'рнд':
        bot.send_message(chat_id, random.choice(message.text[4:].split(',')))

    if 'когда-то давно' in text:
        bot.send_message(chat_id, 'Когда-то давно еще 4 народа жили в мире')

    if 'как дела' in text or 'а у тебя' in text or 'а ты как' in text:
        bot.send_message(chat_id, random.choice(('Хорошо', 'Нормально', 'Неплохо',
                                                 'Ниче', 'Пойдет', 'Ну так')) + ', ' +
                                  random.choice(('а у тебя как?', 'а ты как?', 'а у тебя?')))

    if 'красиво' in text:
        bot.send_message(chat_id, 'Ты вошла в мою грешную жиизнь')

    if text == 'спасибо' or ('спасибо' in text and 'керш' in text):
        bot.send_message(chat_id, 'Обращайся <3')

    if 'я не тебе' in text:
        bot.send_message(chat_id, 'А кому?')

    if 'обед' in text:
        till_what(bot, chat_id, till='обеда', its_time='идти кушат', aim_time=LUNCH_TIME)

    for full in FULL:
        if full in text:
            time = datetime.datetime.now(datetime.timezone.utc).strftime(TIME_FORMAT)
            now_time = datetime.datetime.strptime(str(time), TIME_FORMAT)
            if LUNCH_TIME < now_time:

                bot.send_message(chat_id, 'Заебумба!')
            else:
                bot.send_message(chat_id, random.choice(('Щас бы обожраться до обеда',
                                                         'Крыса!')))
                bot.send_sticker(chat_id, random.choice(('CAADAgADRAADA12hFzJgg4GdHZZtAg',
                                                         'CAADAgADKAADA12hF6cAAfxwHfAUzQI')))

    if random.randint(0, 150) == 10:
        bot.send_message(chat_id, random.choice(('Дима', 'Денис')) + ', кстати, пидор')

    for cinema in CINEMA:
        if cinema in text:
            now_in_cinemas(bot, chat_id)
            break

    if text == 'сос мыслом' or text == '#deep' or text == 'совет':
        bot.send_message(chat_id, random.choice(ADVICES))

    if text == 'ало':
        support_img = open('alo.jpg', 'rb')
        bot.send_photo(chat_id, support_img)
        support_img.close()


def days_til_freedom(message):
    while True:
        if datetime.datetime.now().strftime('%H:%M:%S')[:2] == '11':
            bot.send_message(message.chat.id, 'hi')
        'test'
        time.sleep(100)


p1 = Process(target=days_til_freedom, args=())
p1.start()
bot.polling(none_stop=True, interval=0)

