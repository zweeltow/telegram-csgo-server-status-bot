import requests
import json
from bs4 import BeautifulSoup
from apps import file_manager

import config

url_st = 'https://store.steampowered.com/stats/'
url_cs = 'https://blog.counter-strike.net'
url_ss = 'https://crowbar.steamstat.us/gravity.json'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}


class PeakOnline:
    def get_peak(self):
        try:
            soup = BeautifulSoup(requests.get(url_st, headers=headers).content, 'html.parser')

            string = soup.find(string="Counter-Strike: Global Offensive")
            tr = string.find_parent("tr")
            span = tr.find_all("span")
            peak24 = str(span[1])
            peak24 = peak24.replace('<span class="currentServers">', '')
            peak24 = peak24.replace('</span>', '')
            peak24 = peak24.replace(',', '')
            peak24 = int(peak24)
            return peak24
        except:
            peak24 = 'N/A'
            return peak24


class Monthly:
    def get_unique(self):
        try:
            soup = BeautifulSoup(requests.get(url_cs, headers=headers).content, 'html.parser')

            unique = soup.find("div", {"class": "monthly"}).string
            unique = unique.replace(',', '')
            unique = int(unique)
            return unique
        except:
            unique = 'N/A'
            return unique
        
class CSGOGameCoordinator:
    def get_status(self):
        try:
            soup = BeautifulSoup(requests.get(url_ss, headers=headers).content, 'html.parser')

            data = soup.get_text()

            f = open(config.SS_CACHE_FILE_PATH, 'r+')
            f.truncate(0)
            f.close()

            f = open(config.SS_CACHE_FILE_PATH, 'a')
            f.write(data)
            f.close()
            
            fin = open(config.SS_CACHE_FILE_PATH,"r")  
            parsed = json.load(fin)
            fin.close()
            line = json.dumps(parsed, indent=4)
            fout = open(config.SS_CACHE_FILE_PATH,"w")
            fout.write(line)
            fout.close()
            
            items = file_manager.readJson(config.SS_CACHE_FILE_PATH)
            delta = items['services'][4]
            gc_status = delta[2]

            return gc_status
        except:
            gc_status = 'N/A'
            return gc_status
