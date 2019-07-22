import datetime

TIME_FORMAT = '%H:%M:%S'
TEA_TIME = datetime.datetime.strptime('14:00:00', TIME_FORMAT)
LUNCH_TIME = datetime.datetime.strptime('11:00:00', TIME_FORMAT)
MENU = ('menu', 'меню', 'а можно меню африки', 'че там сегодня в африке',
        'африка', '/menu@africa_menu_bot', '/menu')
TEA = ('чай', 'tea', '🍵', 'чая')
SUPPORT = ('поддержка', 'помогит', 'заибавс', 'я устал', 'хелп', 'заебавс', 'памагит')
CINEMA = ('афиша', 'афишу', 'че в кино', 'что в кино')
PLACES_TO_EAT = ('Африка',
                 '[Kochi](https://eda.yandex/restaurant/kochi_korean_food)',
                 '[Макдак](https://mcdonalds.ru/products), '
                 '[KFC](https://www.kfc.ru/foodorder/category/1), '
                 '[Burger King](https://burgerking.ru/menu), '
                 '[Теремок](https://teremok.ru/menu/)',
                 '[Дедушка Хо](https://eda.yandex/restaurant/Dedushkaho_Kamenoostrovskiy)',
                 '[Тайяки](https://eda.yandex/restaurant/tayaki_spb2)',
                 '[Машита](http://mashita-ramen.ru/menu.php)',
                 'Тррррррдельник',
                 '[Кореана](https://www.koreanalight.ru/menyu-1)')
FULL = ('объивс', 'объевс', 'обожравс', 'обкуша')
