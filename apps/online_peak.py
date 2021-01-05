import requests
from bs4 import BeautifulSoup

url = 'https://steamdb.info/app/730/graphs/'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}

class PeakOnline:
    def get_peak(self):
        soup = BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')

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
