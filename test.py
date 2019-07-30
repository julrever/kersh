from lxml import html
import requests


def get_links():
    r = requests.get('https://guz.ru/postuplenie/priemnaya-kampaniya-2019-2020/rez-vstup-ispyt/', verify=False)
    html_content = html.fromstring(r.content)
    return html_content.xpath('//td[@class="workarea"]/div/a/@href')
