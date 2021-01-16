# based on: https://github.com/ericwoolard/CS-GO-Update-Notifier

from steam.client import SteamClient
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import traceback
import logging
import telebot

import config
import strings
from apps import file_manager

url_db = 'https://steamdb.info/app/730/patchnotes/'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}

soup = BeautifulSoup(requests.get(url_db, headers=headers).content, 'html.parser')

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
            tbody = soup.find("tbody", {"id": "js-builds"})
            tr = tbody.find("tr")
            td = tr.find_all("td")
            td = td[3]
            a = td.find("a").string
            version = str(a)
            if 'version' in version:
                version = a.replace('version ', '')
            else:
                version = 'N/A'


            currentBuild = 0

            for key, values in client.get_product_info(apps=[730], timeout=15).items():
                for k, val in values.items():
                    currentBuild = val['depots']['branches']['public']['buildid']

            cacheFile = file_manager.readJson(config.CACHE_FILE_PATH)
            cache_key_list = []
            for key, value in cacheFile.items():
                cache_key_list.append(key)

            if currentBuild != cacheFile['build_ID'] and version != cacheFile['version']:
                file_manager.updateJson(config.CACHE_FILE_PATH, currentBuild, cache_key_list[0])
                file_manager.updateJson(config.CACHE_FILE_PATH, version, cache_key_list[1])
                send_alert(currentBuild, version)

            time.sleep(10)

        except AttributeError:
            error_message = traceback.format_exc()
            now = str(datetime.now())
            print(f'{now} - Error:\n{error_message}\n\n\n')
            client.logout()
            time.sleep(60)
            setup()


def send_alert(currentBuild, version):
    bot = telebot.TeleBot(config.BOT_TOKEN)
    text = strings.notiNewBuild_ru.format(version, currentBuild)
    bot.send_message(config.CSGOBETACHAT, text, parse_mode='Markdown')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(process)d %(message)s')
    setup()
