from bs4 import BeautifulSoup

class Parser:
    def __init__(self, data):
        self.data = data
        self.soup = BeautifulSoup(self.data, 'html.parser')

    def parse_data(self):
        parsed_data = []
        tables = self.soup.find_all("table")
        for table in tables:
            rows = table.find_all("tr")
            for row in rows:
                cols = row.find_all("td")
                cols = [ele.text.strip() for ele in cols]
                parsed_data.append([ele for ele in cols if ele])
        return parsed_data
