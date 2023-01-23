from flask import Flask, request
from template_web_scraper.scraper import scrape
from template_web_scraper.parser import parse
from template_web_scraper.data_storage import save

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape_website():
    url = request.args.get('url')
    if not url:
        return "Error: No URL provided. Please specify a URL to scrape."

    # Scrape website
    data = scrape(url)
    
    # parse the data
    parsed_data = parse(data)
    
    # save the data
    save(parsed_data)
    
    return "Scraped data from {}".format(url)

if __name__ == '__main__':
    app.run(debug=True)
