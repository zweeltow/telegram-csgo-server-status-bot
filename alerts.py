import telebot
import config


def send_alert(currentBuild):
    bot = telebot.TeleBot(config.BOT_TOKEN)
    csgobetachat = -1001280394480 # just for beta works only in t.me/csgobetachat
    text = 'Обнаружено новое обновление Counter-Strike: Global Offensive. Пост со списком изменений выйдет в ближайшее время.\n\nID новой сборки: `{}`.'
    chat_list = [csgobetachat, config.AQ]
    for chatID in chat_list:
        bot.send_message(chatID, text.format(currentBuild), parse_mode='Markdown')