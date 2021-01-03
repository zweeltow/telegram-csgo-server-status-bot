import requests
from bs4 import BeautifulSoup

url = 'https://blog.counter-strike.net'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}

class Monthly:
    def get_unique(self):
        soup = BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')

        unique = soup.find("div", {"class": "monthly"}).string
        unique = unique.replace(',', '')

        return unique
