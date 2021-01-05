import telebot
import config
import strings


def send_alert(currentBuild):
    bot = telebot.TeleBot(config.BOT_TOKEN)
    csgobetachat = -1001280394480 # just for beta works only in t.me/csgobetachat
    text = strings.notiNewBuild_ru.format(currentBuild)
    if not config.TEST_MODE:
        chat_list = [csgobetachat, config.AQ]
    else:
        chat_list = [config.OWNER]
    for chatID in chat_list:
        bot.send_message(chatID, text, parse_mode='Markdown')