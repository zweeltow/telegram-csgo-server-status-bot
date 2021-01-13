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

    def australia(self):
        """
        Australia (Sydney)"""
        try:
            result = get_response()        
            datacenters = result['datacenters']

            Australia = datacenters['Australia']
            capacity = Australia['capacity']
            load = Australia['load']
            
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
            else:
                load_ru = load
            return capacity, load, capacity_ru, load_ru
            
        except:
            capacity = 'N/A'
            load = 'N/A'
            capacity_ru = 'N/A'
            load_ru = 'N/A'
            return capacity, load, capacity_ru, load_ru

#
#   South Africa
#

    def africa_South(self):
        """
        South Africa (Johannesburg)"""
        try:
            result = get_response()
            datacenters = result['datacenters']

            South_Africa = datacenters['South Africa']
            capacity = South_Africa['capacity']
            load = South_Africa['load']
                    
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
            else:
                load_ru = load

            return capacity, load, capacity_ru, load_ru
        except:
            capacity = 'N/A'
            load = 'N/A'
            capacity_ru = 'N/A'
            load_ru = 'N/A'
            return capacity, load, capacity_ru, load_ru
    
#
#   South America
#

    def sa(self):
        """
        Brazil (Sao Paulo), 
        Chile, (Santiago), 
        Peru (Lima)"""
        try:
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

            if capacity_Brazil == 'full':
                capacity_Brazil_ru = 'полная'
            elif capacity_Brazil == 'offline':
                capacity_Brazil_ru = 'офлайн'
            else:
                capacity_Brazil_ru = capacity_Brazil        
                
            if capacity_Chile == 'full':
                capacity_Chile_ru = 'полная'
            elif capacity_Chile == 'offline':
                capacity_Chile_ru = 'офлайн'
            else:
                capacity_Chile_ru = capacity_Chile
                        
            if capacity_Peru == 'full':
                capacity_Peru_ru = 'полная'
            elif capacity_Peru == 'offline':
                capacity_Peru_ru = 'офлайн'
            else:
                capacity_Peru_ru = capacity_Peru
                
            if load_Brazil == 'idle':
                load_Brazil_ru = 'никакая'
            elif load_Brazil == 'low':
                load_Brazil_ru = 'низкая'
            elif load_Brazil == 'medium':
                load_Brazil_ru = 'средняя'
            elif load_Brazil == 'high':
                load_Brazil_ru = 'высокая'
            else:
                load_Brazil_ru = load_Brazil
                
            if load_Chile == 'idle':
                load_Chile_ru = 'никакая'
            elif load_Chile == 'low':
                load_Chile_ru = 'низкая'
            elif load_Chile == 'medium':
                load_Chile_ru = 'средняя'
            elif load_Chile == 'high':
                load_Chile_ru = 'высокая'
            else:
                load_Chile_ru = load_Chile
                
            if load_Peru == 'idle':
                load_Peru_ru = 'никакая'
            elif load_Peru == 'low':
                load_Peru_ru = 'низкая'
            elif load_Peru == 'medium':
                load_Peru_ru = 'средняя'
            elif load_Peru == 'high':
                load_Peru_ru = 'высокая'
            else:
                load_Peru_ru = load_Peru


            return capacity_Chile, capacity_Peru, capacity_Brazil, load_Chile, load_Peru, load_Brazil, load_Brazil_ru, capacity_Brazil_ru, load_Chile_ru, capacity_Chile_ru, load_Peru_ru, capacity_Peru_ru
        except:
            capacity_Chile = 'N/A'
            capacity_Peru = 'N/A'
            capacity_Brazil = 'N/A'
            load_Chile = 'N/A'
            load_Peru = 'N/A'
            load_Brazil = 'N/A'
            load_Brazil_ru = 'N/A'
            capacity_Brazil_ru = 'N/A'
            load_Chile_ru = 'N/A'
            capacity_Chile_ru = 'N/A'
            load_Peru_ru = 'N/A'
            capacity_Peru_ru = 'N/A'
            return capacity_Chile, capacity_Peru, capacity_Brazil, load_Chile, load_Peru, load_Brazil, load_Brazil_ru, capacity_Brazil_ru, load_Chile_ru, capacity_Chile_ru, load_Peru_ru, capacity_Peru_ru

#
#   USA
#

    def usa_North(self):
        """
        US Northcentral (Chicago)
        US Northeast (Sterling)
        US Northwest (Moses Lake)"""
        try:
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

            if capacity_US_Northcentral == 'full':
                capacity_US_Northcentral_ru = 'полная'
            elif capacity_US_Northcentral == 'offline':
                capacity_US_Northcentral_ru = 'офлайн'
            else:
                capacity_US_Northcentral_ru = capacity_US_Northcentral        
                
            if capacity_US_Northeast == 'full':
                capacity_US_Northeast_ru = 'полная'
            elif capacity_US_Northeast == 'offline':
                capacity_US_Northeast_ru = 'офлайн'
            else:
                capacity_US_Northeast_ru = capacity_US_Northeast
                        
            if capacity_US_Northwest == 'full':
                capacity_US_Northwest_ru = 'полная'
            elif capacity_US_Northwest == 'offline':
                capacity_US_Northwest_ru = 'офлайн'
            else:
                capacity_US_Northwest_ru = capacity_US_Northwest
                
            if load_US_Northcentral == 'idle':
                load_US_Northcentral_ru = 'никакая'
            elif load_US_Northcentral == 'low':
                load_US_Northcentral_ru = 'низкая'
            elif load_US_Northcentral == 'medium':
                load_US_Northcentral_ru = 'средняя'
            elif load_US_Northcentral == 'high':
                load_US_Northcentral_ru = 'высокая'
            else:
                load_US_Northcentral_ru = load_US_Northcentral
                
            if load_US_Northeast == 'idle':
                load_US_Northeast_ru = 'никакая'
            elif load_US_Northeast == 'low':
                load_US_Northeast_ru = 'низкая'
            elif load_US_Northeast == 'medium':
                load_US_Northeast_ru = 'средняя'
            elif load_US_Northeast == 'high':
                load_US_Northeast_ru = 'высокая'
            else:
                load_US_Northeast_ru = load_US_Northeast  
                
            if load_US_Northwest == 'idle':
                load_US_Northwest_ru = 'никакая'
            elif load_US_Northwest == 'low':
                load_US_Northwest_ru = 'низкая'
            elif load_US_Northwest == 'medium':
                load_US_Northwest_ru = 'средняя'
            elif load_US_Northwest == 'high':
                load_US_Northwest_ru = 'высокая'
            else:
                load_US_Northwest_ru = load_US_Northwest

            return capacity_US_Northcentral, capacity_US_Northeast, capacity_US_Northwest, load_US_Northcentral, load_US_Northeast, load_US_Northwest, load_US_Northcentral_ru, capacity_US_Northcentral_ru, load_US_Northeast_ru, capacity_US_Northeast_ru, load_US_Northwest_ru, capacity_US_Northwest_ru
        except:
            capacity_US_Northcentral = 'N/A'
            capacity_US_Northeast = 'N/A'
            capacity_US_Northwest = 'N/A'
            load_US_Northcentral = 'N/A'
            load_US_Northeast = 'N/A'
            load_US_Northwest = 'N/A'
            load_US_Northcentral_ru = 'N/A'
            capacity_US_Northcentral_ru = 'N/A'
            load_US_Northeast_ru = 'N/A'
            capacity_US_Northeast_ru = 'N/A'
            load_US_Northwest_ru = 'N/A'
            capacity_US_Northwest_ru = 'N/A'
            return capacity_US_Northcentral, capacity_US_Northeast, capacity_US_Northwest, load_US_Northcentral, load_US_Northeast, load_US_Northwest, load_US_Northcentral_ru, capacity_US_Northcentral_ru, load_US_Northeast_ru, capacity_US_Northeast_ru, load_US_Northwest_ru, capacity_US_Northwest_ru

    def usa_South(self):
        """
        US Southwest (Los Angeles)
        US Southeast (Atlanta)"""
        try:
            result = get_response()
            datacenters = result['datacenters']

            US_Southwest = datacenters['US Southwest']
            capacity_US_Southwest = US_Southwest['capacity']
            load_US_Southwest = US_Southwest['load']

            US_Southeast = datacenters['US Southeast']
            capacity_US_Southeast = US_Southeast['capacity']
            load_US_Southeast = US_Southeast['load']

            if capacity_US_Southeast == 'full':
                capacity_US_Southeast_ru = 'полная'
            elif capacity_US_Southeast == 'offline':
                capacity_US_Southeast_ru = 'офлайн'
            else:
                capacity_US_Southeast_ru = capacity_US_Southeast        
                
            if capacity_US_Southwest == 'full':
                capacity_US_Southwest_ru = 'полная'
            elif capacity_US_Southwest == 'offline':
                capacity_US_Southwest_ru = 'офлайн'
            else:
                capacity_US_Southwest_ru = capacity_US_Southwest
                
            if load_US_Southeast == 'idle':
                load_US_Southeast_ru = 'никакая'
            elif load_US_Southeast == 'low':
                load_US_Southeast_ru = 'низкая'
            elif load_US_Southeast == 'medium':
                load_US_Southeast_ru = 'средняя'
            elif load_US_Southeast == 'high':
                load_US_Southeast_ru = 'высокая'
            else:
                load_US_Southeast_ru = load_US_Southeast
                
            if load_US_Southwest == 'idle':
                load_US_Southwest_ru = 'никакая'
            elif load_US_Southwest == 'low':
                load_US_Southwest_ru = 'низкая'
            elif load_US_Southwest == 'medium':
                load_US_Southwest_ru = 'средняя'
            elif load_US_Southwest == 'high':
                load_US_Southwest_ru = 'высокая'
            else:
                load_US_Southwest_ru = load_US_Southwest  
            
            return capacity_US_Southeast, capacity_US_Southwest, load_US_Southeast, load_US_Southwest, load_US_Southwest_ru, capacity_US_Southwest_ru, load_US_Southeast_ru, capacity_US_Southeast_ru
        except:
            capacity_US_Southeast = 'N/A'
            capacity_US_Southwest = 'N/A'
            load_US_Southeast = 'N/A'
            load_US_Southwest = 'N/A'
            load_US_Southwest_ru = 'N/A'
            capacity_US_Southwest_ru = 'N/A'
            load_US_Southeast_ru = 'N/A'
            capacity_US_Southeast_ru = 'N/A'
            return capacity_US_Southeast, capacity_US_Southwest, load_US_Southeast, load_US_Southwest, load_US_Southwest_ru, capacity_US_Southwest_ru, load_US_Southeast_ru, capacity_US_Southeast_ru

#
#   Europe
#

    def eu_West(self):
        """
        EU West (Luxembourg)    
        Spain (Mardid)"""    
        try:
            result = get_response()
            datacenters = result['datacenters']

            EU_West = datacenters['EU West']
            capacity = EU_West['capacity']
            load = EU_West['load']

            Spain = datacenters['Spain']
            capacity_Spain = Spain['capacity']
            load_Spain = Spain['load']
            
            if capacity == 'full':
                capacity_ru = 'полная'
            elif capacity == 'offline':
                capacity_ru = 'офлайн'
            else:
                capacity_ru = capacity
                
            if capacity_Spain == 'full':
                capacity_Spain_ru = 'полная'
            elif capacity_Spain == 'offline':
                capacity_Spain_ru = 'офлайн'
            else:
                capacity_Spain_ru = capacity_Spain
                
            if load == 'idle':
                load_ru = 'никакая'
            elif load == 'low':
                load_ru = 'низкая'
            elif load == 'medium':
                load_ru = 'средняя'
            elif load == 'high':
                load_ru = 'высокая'
            else:
                load_ru = load
                        
            if load_Spain == 'idle':
                load_Spain_ru = 'никакая'
            elif load_Spain == 'low':
                load_Spain_ru = 'низкая'
            elif load_Spain == 'medium':
                load_Spain_ru = 'средняя'
            elif load_Spain == 'high':
                load_Spain_ru = 'высокая'
            else:
                load_Spain_ru = load_Spain
                
            return capacity, load, capacity_Spain, load_Spain, capacity_ru, load_ru, capacity_Spain_ru, load_Spain_ru
        except:
            capacity = 'N/A'
            load = 'N/A'
            capacity_Spain = 'N/A'
            load_Spain = 'N/A'
            capacity_ru = 'N/A'
            load_ru = 'N/A'
            capacity_Spain_ru = 'N/A'
            return capacity, load, capacity_Spain, load_Spain, capacity_ru, load_ru, capacity_Spain_ru, load_Spain_ru
        
    def eu_East(self):
        """
        EU East (Vienna)
        Poland (Warsaw)"""
        try:
            result = get_response()
            datacenters = result['datacenters']

            EU_East = datacenters['EU East']
            capacity = EU_East['capacity']
            load = EU_East['load']

            Poland = datacenters['Poland']
            capacity_Poland = Poland['capacity']
            load_Poland = Poland['load']

            if capacity == 'full':
                capacity_ru = 'полная'
            elif capacity == 'offline':
                capacity_ru = 'офлайн'
            else:
                capacity_ru = capacity
                
            if capacity_Poland == 'full':
                capacity_Poland_ru = 'полная'
            elif capacity_Poland == 'offline':
                capacity_Poland_ru = 'офлайн'
            else:
                capacity_Poland_ru = capacity_Poland
                
            if load == 'idle':
                load_ru = 'никакая'
            elif load == 'low':
                load_ru = 'низкая'
            elif load == 'medium':
                load_ru = 'средняя'
            elif load == 'high':
                load_ru = 'высокая'
            else:
                load_ru = load

            if load_Poland == 'idle':
                load_Poland_ru = 'никакая'
            elif load_Poland == 'low':
                load_Poland_ru = 'низкая'
            elif load_Poland == 'medium':
                load_Poland_ru = 'средняя'
            elif load_Poland == 'high':
                load_Poland_ru = 'высокая'
            else:
                load_Poland_ru = load_Poland

            return capacity, capacity_Poland, load, load_Poland, capacity_ru, capacity_Poland_ru, load_ru, load_Poland_ru 
        except:
            capacity = 'N/A'
            capacity_Poland = 'N/A'
            load = 'N/A'
            load_Poland = 'N/A'
            capacity_ru = 'N/A'
            capacity_Poland_ru = 'N/A'
            load_ru = 'N/A'
            load_Poland_ru  = 'N/A'
            return capacity, capacity_Poland, load, load_Poland, capacity_ru, capacity_Poland_ru, load_ru, load_Poland_ru 

    def eu_North(self):
        """
        EU North (Stockholm)"""
        try:
            result = get_response()
            datacenters = result['datacenters']

            EU_North = datacenters['EU North']
            capacity = EU_North['capacity']
            load = EU_North['load']

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
            else:
                load_ru = load

            return capacity, load, capacity_ru, load_ru
        except:
            capacity = 'N/A'
            load = 'N/A'
            capacity_ru = 'N/A'
            load_ru = 'N/A'
            return capacity, load, capacity_ru, load_ru            

#
#    Asia   
#

    def india(self):
        '''
        India (Mumbai)
        India East (Chennai)'''
        try:
            result = get_response()
            datacenters = result['datacenters']

            India = datacenters['India']
            capacity = India['capacity']
            load = India['load']

            India_East = datacenters['India East']
            capacity_East = India_East['capacity']
            load_East = India_East['load']

            if capacity == 'full':
                capacity_ru = 'полная'
            elif capacity == 'offline':
                capacity_ru = 'офлайн'
            else:
                capacity_ru = capacity
                
            if capacity_East == 'full':
                capacity_East_ru = 'полная'
            elif capacity_East == 'offline':
                capacity_East_ru = 'офлайн'
            else:
                capacity_East_ru = capacity_East
                
            if load == 'idle':
                load_ru = 'никакая'
            elif load == 'low':
                load_ru = 'низкая'
            elif load == 'medium':
                load_ru = 'средняя'
            elif load == 'high':
                load_ru = 'высокая'
            else:
                load_ru = load

            if load_East == 'idle':
                load_East_ru = 'никакая'
            elif load_East == 'low':
                load_East_ru = 'низкая'
            elif load_East == 'medium':
                load_East_ru = 'средняя'
            elif load_East == 'high':
                load_East_ru = 'высокая'
            else:
                load_East_ru = load_East

            return capacity, capacity_East, load, load_East, load_ru, capacity_ru, load_East_ru, capacity_East_ru
        except:
            capacity = 'N/A'
            capacity_East = 'N/A'
            load = 'N/A'
            load_East = 'N/A'
            load_ru = 'N/A'
            capacity_ru = 'N/A'
            load_East_ru = 'N/A'
            capacity_East_ru = 'N/A'
            return capacity, capacity_East, load, load_East, load_ru, capacity_ru, load_East_ru, capacity_East_ru

    def japan(self):
        '''
        Japan (Tokyo)'''
        try:
            result = get_response()
            datacenters = result['datacenters']

            Japan = datacenters['Japan']
            capacity = Japan['capacity']
            load = Japan['load']
            
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
            else:
                load_ru = load

            return capacity, load, capacity_ru, load_ru
        except:
            capacity = 'N/A'
            load = 'N/A'
            capacity_ru = 'N/A'
            load_ru = 'N/A'
            return capacity, load, capacity_ru, load_ru

    def emirates(self):
        '''
        Emirates (Dubai)'''
        try:
            result = get_response()
            datacenters = result['datacenters']

            Emirates = datacenters['Emirates']
            capacity = Emirates['capacity']
            load = Emirates['load']
            
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
            else:
                load_ru = load

            return capacity, load, load_ru, capacity_ru
        except:
            capacity = 'N/A'
            load = 'N/A'
            capacity_ru = 'N/A'
            load_ru = 'N/A'
            return capacity, load, capacity_ru, load_ru

    def china(self):
        '''
        China Shanghai
        China Tianjin
        China Guangzhou'''
        try:
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

            if capacity_Shanghai == 'full':
                capacity_Shanghai_ru = 'полная'
            elif capacity_Shanghai == 'offline':
                capacity_Shanghai_ru = 'офлайн'
            else:
                capacity_Shanghai_ru = capacity_Shanghai        
                
            if capacity_Tianjin == 'full':
                capacity_Tianjin_ru = 'полная'
            elif capacity_Tianjin == 'offline':
                capacity_Tianjin_ru = 'офлайн'
            else:
                capacity_Tianjin_ru = capacity_Tianjin
                        
            if capacity_Guangzhou == 'full':
                capacity_Guangzhou_ru = 'полная'
            elif capacity_Guangzhou == 'offline':
                capacity_Guangzhou_ru = 'офлайн'
            else:
                capacity_Guangzhou_ru = capacity_Guangzhou
                
            if load_Shanghai == 'idle':
                load_Shanghai_ru = 'никакая'
            elif load_Shanghai == 'low':
                load_Shanghai_ru = 'низкая'
            elif load_Shanghai == 'medium':
                load_Shanghai_ru = 'средняя'
            elif load_Shanghai == 'high':
                load_Shanghai_ru = 'высокая'
            else:
                load_Shanghai_ru = load_Shanghai
                
            if load_Tianjin == 'idle':
                load_Tianjin_ru = 'никакая'
            elif load_Tianjin == 'low':
                load_Tianjin_ru = 'низкая'
            elif load_Tianjin == 'medium':
                load_Tianjin_ru = 'средняя'
            elif load_Tianjin == 'high':
                load_Tianjin_ru = 'высокая'
            else:
                load_Tianjin_ru = load_Tianjin
                
            if load_Guangzhou == 'idle':
                load_Guangzhou_ru = 'никакая'
            elif load_Guangzhou == 'low':
                load_Guangzhou_ru = 'низкая'
            elif load_Guangzhou == 'medium':
                load_Guangzhou_ru = 'средняя'
            elif load_Guangzhou == 'high':
                load_Guangzhou_ru = 'высокая'
            else:
                load_Guangzhou_ru = load_Guangzhou

            return capacity_Shanghai, capacity_Tianjin, capacity_Guangzhou, load_Shanghai, load_Tianjin, load_Guangzhou, load_Shanghai_ru, capacity_Shanghai_ru, load_Tianjin_ru, capacity_Tianjin_ru, load_Guangzhou_ru, capacity_Guangzhou_ru
        except:
            capacity_Shanghai = 'N/A'
            capacity_Tianjin = 'N/A'
            capacity_Guangzhou = 'N/A'
            load_Shanghai = 'N/A'
            load_Tianjin = 'N/A'
            load_Guangzhou = 'N/A'
            load_Shanghai_ru = 'N/A'
            capacity_Shanghai_ru = 'N/A'
            load_Tianjin_ru = 'N/A'
            capacity_Tianjin_ru = 'N/A'
            load_Guangzhou_ru = 'N/A'
            capacity_Guangzhou_ru = 'N/A'
            return capacity_Shanghai, capacity_Tianjin, capacity_Guangzhou, load_Shanghai, load_Tianjin, load_Guangzhou, load_Shanghai_ru, capacity_Shanghai_ru, load_Tianjin_ru, capacity_Tianjin_ru, load_Guangzhou_ru, capacity_Guangzhou_ru

    def singapore(self):
        '''
        Singapore'''
        try:
            result = get_response()
            datacenters = result['datacenters']

            Singapore = datacenters['Singapore']
            capacity = Singapore['capacity']
            load = Singapore['load']
            
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
            else:
                load_ru = load

            return capacity, load, load_ru, capacity_ru
        except:
            capacity = 'N/A'
            load = 'N/A'
            capacity_ru = 'N/A'
            load_ru = 'N/A'
            return capacity, load, capacity_ru, load_ru

    def hong_kong(self):
        '''
        Hong Kong'''
        try:
            result = get_response()
            datacenters = result['datacenters']

            Hong_Kong = datacenters['Hong Kong']
            capacity = Hong_Kong['capacity']
            load = Hong_Kong['load']
            
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
            else:
                load_ru = load

            return capacity, load, load_ru, capacity_ru
        except:
            capacity = 'N/A'
            load = 'N/A'
            capacity_ru = 'N/A'
            load_ru = 'N/A'
            return capacity, load, capacity_ru, load_ru
