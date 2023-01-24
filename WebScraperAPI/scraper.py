import requests

class Scraper:
    def __init__(self, url):
        self.url = url

    def get_html(self):
        try:
            proxies = {
                'http': 'http://10.10.1.10:3128',
                'https': 'http://10.10.1.10:1080',
            }
            response = requests.get(self.url, proxies=proxies)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(e)
            return None
