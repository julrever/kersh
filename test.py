from requests_html import HTMLSession
import requests
import pyowm

#owm = pyowm.OWM('bcd445d93f2c5c50e8e369e537441af3')
#observation = owm.weather_at_place('Petersburg,RU')
#w = observation.get_weather()
session = HTMLSession()
r = session.get('https://sinoptik.com.ru/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%81%D0%B0%D0%BD%D0%BA%D1%82'
                '-%D0%BF%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3')
temperature_today = r.html.xpath('/html/body/div[3]/div[2]/div[1]/div[1]/div/div[1]/div[2]/div[2]')
condition_today = r.html.xpath('/html/body/div[3]/div[2]/div[1]/div[1]/div/div[1]/div[2]/div[1]', first=True)
text = condition_today.attrs['title'] + '\n'
for t in temperature_today:
    text += t.text
print(text)

temperature_tomorrow = r.html.xpath('/html/body/div[3]/div[2]/div[1]/div[1]/div/div[1]/div[4]/div[2]')
condition_tomorrow = r.html.xpath('/html/body/div[3]/div[2]/div[1]/div[1]/div/div[1]/div[4]/div[1]', first=True)
for t in temperature_tomorrow:
    print(t.text)
print(condition_tomorrow.attrs['title'])