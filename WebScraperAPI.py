from flask import Flask, request
from WebScraperAPI.scraper import Scraper
from WebScraperAPI.parser import Parser
from WebScraperAPI.data_storage import DataStorage
from selenium import webdriver

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape_website():
    url = request.args.get('url')
    if not url:
        return "Error: No URL provided. Please specify a URL to scrape."
    
    # Start a headless browser
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('start-maximized')
    options.add_argument('disable-infobars')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--remote-debugging-port=9222')
    browser = webdriver.Chrome(chrome_options=options)

    # Scrape website using Selenium
    browser.get(url)
    data = browser.page_source

    # Close the browser
    browser.close()

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
