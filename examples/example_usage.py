import sys, os
script_path = os.path.realpath(os.path.dirname(__name__))
os.chdir(script_path)
sys.path.append("..")

from template_web_scraper.scraper import Scraper
from template_web_scraper.parser import Parser
from template_web_scraper.data_storage import DataStorage

# Create an instance of the Scraper class
scraper = Scraper("https://www.worldometers.info/coronavirus/")

# Get the HTML from the website
html = scraper.get_html()

# Create an instance of the Parser class
parser = Parser(html)

# Extract the data from the HTML
data = parser.get_data()

# Create an instance of the DataStorage class
data_storage = DataStorage(data, "example_output.csv")

# Save the data to a CSV file
data_storage.to_csv()
