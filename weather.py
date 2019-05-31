import requests
import json
from googletrans import Translator
translator = Translator()
base_url = 'http://api.apixu.com/'
api_key = '25c7c61db925428d9b5153604193005'


def weather_now(bot, chat_id):
    r = requests.post(base_url + 'v1/current.json?key=' + api_key + '&q=Petersburg,Ru')
    res = json.loads(r.text)['current']
    condition = translator.translate(res['condition']['text'], src='en', dest='ru').text
    text = set_emoji_weather(condition) + \
           '\nСейчас ' + str(res['temp_c']) + '°\n' \
           'Ветерок: ' + str(res['wind_kph']) + ' км/ч\n' \
           'Влажность: ' + str(res['humidity']) + '%\n' \
           'Ощущается это все как ' + str(res['feelslike_c']) + '°'
    bot.send_message(chat_id, text)


def weather_week(bot, chat_id):
    r = requests.post(base_url + 'v1/forecast.json?key=' + api_key + '&q=Petersburg,Ru&days=7')
    res = json.loads(r.text)['forecast']['forecastday']
    text = ''
    for i in range(0, 7):
        day = res[i]
        text += day['date']
        condition = translator.translate(day['day']['condition']['text'], src='en', dest='ru').text
        text += '\n' + set_emoji_weather(condition) + \
                '\nМакс.: ' + str(day['day']['maxtemp_c']) + '°\n' \
                'Мин.: ' + str(day['day']['mintemp_c']) + '°\n' \
                'Влажность: ' + str(day['day']['avghumidity']) + '%\n' \
                'Рассвет: ' + day['astro']['sunrise'] + ', закат: ' + day['astro']['sunset'] + '\n\n'
    bot.send_message(chat_id, text)


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
    return res + ' ' + text
