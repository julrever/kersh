from requests_html import HTMLSession


def now_in_cinemas(bot, chat_id):
    text = ''
    session = HTMLSession()
    r = session.get('https://www.kinopoisk.ru/afisha/new/city/2/')
    table = r.html.find('.filmsListNew', first=True)
    names = table.find('.name > a')
    duration = table.find('.name > span')
    genre = table.find('.gray')
    info = table.find('.info')
    for i in range(0, 10):
        text += '🔸*' + names[i].text + '*\n_'
        text += genre[2*i].text + '_\n' + genre[2*i+1].text[8:] + '\n'
        rating = info[i].find('.rating > span', first=True)
        try:
            text += '⭐️*' + rating.text + '*⠀'
        except:
            pass
        dur = duration[i].text.split(' ')
        text += '🕐_' + dur[-2] + ' ' + dur[-1] + '_'
        text += ' 🔗[инфо](http://kinopoisk.ru' + names[i].attrs['href'] + ')\n'
        text += '🎟 [Сеансы](http://kinopoisk.ru' + names[i].attrs['href'] + 'afisha/city/2/)\n\n'


    bot.send_message(chat_id, text.replace('...', ''), parse_mode='Markdown', disable_web_page_preview=True)

