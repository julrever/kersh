import telebot

bot = telebot.TeleBot('694527891:AAF9t-c4MbZxdzwXXnLIPJF0vrVkfzSBTuM')
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if 'стартуем' in message.text.lower() or 'денис' in message.text.lower():
        bot.send_message(message.chat.id, '/денис')

bot.polling(none_stop=True, interval=0)
