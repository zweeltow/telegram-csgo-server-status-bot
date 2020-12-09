import requests
import config


API = f'https://api.steampowered.com/ICSGOServers_730/GetGameServersStatus/v1?key={config.KEY}'
API_player_count = 'https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1?appid=730' 
API_dev_count = 'https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1?appid=710'


def get_response():
    
    response = requests.get(API)
    response = response.json()
    result = response['result']

    return result


class ValveServersAPI:

    def status(self):
        result = get_response()

        services = result['services']
        SessionsLogon = services['SessionsLogon']
        app = result['app']
        time_server = app['time']

        response_player_count = requests.get(API_player_count)
        json_response_player_count = response_player_count.json()
        response1 = json_response_player_count['response']
        player_count = response1['player_count']

        return SessionsLogon, player_count, time_server


    def matchmaking(self):
        result = get_response()

        matchmaking = result['matchmaking']
        scheduler = matchmaking['scheduler']
        online_servers = matchmaking['online_servers']
        online_players = matchmaking['online_players']
        searching_players = matchmaking['searching_players']
        app = result['app']
        time_server = app['time']
        search_seconds_avg = matchmaking['search_seconds_avg']

        return scheduler, online_servers, online_players, time_server, search_seconds_avg, searching_players
        
        
    def devcount(self):
        result = get_response()

        app = result['app']
        time_server = app['time']

        response_dev_player_count = requests.get(API_dev_count)
        json_response_dev_player_count = response_dev_player_count.json()
        response1 = json_response_dev_player_count['response']
        dev_player_count = response1['player_count']

        return dev_player_count, time_server
    

class ValveServersDataCentersAPI:

#
#   Australia
#

    def australia(self):
        """
        Australia (Sydney)"""
        result = get_response()
        datacenters = result['datacenters']

        Australia = datacenters['Australia']
        capacity = Australia['capacity']
        load = Australia['load']

        app = result['app']
        time_server = app['time']

        return capacity, load, time_server

#
#   South Africa
#

    def africa_South(self):
        """
        South Africa (Johannesburg)"""
        result = get_response()
        datacenters = result['datacenters']

        South_Africa = datacenters['South Africa']
        capacity = South_Africa['capacity']
        load = South_Africa['load']

        app = result['app']
        time_server = app['time']

        return capacity, load, time_server
    
#
#   South America
#

    def sa(self):
        """
        Brazil (Sao Paulo), 
        Chile, (Santiago), 
        Peru (Lima)"""

        result = get_response()
        datacenters = result['datacenters']

        Brazil = datacenters['Brazil']
        capacity_Brazil = Brazil['capacity']
        load_Brazil = Brazil['load']

        Chile = datacenters['Chile']
        capacity_Chile = Chile['capacity']
        load_Chile = Chile['load']

        Peru = datacenters['Peru']
        capacity_Peru = Peru['capacity']
        load_Peru = Peru['load']

        app = result['app']
        time_server = app['time']

        return capacity_Chile, capacity_Peru, capacity_Brazil, load_Chile, load_Peru, load_Brazil, time_server

#
#   USA
#

    def usa_North(self):
        """
        US Northcentral (Chicago)
        US Northeast (Sterling)
        US Northwest (Moses Lake)"""
        
        result = get_response()
        datacenters = result['datacenters']

        US_Northcentral = datacenters['US Northcentral']
        capacity_US_Northcentral = US_Northcentral['capacity']
        load_US_Northcentral = US_Northcentral['load']

        US_Northeast = datacenters['US Northeast']
        capacity_US_Northeast = US_Northeast['capacity']
        load_US_Northeast = US_Northeast['load']

        US_Northwest = datacenters['US Northwest']
        capacity_US_Northwest = US_Northwest['capacity']
        load_US_Northwest = US_Northwest['load']

        app = result['app']
        time_server = app['time']

        return capacity_US_Northcentral, capacity_US_Northeast, capacity_US_Northwest, load_US_Northcentral, load_US_Northeast, load_US_Northwest, time_server

    def usa_South(self):
        """
        US Southwest (Los Angeles)
        US Southeast (Atlanta)"""

        result = get_response()
        datacenters = result['datacenters']

        US_Southwest = datacenters['US Southwest']
        capacity_US_Southwest = US_Southwest['capacity']
        load_US_Southwest = US_Southwest['load']

        US_Southeast = datacenters['US Southeast']
        capacity_US_Southeast = US_Southeast['capacity']
        load_US_Southeast = US_Southeast['load']

        app = result['app']
        time_server = app['time']

        return capacity_US_Southeast, capacity_US_Southwest, load_US_Southeast, load_US_Southwest, time_server

#
#   Europe
#

    def eu_West(self):
        """
        EU West (Luxembourg)"""
        result = get_response()
        datacenters = result['datacenters']

        EU_West = datacenters['EU West']
        capacity = EU_West['capacity']
        load = EU_West['load']

        Spain = datacenters['Spain']
        capacity_Spain = Spain['capacity']
        load_Spain = Spain['load']

        app = result['app']
        time_server = app['time']

        return capacity, load, capacity_Spain, load_Spain, time_server
        

    def eu_East(self):
        """
        EU East (Vienna)
        Spain (Mardid)
        Poland (Warsaw)"""
        result = get_response()
        datacenters = result['datacenters']

        EU_East = datacenters['EU East']
        capacity_East = EU_East['capacity']
        load_East = EU_East['load']

        Spain = datacenters['Spain']
        capacity_Spain = Spain['capacity']
        load_Spain = Spain['load']

        Poland = datacenters['Poland']
        capacity_Poland = Poland['capacity']
        load_Poland = Poland['load']

        app = result['app']
        time_server = app['time']

        return capacity_East, capacity_Poland, load_East, load_Poland, time_server

    def eu_North(self):
        """
        EU North (Stockholm)"""
        result = get_response()
        datacenters = result['datacenters']

        EU_North = datacenters['EU North']
        capacity = EU_North['capacity']
        load = EU_North['load']

        app = result['app']
        time_server = app['time']

        return capacity, load, time_server

#
#    Asia   
#

    def india(self):
        '''
        India (Mumbai)
        India East (Chennai)'''
        result = get_response()
        datacenters = result['datacenters']

        India = datacenters['India']
        capacity = India['capacity']
        load = India['load']

        India_East = datacenters['India East']
        capacity_East = India_East['capacity']
        load_East = India_East['load']

        app = result['app']
        time_server = app['time']

        return capacity, capacity_East, load, load_East, time_server

    def japan(self):
        '''
        Japan (Tokyo)'''
        result = get_response()
        datacenters = result['datacenters']

        Japan = datacenters['Japan']
        capacity = Japan['capacity']
        load = Japan['load']
        
        app = result['app']
        time_server = app['time']

        return capacity, load, time_server

    def emirates(self):
        '''
        Emirates (Dubai)'''
        result = get_response()
        datacenters = result['datacenters']

        Emirates = datacenters['Emirates']
        capacity = Emirates['capacity']
        load = Emirates['load']

        app = result['app']
        time_server = app['time']

        return capacity, load, time_server

    def china(self):
        '''
        China Shanghai
        China Tianjin
        China Guangzhou'''
        result = get_response()
        datacenters = result['datacenters']

        China_Shanghai = datacenters['China Shanghai']
        capacity_Shanghai = China_Shanghai['capacity']
        load_Shanghai = China_Shanghai['load']

        China_Tianjin = datacenters['China Tianjin']
        capacity_Tianjin = China_Tianjin['capacity']
        load_Tianjin = China_Tianjin['load']

        China_Guangzhou = datacenters['China Guangzhou']
        capacity_Guangzhou = China_Guangzhou['capacity']
        load_Guangzhou = China_Guangzhou['load']

        app = result['app']
        time_server = app['time']

        return capacity_Shanghai, capacity_Tianjin, capacity_Guangzhou, load_Shanghai, load_Tianjin, load_Guangzhou, time_server

    def singapore(self):
        '''
        Singapore'''
        result = get_response()
        datacenters = result['datacenters']

        Singapore = datacenters['Singapore']
        capacity = Singapore['capacity']
        load = Singapore['load']

        app = result['app']
        time_server = app['time']

        return capacity, load, time_server

    def hong_kong(self):
        '''
        Hong Kong'''
        result = get_response()
        datacenters = result['datacenters']

        Hong_Kong = datacenters['Hong Kong']
        capacity = Hong_Kong['capacity']
        load = Hong_Kong['load']

        app = result['app']
        time_server = app['time']

        return capacity, load, time_server
