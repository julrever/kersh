from requests_html import HTMLSession
import urllib
import random
from config import *


def send_menu(bot, chat_id):
    weekday = datetime.datetime.today().weekday()
    today = str(datetime.datetime.today().date())
    if weekday == 5 or weekday == 6:
        bot.send_message(chat_id, 'not today')
    else:
        try:
            img = open(today + '.jpg', 'rb')
        except:
            session = HTMLSession()
            r = session.get('http://art-afrika.ru/lunch/')
            pic = r.html.find('#dle-content', first=True).find('a', first=True).attrs['href']
            f = open('africa/' + today + '.jpg', 'wb')
            f.write(urllib.request.urlopen(pic).read())
            f.close()
            img = open('africa/' + today + '.jpg', 'rb')
    bot.send_photo(chat_id, img)
    img.close()


def till_tea(bot, message):
    weekday = datetime.datetime.today().weekday()
    skoka = 'чучуть'
    if weekday == 5 or weekday == 6:
        bot.send_message(message.chat.id, 'До вечернего чая еще совсем нечучуть')
    else:
        time = datetime.datetime.now(datetime.timezone.utc).strftime(TIME_FORMAT)
        now_time = datetime.datetime.strptime(str(time), TIME_FORMAT)
        if TEA_TIME > now_time:
            remains = int((TEA_TIME - now_time).seconds / 60)
        else:
            remains = int((now_time - TEA_TIME).seconds / 60 * -1)
            if remains < -60:
                remains = 24*60 + remains
                if weekday == 4:
                    bot.send_message(message.chat.id, 'До вечернего чая еще совсем нечучуть')
                    pass
        if remains > 120:
            skoka = 'нечучуть'
        if remains > 0:
            bot.send_message(message.chat.id, 'До вечернего чая осталось ' + skoka +
                         ' (' + str(remains) + ' мин.)')
        else:
            remains = str(-1 * remains)
            late_text = ('Вы охуели тут все? Уже ' + remains + ' мин. как чай. Мда, пиздец.',
                         'Ало, чай был ' + remains + ' мин. назад',
                         'Чай то пить пойдем? Уже ' + remains + ' мин. как чай.',
                         'Кхм-кхм, чай. ' + remains + ' мин. уже')
            bot.send_message(message.chat.id, random.choice(late_text))


def need_support(bot, message):
    options = [send_supportive_sticker, send_puppies, send_support]
    random.choice(options)(bot, message)


def send_puppies(bot, message):
    support_img = open('support.jpg', 'rb')
    bot.send_photo(message.chat.id, support_img)
    support_img.close()


def send_support(bot, message):
    support = ['ну-ну', 'всё хорошо будет']
    bot.send_message(message.chat.id, random.choice(support))


def send_supportive_sticker(bot, message):
    stickers = ['CAADAgADXgADVy4jC1_xeIKnUJcvAg',  # держись малышка
                'CAADAgAD5w8AAujW4hKTEOfr_aLUEQI',  # how amazing you are
                'CAADAgAD3A8AAujW4hKu4tX6RHk6rAI',  # ur cute
                'CAADAgAD1g8AAujW4hLiymAhix9KpAI']  # boop
    bot.send_sticker(message.chat.id, random.choice(stickers))


def naruto(bot, message):
    bot.send_message(message.chat.id, 'Собаки, я — Наруто Узумаки')
    bot.send_message(message.chat.id, 'Да, и, кстати, я — будущий Хокаге')
    bot.send_message(message.chat.id, 'У меня всё круто, я же всё-таки Наруто')
    bot.send_message(message.chat.id, 'Ненавижу Орочимару и Кабуто')
    bot.send_message(message.chat.id, 'Знаю много джутсу, ненавижу бутсы')
    bot.send_message(message.chat.id, 'Лучше клонов, Расенгана не найдутся ')
    bot.send_message(message.chat.id, 'У меня фанаты, плюс я люблю Хинату')
    bot.send_message(message.chat.id, 'Немало друзей, и однокомнатная хата')


def get_weather_today(bot, message):
    session = HTMLSession()
    r = session.get('https://sinoptik.com.ru/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%81%D0%B0%D0%BD%D0%BA%D1%82'
                    '-%D0%BF%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3')
    temperature_today = r.html.xpath('/html/body/div[3]/div[2]/div[1]/div[1]/div/div[1]/div[2]/div[2]')
    condition_today = r.html.xpath('/html/body/div[3]/div[2]/div[1]/div[1]/div/div[1]/div[2]/div[1]', first=True)
    text = condition_today.attrs['title'] + '\n'
    for t in temperature_today:
        text += t.text
    bot.send_message(message.chat.id, set_emoji_weather(text) + text)


def get_weather_tomorrow(bot, message):
    session = HTMLSession()
    r = session.get('https://sinoptik.com.ru/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%81%D0%B0%D0%BD%D0%BA%D1%82'
                    '-%D0%BF%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3')
    temperature_tomorrow = r.html.xpath('/html/body/div[3]/div[2]/div[1]/div[1]/div/div[1]/div[4]/div[2]')
    condition_tomorrow = r.html.xpath('/html/body/div[3]/div[2]/div[1]/div[1]/div/div[1]/div[4]/div[1]', first=True)
    text = condition_tomorrow.attrs['title'] + '\n'
    for t in temperature_tomorrow:
        text += t.text
    bot.send_message(message.chat.id, set_emoji_weather(text) + text)


def set_emoji_weather(text):
    text = text.lower()
    res = ''
    if 'ясно' in text:
        res += '☀️'
    if 'облачно' in text:
        res += '⛅️'
    if 'дождь' in text:
        res += '🌧'
    if 'снег' in text:
        res += '❄️'
    return res


def where_to_eat(bot, message):
    bot.send_message(message.chat.id, random.choice(PLACES_TO_EAT))
