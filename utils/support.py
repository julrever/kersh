import random


def need_support(bot, chat_id):
    options = [send_supportive_sticker, send_puppies, send_support]
    random.choice(options)(bot, chat_id)


def send_puppies(bot, chat_id):
    img = random.choice(('support.jpg', 'support2.jpg', 'support3.jpg'))
    support_img = open(img, 'rb')
    bot.send_photo(chat_id, support_img)
    support_img.close()


def send_support(bot, chat_id):
    support = ['ну-ну', 'всё хорошо будет']
    bot.send_message(chat_id, random.choice(support))


def send_supportive_sticker(bot, chat_id):
    stickers = ['CAADAgADXgADVy4jC1_xeIKnUJcvAg',  # держись малышка
                'CAADAgAD5w8AAujW4hKTEOfr_aLUEQI',  # how amazing you are
                'CAADAgAD3A8AAujW4hKu4tX6RHk6rAI',  # ur cute
                'CAADAgAD1g8AAujW4hLiymAhix9KpAI']  # boop
    bot.send_sticker(chat_id, random.choice(stickers))