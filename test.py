from lxml import html
import requests
from requests_html import HTMLSession

def get_links():
    r = requests.get('https://guz.ru/postuplenie/priemnaya-kampaniya-2019-2020/rez-vstup-ispyt/', verify=False)
    html_content = html.fromstring(r.content)
    return html_content.xpath('//td[@class="workarea"]/div/a/@href')


session = HTMLSession()
r = session.get('http://art-afrika.ru/lunch/')
pic = r.html.find('#dle-content', first=True).find('a')[1].attrs['href']
print(pic)