from bs4 import BeautifulSoup

class Parser:
    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')

    def get_data(self):
        data = []
        table = self.soup.find("table", {"id": "main_table_countries_today"})
        rows = table.find_all("tr")
        for row in rows:
            cols = row.find_all("td")
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])
        return data
