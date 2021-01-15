import json
from datetime import datetime
import time
import traceback
import logging
import config

from apps import file_manager
from apps.valve_api import ValveServersAPI
from apps.scrapper import PeakOnline, Monthly, CSGOGameCoordinator

api = ValveServersAPI()
peak_count = PeakOnline()
month_unique = Monthly()
gc = CSGOGameCoordinator()


def info_updater():
    while True:
        try:
            cacheFile = file_manager.readJson(config.CACHE_FILE_PATH)

            value_list = [ cacheFile['build_ID'], gc.get_status(), api.check_status(), api.get_status()[1], api.get_players(), api.get_status()[4], api.get_status()[0],
            api.get_status()[2], api.get_status()[3], api.get_status()[5], api.get_status()[6], api.get_devs(), peak_count.get_peak(), cacheFile['peak_all_time'], month_unique.get_unique() ]

            cache_value_list = [ cacheFile['build_ID'], cacheFile['game_coordinator'], cacheFile['valve_webapi'], cacheFile['sessionsLogon'], cacheFile['online_player_count'],
            cacheFile['time_server'], cacheFile['scheduler'], cacheFile['online_server_count'], cacheFile['active_player_count'], cacheFile['search_seconds_avg'],
            cacheFile['searching_players'], cacheFile['dev_player_count'], cacheFile['peak_24_hours'], cacheFile['peak_all_time'], cacheFile['unique_monthly'] ]

            cache_keys = file_manager.readJson(config.CACHE_FILE_PATH).items()
            cache_key_list = []
            for key, value in cache_keys:
                cache_key_list.append(key)

            for val, cache_val, cache_key in zip(value_list, cache_value_list, cache_key_list):
                if val != cache_val:
                    file_manager.updateJson(config.CACHE_FILE_PATH, val, cache_key)

            if api.get_players() > cacheFile['peak_all_time']:
                file_manager.updateJson(config.CACHE_FILE_PATH, api.get_players(), cache_key_list[13])

            time.sleep(60)

        except AttributeError:
            error_message = traceback.format_exc()
            now = str(datetime.now())
            print(f'{now} - Error:\n{error_message}\n\n\n')
            time.sleep(60)
            info_updater()
            
            
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(process)d %(message)s')
    info_updater()
