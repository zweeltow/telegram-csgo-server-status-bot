import requests
import json
from bs4 import BeautifulSoup
from apps import file_manager

import config

url_db = 'https://steamdb.info/app/730/graphs/'
url_cs = 'https://blog.counter-strike.net'
url_ss = 'https://crowbar.steamstat.us/gravity.json'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}


class PeakOnline:
    def get_peak(self):
        soup = BeautifulSoup(requests.get(url_db, headers=headers).content, 'html.parser')

        peak = soup.find_all("strong")

        peak24 = str(peak[1])
        peak_all = str(peak[2])

        peak24 = peak24.replace('<strong>', '')
        peak24 = peak24.replace('</strong>', '')
        peak24 = peak24.replace(',', '')

        peak_all = peak_all.replace('<strong>', '')
        peak_all = peak_all.replace('</strong>', '')
        peak_all = peak_all.replace(',', '')

        return peak24, peak_all


class Monthly:
    def get_unique(self):
        soup = BeautifulSoup(requests.get(url_cs, headers=headers).content, 'html.parser')

        unique = soup.find("div", {"class": "monthly"}).string
        unique = unique.replace(',', '')

        return unique
        
class CSGOGameCoordinator:
    def get_status(self):
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
        delta1 = items['services'][4]
        delta2 = items['services'][61]
        gc_status = delta1[2]
        webapi_status = delta2[2]

        return gc_status, webapi_status
