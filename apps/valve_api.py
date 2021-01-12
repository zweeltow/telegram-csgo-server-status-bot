import requests
import config


API_1 = f'https://api.steampowered.com/ICSGOServers_730/GetGameServersStatus/v1?key={config.KEY}'
API_2 = 'https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1?appid=730' 
API_3 = 'https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1?appid=710'

def get_response():
    response = requests.get(API_1)
    response = response.json()
    result = response['result']

    return result

class ValveServersAPI:

    def first_api(self): 
    
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
        
        
    def second_api(self):

        response = requests.get(API_2)
        data = response.json()
        player_count = data['response']['player_count']

        return player_count

        
        
    def third_api(self):

        response = requests.get(API_3)
        data = response.json()
        dev_player_count = data['response']['player_count']

        return dev_player_count
    
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



        return capacity, load

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



        return capacity, load
    
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



        return capacity_Chile, capacity_Peru, capacity_Brazil, load_Chile, load_Peru, load_Brazil

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



        return capacity_US_Northcentral, capacity_US_Northeast, capacity_US_Northwest, load_US_Northcentral, load_US_Northeast, load_US_Northwest

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



        return capacity_US_Southeast, capacity_US_Southwest, load_US_Southeast, load_US_Southwest

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



        return capacity, load, capacity_Spain, load_Spain
        
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



        return capacity_East, capacity_Poland, load_East, load_Poland

    def eu_North(self):
        """
        EU North (Stockholm)"""
        result = get_response()
        datacenters = result['datacenters']

        EU_North = datacenters['EU North']
        capacity = EU_North['capacity']
        load = EU_North['load']



        return capacity, load

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



        return capacity, capacity_East, load, load_East

    def japan(self):
        '''
        Japan (Tokyo)'''
        result = get_response()
        datacenters = result['datacenters']

        Japan = datacenters['Japan']
        capacity = Japan['capacity']
        load = Japan['load']
        


        return capacity, load

    def emirates(self):
        '''
        Emirates (Dubai)'''
        result = get_response()
        datacenters = result['datacenters']

        Emirates = datacenters['Emirates']
        capacity = Emirates['capacity']
        load = Emirates['load']



        return capacity, load

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



        return capacity_Shanghai, capacity_Tianjin, capacity_Guangzhou, load_Shanghai, load_Tianjin, load_Guangzhou

    def singapore(self):
        '''
        Singapore'''
        result = get_response()
        datacenters = result['datacenters']

        Singapore = datacenters['Singapore']
        capacity = Singapore['capacity']
        load = Singapore['load']



        return capacity, load 

    def hong_kong(self):
        '''
        Hong Kong'''
        result = get_response()
        datacenters = result['datacenters']

        Hong_Kong = datacenters['Hong Kong']
        capacity = Hong_Kong['capacity']
        load = Hong_Kong['load']



        return capacity, load 
