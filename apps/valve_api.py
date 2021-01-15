import requests
import config

API_server_status = f'https://api.steampowered.com/ICSGOServers_730/GetGameServersStatus/v1?key={config.KEY}'
API_csgo_players = 'https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1?appid=730' 
API_dev_players = 'https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1?appid=710'
    

def get_response():
    response = requests.get(API_server_status)
    response = response.json()
    result = response['result']
    return result

def translate_ru(capacity_raw, load_raw, capacity_secondary_raw, load_secondary_raw, capacity_tertiary_raw, load_tertiary_raw):
    capacity_ru = ''
    load_ru = ''
    capacity = capacity_raw
    load = load_raw
    
    if capacity == 'full':
        capacity_ru = 'полная'
    elif capacity == 'offline':
        capacity_ru = 'офлайн'
    else:
        capacity_ru = capacity
        
    if load == 'idle':
        load_ru = 'никакая'
    elif load == 'low':
        load_ru = 'низкая'
    elif load == 'medium':
        load_ru = 'средняя'
    elif load == 'high':
        load_ru = 'высокая'
    elif load == 'full':
        load_ru = 'полная'
    else:
        load_ru = load
    
    capacity_secondary_ru = ''
    load_secondary_ru = ''
    capacity_secondary = capacity_secondary_raw
    load_secondary = load_secondary_raw
    
    if capacity_secondary == 'full':
        capacity_secondary_ru = 'полная'
    elif capacity_secondary == 'offline':
        capacity_secondary_ru = 'офлайн'
    else:
        capacity_secondary_ru = capacity_secondary

    if load_secondary == 'idle':
        load_secondary_ru = 'никакая'
    elif load_secondary == 'low':
        load_secondary_ru = 'низкая'
    elif load_secondary == 'medium':
        load_secondary_ru = 'средняя'
    elif load_secondary == 'high':
        load_secondary_ru = 'высокая'
    elif load_secondary == 'full':
        load_secondary_ru = 'полная'
    else:
        load_secondary_ru = load_secondary 
        
    capacity_tertiary_ru = ''
    load_tertiary_ru = ''
    capacity_tertiary = capacity_tertiary_raw
    load_tertiary = load_tertiary_raw
    
    if capacity_tertiary == 'full':
        capacity_tertiary_ru = 'полная'
    elif capacity_tertiary == 'offline':
        capacity_tertiary_ru = 'офлайн'
    else:
        capacity_tertiary_ru = capacity_tertiary

    if load_tertiary == 'idle':
        load_tertiary_ru = 'никакая'
    elif load_tertiary == 'low':
        load_tertiary_ru = 'низкая'
    elif load_tertiary == 'medium':
        load_tertiary_ru = 'средняя'
    elif load_tertiary == 'high':
        load_tertiary_ru = 'высокая'
    elif load_tertiary == 'full':
        load_tertiary_ru = 'полная'
    else:
        load_tertiary_ru = load_tertiary

    return capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru

class ValveServersAPI:

    def get_status(self): 
        try:
            result = get_response()

            matchmaking = result['matchmaking']
            
            scheduler = matchmaking['scheduler']
            sessionsLogon = result['services']['SessionsLogon']
            time_server = result['app']['time']

            online_servers = matchmaking['online_servers']
            online_players = matchmaking['online_players']
            searching_players = matchmaking['searching_players']        
            search_seconds_avg = matchmaking['search_seconds_avg']

            return scheduler, sessionsLogon, online_servers, online_players, time_server, search_seconds_avg, searching_players
        except:
            scheduler = 'N/A'
            sessionsLogon = 'N/A'
            online_servers = 'N/A'
            online_players = 'N/A'
            time_server = 'N/A'
            search_seconds_avg = 'N/A'
            searching_players = 'N/A'
            return scheduler, sessionsLogon, online_servers, online_players, time_server, search_seconds_avg, searching_players
            
    def get_players(self):
        try:
            response = requests.get(API_csgo_players)
            data = response.json()
            player_count = data['response']['player_count']

            return player_count
        except:
            player_count = 'N/A'
            return player_count
            
    def get_devs(self):
        try:
            response = requests.get(API_dev_players)
            data = response.json()
            dev_player_count = data['response']['player_count']

            return dev_player_count
        except:
            dev_player_count = 'N/A'
            return dev_player_count
            
    def check_status(self):
        try:
            response = requests.get(API_server_status)
            if response.status_code == 200:
                webapi_status = 'Normal'
            else:
                webapi_status = 'N/A'
            return webapi_status
        except requests.ConnectionError:
            webapi_status = 'N/A'
            return webapi_status
    
class ValveServersDataCentersAPI:

    #
    #   Australia
    #
    """Australia (Sydney)"""
    def australia(self):
        try:
            result = get_response()
            capacity_raw = result['datacenters']['Australia']['capacity']
            load_raw = result['datacenters']['Australia']['load']
            capacity_secondary_raw = load_secondary_raw = capacity_tertiary_raw = load_tertiary_raw = 'N/A'
            capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru = translate_ru(capacity_raw, load_raw, capacity_secondary_raw, load_secondary_raw, capacity_tertiary_raw, load_tertiary_raw)
            return capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru
        except:
            capacity = load = capacity_ru = load_ru = capacity_secondary = load_secondary = capacity_secondary_ru = load_secondary_ru = capacity_tertiary = load_tertiary = capacity_tertiary_ru = load_tertiary_ru = 'N/A'
            return capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru

 
    #
    #   South Africa
    #
    """South Africa (Johannesburg)"""
    def africa_South(self):
        try:
            result = get_response()
            capacity_raw = result['datacenters']['South Africa']['capacity']
            load_raw = result['datacenters']['South Africa']['load']
            capacity_secondary_raw = load_secondary_raw = capacity_tertiary_raw = load_tertiary_raw = 'N/A'
            capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru = translate_ru(capacity_raw, load_raw, capacity_secondary_raw, load_secondary_raw, capacity_tertiary_raw, load_tertiary_raw)
            return capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru
        except:
            capacity = load = capacity_ru = load_ru = capacity_secondary = load_secondary = capacity_secondary_ru = load_secondary_ru = capacity_tertiary = load_tertiary = capacity_tertiary_ru = load_tertiary_ru = 'N/A'
            return capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru
    
    #
    #   South America
    #
    """Brazil (Sao Paulo) && Chile, (Santiago) && Peru (Lima)"""
    def sa(self):
        try:
            result = get_response()
            capacity_raw = result['datacenters']['Brazil']['capacity']
            load_raw = result['datacenters']['Brazil']['load']
            capacity_secondary_raw = result['datacenters']['Chile']['capacity']
            load_secondary_raw = result['datacenters']['Chile']['load']
            capacity_tertiary_raw = result['datacenters']['Peru']['capacity']
            load_tertiary_raw = result['datacenters']['Peru']['load']
            capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru = translate_ru(capacity_raw, load_raw, capacity_secondary_raw, load_secondary_raw, capacity_tertiary_raw, load_tertiary_raw)
            return capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru
        except:
            capacity = load = capacity_ru = load_ru = capacity_secondary = load_secondary = capacity_secondary_ru = load_secondary_ru = capacity_tertiary = load_tertiary = capacity_tertiary_ru = load_tertiary_ru = 'N/A'
            return capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru

    #
    #   USA
    #
    """US Northcentral (Chicago) && US Northeast (Sterling) && US Northwest (Moses Lake)"""
    def usa_North(self):
        try:
            result = get_response()
            capacity_raw = result['datacenters']['US Northcentral']['capacity']
            load_raw = result['datacenters']['US Northcentral']['load']
            capacity_secondary_raw = result['datacenters']['US Northeast']['capacity']
            load_secondary_raw = result['datacenters']['US Northeast']['load']
            capacity_tertiary_raw = result['datacenters']['US Northwest']['capacity']
            load_tertiary_raw = result['datacenters']['US Northwest']['load']
            capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru = translate_ru(capacity_raw, load_raw, capacity_secondary_raw, load_secondary_raw, capacity_tertiary_raw, load_tertiary_raw)
            return capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru
        except:
            capacity = load = capacity_ru = load_ru = capacity_secondary = load_secondary = capacity_secondary_ru = load_secondary_ru = capacity_tertiary = load_tertiary = capacity_tertiary_ru = load_tertiary_ru = 'N/A'
            return capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru

    """US Southwest (Los Angeles) && US Southeast (Atlanta)"""
    def usa_South(self):
        try:
            result = get_response()
            capacity_raw = result['datacenters']['US Southwest']['capacity']
            load_raw = result['datacenters']['US Southwest']['load']
            capacity_secondary_raw = result['datacenters']['US Southeast']['capacity']
            load_secondary_raw = result['datacenters']['US Southeast']['load']
            capacity_tertiary_raw = load_tertiary_raw = 'N/A'
            capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru = translate_ru(capacity_raw, load_raw, capacity_secondary_raw, load_secondary_raw, capacity_tertiary_raw, load_tertiary_raw)
            return capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru
        except:
            capacity = load = capacity_ru = load_ru = capacity_secondary = load_secondary = capacity_secondary_ru = load_secondary_ru = capacity_tertiary = load_tertiary = capacity_tertiary_ru = load_tertiary_ru = 'N/A'
            return capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru

    #
    #   Europe
    #
    """EU West (Luxembourg) && Spain (Mardid)"""   
    def eu_West(self):
        try:
            result = get_response()
            capacity_raw = result['datacenters']['EU West']['capacity']
            load_raw = result['datacenters']['EU West']['load']
            capacity_secondary_raw = result['datacenters']['Spain']['capacity']
            load_secondary_raw = result['datacenters']['Spain']['load']
            capacity_tertiary_raw = load_tertiary_raw = 'N/A'
            capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru = translate_ru(capacity_raw, load_raw, capacity_secondary_raw, load_secondary_raw, capacity_tertiary_raw, load_tertiary_raw)
            return capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru
        except:
            capacity = load = capacity_ru = load_ru = capacity_secondary = load_secondary = capacity_secondary_ru = load_secondary_ru = capacity_tertiary = load_tertiary = capacity_tertiary_ru = load_tertiary_ru = 'N/A'
            return capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru
        
    """EU East (Vienna) && Poland (Warsaw)"""
    def eu_East(self):
        try:
            result = get_response()
            capacity_raw = result['datacenters']['EU East']['capacity']
            load_raw = result['datacenters']['EU East']['load']
            capacity_secondary_raw = result['datacenters']['Poland']['capacity']
            load_secondary_raw = result['datacenters']['Poland']['load']
            capacity_tertiary_raw = load_tertiary_raw = 'N/A'
            capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru = translate_ru(capacity_raw, load_raw, capacity_secondary_raw, load_secondary_raw, capacity_tertiary_raw, load_tertiary_raw)
            return capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru
        except:
            capacity = load = capacity_ru = load_ru = capacity_secondary = load_secondary = capacity_secondary_ru = load_secondary_ru = capacity_tertiary = load_tertiary = capacity_tertiary_ru = load_tertiary_ru = 'N/A'
            return capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru
    
    """EU North (Stockholm)"""
    def eu_North(self):
        try:
            result = get_response()
            capacity_raw = result['datacenters']['EU North']['capacity']
            load_raw = result['datacenters']['EU North']['load']
            capacity_secondary_raw = load_secondary_raw = capacity_tertiary_raw = load_tertiary_raw = 'N/A'
            capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru = translate_ru(capacity_raw, load_raw, capacity_secondary_raw, load_secondary_raw, capacity_tertiary_raw, load_tertiary_raw)
            return capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru
        except:
            capacity = load = capacity_ru = load_ru = capacity_secondary = load_secondary = capacity_secondary_ru = load_secondary_ru = capacity_tertiary = load_tertiary = capacity_tertiary_ru = load_tertiary_ru = 'N/A'
            return capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru

    #
    #    Asia   
    #
    """India (Mumbai) && India East (Chennai)"""
    def india(self):
        try:
            result = get_response()
            capacity_raw = result['datacenters']['India']['capacity']
            load_raw = result['datacenters']['India']['load']
            capacity_secondary_raw = result['datacenters']['India East']['capacity']
            load_secondary_raw = result['datacenters']['India East']['load']
            capacity_tertiary_raw = load_tertiary_raw = 'N/A'
            capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru = translate_ru(capacity_raw, load_raw, capacity_secondary_raw, load_secondary_raw, capacity_tertiary_raw, load_tertiary_raw)
            return capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru
        except:
            capacity = load = capacity_ru = load_ru = capacity_secondary = load_secondary = capacity_secondary_ru = load_secondary_ru = capacity_tertiary = load_tertiary = capacity_tertiary_ru = load_tertiary_ru = 'N/A'
            return capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru
    
    """Japan (Tokyo)"""
    def japan(self):

        try:
            result = get_response()
            capacity_raw = result['datacenters']['Japan']['capacity']
            load_raw = result['datacenters']['Japan']['load']
            capacity_secondary_raw = load_secondary_raw = capacity_tertiary_raw = load_tertiary_raw = 'N/A'
            capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru = translate_ru(capacity_raw, load_raw, capacity_secondary_raw, load_secondary_raw, capacity_tertiary_raw, load_tertiary_raw)
            return capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru
        except:
            capacity = load = capacity_ru = load_ru = capacity_secondary = load_secondary = capacity_secondary_ru = load_secondary_ru = capacity_tertiary = load_tertiary = capacity_tertiary_ru = load_tertiary_ru = 'N/A'
            return capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru
            
    """Emirates (Dubai)"""
    def emirates(self):
        try:
            result = get_response()
            capacity_raw = result['datacenters']['Emirates']['capacity']
            load_raw = result['datacenters']['Emirates']['load']
            capacity_secondary_raw = load_secondary_raw = capacity_tertiary_raw = load_tertiary_raw = 'N/A'
            capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru = translate_ru(capacity_raw, load_raw, capacity_secondary_raw, load_secondary_raw, capacity_tertiary_raw, load_tertiary_raw)
            return capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru
        except:
            capacity = load = capacity_ru = load_ru = capacity_secondary = load_secondary = capacity_secondary_ru = load_secondary_ru = capacity_tertiary = load_tertiary = capacity_tertiary_ru = load_tertiary_ru = 'N/A'
            return capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru

    """China Shanghai && China Tianjin && China Guangzhou"""
    def china(self):
        try:
            result = get_response()
            capacity_raw = result['datacenters']['China Shanghai']['capacity']
            load_raw = result['datacenters']['China Shanghai']['load']
            capacity_secondary_raw = result['datacenters']['China Tianjin']['capacity']
            load_secondary_raw = result['datacenters']['China Tianjin']['load']
            capacity_tertiary_raw = result['datacenters']['China Guangzhou']['capacity']
            load_tertiary_raw = result['datacenters']['China Guangzhou']['load']
            capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru = translate_ru(capacity_raw, load_raw, capacity_secondary_raw, load_secondary_raw, capacity_tertiary_raw, load_tertiary_raw)
            return capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru
        except:
            capacity = load = capacity_ru = load_ru = capacity_secondary = load_secondary = capacity_secondary_ru = load_secondary_ru = capacity_tertiary = load_tertiary = capacity_tertiary_ru = load_tertiary_ru = 'N/A'
            return capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru
   
    """Singapore"""
    def singapore(self):
        try:
            result = get_response()
            capacity_raw = result['datacenters']['Singapore']['capacity']
            load_raw = result['datacenters']['Singapore']['load']
            capacity_secondary_raw = load_secondary_raw = capacity_tertiary_raw = load_tertiary_raw = 'N/A'
            capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru = translate_ru(capacity_raw, load_raw, capacity_secondary_raw, load_secondary_raw, capacity_tertiary_raw, load_tertiary_raw)
            return capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru
        except:
            capacity = load = capacity_ru = load_ru = capacity_secondary = load_secondary = capacity_secondary_ru = load_secondary_ru = capacity_tertiary = load_tertiary = capacity_tertiary_ru = load_tertiary_ru = 'N/A'
            return capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru
            
    """Hong Kong"""
    def hong_kong(self):
        try:
            result = get_response()
            capacity_raw = result['datacenters']['Hong Kong']['capacity']
            load_raw = result['datacenters']['Hong Kong']['load']
            capacity_secondary_raw = load_secondary_raw = capacity_tertiary_raw = load_tertiary_raw = 'N/A'
            capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru = translate_ru(capacity_raw, load_raw, capacity_secondary_raw, load_secondary_raw, capacity_tertiary_raw, load_tertiary_raw)
            return capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru
        except:
            capacity = load = capacity_ru = load_ru = capacity_secondary = load_secondary = capacity_secondary_ru = load_secondary_ru = capacity_tertiary = load_tertiary = capacity_tertiary_ru = load_tertiary_ru = 'N/A'
            return capacity, load, capacity_ru, load_ru, capacity_secondary, load_secondary, capacity_secondary_ru, load_secondary_ru, capacity_tertiary, load_tertiary, capacity_tertiary_ru, load_tertiary_ru
