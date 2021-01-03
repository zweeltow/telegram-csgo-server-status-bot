# based on: https://github.com/ericwoolard/CS-GO-Update-Notifier

from steam.client import SteamClient
import json
from datetime import datetime
import time
import traceback
import logging


import file_manager
# import alerts

from bot import SendAlert

import config


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

            cacheFile = file_manager.readJson('/root/tgbot/telegram-csgo-server-status-bot/cache.json')
            bIDCache = cacheFile['build_ID']

            if currentBuild != bIDCache:
                print('New update found! Sending alerts...')
                file_manager.updateJson('/root/tgbot/telegram-csgo-server-status-bot/cache.json', currentBuild)
                SendAlert().send_alert(currentBuild)

            time.sleep(10)

        except AttributeError:
            error_message = traceback.format_exc()
            now = str(datetime.now())
            print(f'{now} - Error:\n{error_message}\n\n\n')
            client.logout()
            time.sleep(60)
            setup()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(process)d %(message)s')
    setup()
