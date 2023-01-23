from flask import Flask, request
from WebScraperAPI.scraper import Scraper
from WebScraperAPI.parser import Parser
from WebScraperAPI.data_storage import DataStorage

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape_website():
    url = request.args.get('url')
    if not url:
        return "Error: No URL provided. Please specify a URL to scrape."

    # Scrape website
    scraper_obj = Scraper(url)
    data = scraper_obj.get_html()

    if data:
        # Parse the data
        parser_obj = Parser(data)
        parsed_data = parser_obj.parse_data()
        
        # Save the data
        file_name = 'example_output.csv'
        data_storage_obj = DataStorage(parsed_data, file_name)
        data_storage_obj.save_data()
        
        return "Scraped data from {}".format(url)
    else:
        return "An error occurred while scraping the website"

if __name__ == '__main__':
    app.run(debug=True)
