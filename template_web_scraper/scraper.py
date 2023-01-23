import requests

class Scraper:
    def __init__(self, url):
        self.url = url

    def get_html(self):
        try:
            response = requests.get(f'http://localhost:5000/scrape?url={self.url}')
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(e)
            return None
