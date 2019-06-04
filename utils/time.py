import datetime
from config import TIME_FORMAT, TEA_TIME


def till_what(bot, chat_id, till='вечернего чая', its_time='пить чай', aim_time=TEA_TIME):
    weekday = datetime.datetime.today().weekday()
    skoka = 'чучуть'
    if weekday == 5 or weekday == 6:
        bot.send_message(chat_id, 'До ' + till + ' еще совсем нечучуть')
    else:
        time = datetime.datetime.now(datetime.timezone.utc).strftime(TIME_FORMAT)
        now_time = datetime.datetime.strptime(str(time), TIME_FORMAT)
        if aim_time > now_time:
            remains = int((aim_time - now_time).seconds / 60)
        else:
            remains = int((now_time - aim_time).seconds / 60 * -1)
            if remains < -60:
                remains = 24 * 60 + remains
                if weekday == 4:
                    bot.send_message(chat_id, 'До ' + till + ' еще совсем нечучуть')
                    return
        if remains > 120:
            skoka = 'нечучуть'
        if remains > 0:
            bot.send_message(chat_id, 'До ' + till + ' осталось ' + skoka +
                             ' (' + str(remains) + ' мин.)')
        elif remains == 0:
            bot.send_message(chat_id, 'Вот щас самое время ' + its_time)
        else:
            remains = str(-1 * remains)
            bot.send_message(chat_id, 'Уже ' + str(remains) + ' мин. как пора ' + its_time)