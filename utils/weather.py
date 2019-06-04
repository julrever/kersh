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


def weather_day(bot, chat_id, day):
    r = requests.post(base_url + 'v1/forecast.json?key=' + api_key + '&q=Petersburg,Ru&days=' + str(day+1))
    res = json.loads(r.text)['forecast']['forecastday'][day]
    condition = translator.translate(res['day']['condition']['text'], src='en', dest='ru').text
    text = '\n' + set_emoji_weather(condition) + \
           '\nМакс.: ' + str(res['day']['maxtemp_c']) + '°\n' \
           'Мин.: ' + str(res['day']['mintemp_c']) + '°\n' \
           'Влажность: ' + str(res['day']['avghumidity']) + '%\n' \
           'Рассвет: ' + res['astro']['sunrise'] + ', закат: ' + res['astro']['sunset'] + '\n\n'
    bot.send_message(chat_id, text)


def set_emoji_weather(text):
    res = ''
    if 'ясно' in text.lower() or 'солнечн' in text.lower():
        res += '☀️'
    if 'облачно' in text.lower() or 'пасмурн' in text.lower():
        res += '⛅️'
    if 'дождь' in text.lower():
        res += '🌧'
    if 'снег' in text.lower():
        res += '❄️'
    if 'гроз' in text.lower():
        res += '🌩'
    if text == 'Очистить':
        text = 'Ясно'
    return res + ' ' + text


"""         OLD VERSION

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
"""