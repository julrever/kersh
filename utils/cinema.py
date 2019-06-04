from requests_html import HTMLSession


def now_in_cinemas(bot, chat_id):
    text = ''
    session = HTMLSession()
    r = session.get('https://www.kinopoisk.ru/afisha/new/city/2/')
    table = r.html.find('.filmsListNew', first=True)
    names = table.find('.name > a')
    duration = table.find('.name > span')
    genre = table.find('.gray')
    rating = table.find('.rating > span')
    for i in range(0, 10):
        text += '🔸*' + names[i].text + '*\n_'
        text += genre[2*i].text + '_\n' + genre[2*i+1].text[8:] + '\n'
        text += '⭐️*' + rating[i].text + '*⠀'
        dur = duration[i].text.split(' ')
        text += '🕐_' + dur[-2] + ' ' + dur[-1] + '_\n\n'

    bot.send_message(chat_id, text.replace('...', ''), parse_mode='Markdown')


