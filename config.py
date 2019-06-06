import datetime

TIME_FORMAT = '%H:%M:%S'
TEA_TIME = datetime.datetime.strptime('14:00:00', TIME_FORMAT)
LUNCH_TIME = datetime.datetime.strptime('11:00:00', TIME_FORMAT)
MENU = ('menu', 'меню', 'а можно меню африки', 'че там сегодня в африке',
        'африка', '/menu@africa_menu_bot', '/menu')
TEA = ('чай', 'tea', '🍵', 'чая')
SUPPORT = ('поддержка', 'помогит', 'заибавс', 'я устал', 'хелп', 'заебавс', 'памагит')
CINEMA = ('афиша', 'афишу', 'че в кино', 'что в кино')
PLACES_TO_EAT = ('Африка', 'Kochi', 'Лиговъ', 'Дедушка Хо', 'Тайяки',
                 'Машита', 'Тррррррдельник', 'Кореана', 'Манты')
FULL = ('я объивс', 'я объевс', 'обожравс', 'обкуша')
