import json
from datetime import datetime
import time
import traceback
import logging
from apps import file_manager

from apps.valve_api import ValveServersAPI
from apps.scrapper import PeakOnline, Monthly, CSGOGameCoordinator

JSON_FILE_PATH = "/root/tgbot/telegram-csgo-server-status-bot/cache.json"

api = ValveServersAPI()
peak_count = PeakOnline()
month_unique = Monthly()
gc = CSGOGameCoordinator()


def info_updater():
    while True:
        try:
            gc_status = gc.get_status()[0]
            webapi_status = gc.get_status()[1]
            sessionsLogon = api.get_status()[1]
            player_count = api.get_players()
            time_server = api.get_status()[4]
            scheduler = api.get_status()[0]
            server_count = api.get_status()[2]
            online_players = api.get_status()[3]
            search_seconds_avg = api.get_status()[5]
            searching_players = api.get_status()[6]
            dev_player_count = api.get_devs()
            peak24 = peak_count.get_peak()[0]
            peak_all = peak_count.get_peak()[1]
            unique = month_unique.get_unique()
            
            cacheFile = file_manager.readJson(JSON_FILE_PATH)
            
            gcCache = cacheFile['game_coordinator']
            wsCache = cacheFile['valve_webapi']
            slCache = cacheFile['sessionsLogon']
            pcCache = cacheFile['online_player_count']
            tsCache = cacheFile['time_server']
            sCache = cacheFile['scheduler']
            scCache = cacheFile['online_server_count']
            apCache = cacheFile['active_player_count']
            ssCache = cacheFile['search_seconds_avg']
            spCache = cacheFile['searching_players']
            dcCache = cacheFile['dev_player_count']
            p24Cache = cacheFile['peak_24_hours']
            paCache = cacheFile['peak_all_time']
            uqCache = cacheFile['unique_monthly']

            if gc_status != gcCache:
                file_manager.updateJsonGC(JSON_FILE_PATH, gc_status)
              
            if webapi_status != wsCache:
                file_manager.updateJsonWS(JSON_FILE_PATH, webapi_status)
                
            if sessionsLogon != slCache:
                file_manager.updateJsonSL(JSON_FILE_PATH, sessionsLogon)
                
            if player_count != pcCache:
                file_manager.updateJsonPC(JSON_FILE_PATH, player_count)
                
            if time_server != tsCache:
                file_manager.updateJsonTS(JSON_FILE_PATH, time_server)
                
            if scheduler != sCache:
                file_manager.updateJsonS(JSON_FILE_PATH, scheduler)
            
            if server_count != scCache:
                file_manager.updateJsonSC(JSON_FILE_PATH, server_count)
                
            if online_players != apCache:
                file_manager.updateJsonAP(JSON_FILE_PATH, online_players)
                
            if search_seconds_avg != ssCache:
                file_manager.updateJsonSS(JSON_FILE_PATH, search_seconds_avg)
                
            if searching_players != spCache:
                file_manager.updateJsonSP(JSON_FILE_PATH, searching_players)
               
            if dev_player_count != dcCache:
                file_manager.updateJsonDC(JSON_FILE_PATH, dev_player_count)
                
            if peak24 != p24Cache:
                file_manager.updateJsonP24(JSON_FILE_PATH, peak24)
                
            if peak_all != paCache:
                file_manager.updateJsonPA(JSON_FILE_PATH, peak_all)
                
            if unique != uqCache:
                file_manager.updateJsonUQ(JSON_FILE_PATH, unique)

            time.sleep(10)

        except AttributeError:
            error_message = traceback.format_exc()
            now = str(datetime.now())
            print(f'{now} - Error:\n{error_message}\n\n\n')
            time.sleep(60)
            info_updater()
            
            
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(process)d %(message)s')
    info_updater()
