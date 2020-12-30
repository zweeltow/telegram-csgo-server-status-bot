import requests
from bs4 import BeautifulSoup

url = 'https://steamdb.info/api/RenderAppHover/?appid=730'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}

class Peak24h:
    def get_peak24h(self):
        soup = BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')

        peak = soup.strong.string
        peak = peak.replace(',', '')

        return peak