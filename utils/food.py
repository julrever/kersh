from requests_html import HTMLSession
import urllib
import random
from config import *


def send_menu(bot, chat_id):
    weekday = datetime.datetime.today().weekday()
    today = str(datetime.datetime.today().date())
    if weekday == 5 or weekday == 6:
        bot.send_message(chat_id, 'А еще тебе чего?')
        return
    else:
        try:
            img = open(today + '.jpg', 'rb')
        except:
            session = HTMLSession()
            r = session.get('http://art-afrika.ru/lunch/')
            pic = r.html.find('#dle-content', first=True).find('a', first=True).attrs['href']
            f = open('../africa/' + today + '.jpg', 'wb')
            f.write(urllib.request.urlopen(pic).read())
            f.close()
            img = open('../africa/' + today + '.jpg', 'rb')
    bot.send_photo(chat_id, img)
    img.close()


def where_to_eat(bot, chat_id):
    bot.send_message(chat_id, random.choice(PLACES_TO_EAT))
