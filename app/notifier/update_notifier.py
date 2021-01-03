# based on: https://github.com/ericwoolard/CS-GO-Update-Notifier

from steam.client import SteamClient
import json
from datetime import datetime
import time
import traceback
import logging


import file_manager
import alerts


def setup():
    client = SteamClient()
    try:
        client.login(username='', password='')
    except:
        error_message = traceback.format_exc()
        now = str(datetime.now())
        print(now + ' - Error:\n' + error_message + '\n\n\n')
        time.sleep(60)
        setup()
        
    checkForUpdates(client)


def checkForUpdates(client):
    while True:
        try:
            delta = client.get_product_info(apps=[730], timeout=15)
            currentBuild = 0

            for key, values in delta.items():
                for k, val in values.items():
                    currentBuild = val['depots']['branches']['public']['buildid']

            cacheFile = file_manager.readJson('cache.json')
            bIDCache = cacheFile['build_ID']

            if currentBuild != bIDCache:
                print('New update found! Sending alerts...')
                file_manager.updateJson('cache.json', currentBuild)
                alerts.sendAlert(currentBuild)

            time.sleep(10)

        except AttributeError:
            error_message = traceback.format_exc()
            now = str(datetime.now())
            print(now + ' - Error:\n' + error_message + '\n\n\n')
            client.logout()
            time.sleep(60)
            setup()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(process)d %(message)s')
    setup()
