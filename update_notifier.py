# based on: https://github.com/ericwoolard/CS-GO-Update-Notifier

from steam.client import SteamClient
import json
from datetime import datetime
import time
import traceback
import logging
import telebot

import config
import strings
from apps import file_manager


JSON_FILE_PATH = "/root/tgbot/telegram-csgo-server-status-bot/cache.json"


def setup():
    client = SteamClient()
    try:
        client.login(username=config.STEAM_USERNAME, password=config.STEAM_PASS)
    except:
        error_message = traceback.format_exc()
        now = str(datetime.now())
        print(f'{now} - Error:\n{error_message}\n\n\n')
        time.sleep(60)
        setup()
        
    check_for_updates(client)


def check_for_updates(client):
    while True:
        try:
            delta = client.get_product_info(apps=[730], timeout=15)
            currentBuild = 0

            for key, values in delta.items():
                for k, val in values.items():
                    currentBuild = val['depots']['branches']['public']['buildid']

            cacheFile = file_manager.readJson(JSON_FILE_PATH)
            bIDCache = cacheFile['build_ID']

            if currentBuild != bIDCache:
                print('New update found! Sending alerts...')
                file_manager.updateJsonID(JSON_FILE_PATH, currentBuild)
                send_alert(currentBuild)

            time.sleep(10)

        except AttributeError:
            error_message = traceback.format_exc()
            now = str(datetime.now())
            print(f'{now} - Error:\n{error_message}\n\n\n')
            client.logout()
            time.sleep(60)
            setup()


def send_alert(currentBuild):
    bot = telebot.TeleBot(config.BOT_TOKEN)
    text = strings.notiNewBuild_ru.format(currentBuild)
    if not config.TEST_MODE:
        chat_list = [config.CSGOBETACHAT, config.AQ]
    else:
        chat_list = [config.OWNER]
    for chatID in chat_list:
        bot.send_message(chatID, text, parse_mode='Markdown')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(process)d %(message)s')
    setup()
