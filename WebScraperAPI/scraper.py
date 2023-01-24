import requests

class Scraper:
    def __init__(self, url):
        self.url = url
        self.proxy = 'http://proxy_address:proxy_port'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

    def get_html(self):
        try:
            response = requests.get(self.url, proxies={'http': self.proxy, 'https': self.proxy}, headers=self.headers)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(e)
            return None
