import telebot
from requests_html import HTMLSession
import urllib
import datetime


bot = telebot.TeleBot('874668678:AAHLzPER2fu7hs_6CkoiKt4faLV4vQDEVdk')
time_format = '%H:%M:%S'
tea_time = datetime.datetime.strptime('14:00:00', time_format)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/menu" or message.text == "/кушать" \
            or message.text == "/жрать" or message.text == "/меню":
        bot.send_message(message.chat.id, "ты пидор")
        weekday = datetime.datetime.today().weekday()
        today = str(datetime.datetime.today().date())
        if weekday == 5 or weekday == 6:
            bot.send_message(message.chat.id, 'not today')
        else:
            try:
                img = open(today + '.jpg', 'rb')
            except:
                session = HTMLSession()
                r = session.get('http://art-afrika.ru/lunch/')
                pic = r.html.find('#dle-content', first=True).find('a', first=True).attrs['href']
                f = open(today + '.jpg', 'wb')
                f.write(urllib.request.urlopen(pic).read())
                f.close()
                img = open(today + '.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
        img.close()

    if message.text == "/чай":
        weekday = datetime.datetime.today().weekday()
        skoka = 'чучуть'
        if weekday == 5 or weekday == 6:
            bot.send_message(message.chat.id, 'До вечернего чая еще совсем нечучуть')
        else:
            time = datetime.datetime.now(datetime.timezone.utc).strftime(time_format)
            now_time = datetime.datetime.strptime(str(time), time_format)
            if tea_time > now_time:
                remains = int((tea_time - now_time).seconds / 60)
            else:
                remains = int((now_time - tea_time).seconds / 60 * -1)
            if remains > 200:
                skoka = 'нечучуть'
            bot.send_message(message.chat.id, 'До вечернего чая осталось ' + skoka +
                                              ' (' + str(remains) + ' мин.)')


bot.polling(none_stop=True, interval=0)
