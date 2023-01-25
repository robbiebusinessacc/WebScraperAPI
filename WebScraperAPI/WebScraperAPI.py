from WebScraperAPI.scraper import Scraper
from WebScraperAPI.parser import Parser
from WebScraperAPI.data_storage import DataStorage
class WebScraperAPI:
    def __init__(self, file_name='example_output.csv'):
        self.file_name = file_name

    def scrape_website(self, url):
        if not url:
            raise ValueError("Error: No URL provided. Please specify a URL to scrape.")

        # Scrape website
        scraper_obj = Scraper(url)
        data = scraper_obj.get_html()

        if data:
            # Parse the data
            parser_obj = Parser(data)
            parsed_data = parser_obj.parse_data()
            
            # Save the data
            data_storage_obj = DataStorage(parsed_data, self.file_name)
            data_storage_obj.save_data()
            
            return "Scraped data from {} and saved in file: {}".format(url, self.file_name)
        else:
            return "An error occurred while scraping the website"
