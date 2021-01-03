import telegram

def sendAlert(id):
    myBot = telegram.Bot('')
    chatID = ''
    myBot.send_message(chat_id=chatID,
                       text='Обнаружено новое обновление Counter-Strike: Global Offensive. Пост со списком изменений выйдет в ближайшее время.\n\nID новой сборки: `{}`.'.format(id),
                       parse_mode='Markdown')
