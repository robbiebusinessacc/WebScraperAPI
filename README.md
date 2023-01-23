# WebScraperAPI

A web scraping API that allows users to easily extract data from any website by simply providing the URL. The API utilizes advanced parsing and data storage techniques to ensure accurate and efficient data extraction. The package is easy to install and use, making it perfect for data scientists, researchers, and developers looking to quickly and easily access web data.

## Installation

To install the package, use pip:

`pip install WebScraperAPI`

## Usage

You can use the package by importing it in your code and using the `scrape` function.

```python
from WebScraperAPI.scraper import Scraper
from WebScraperAPI.parser import Parser
from WebScraperAPI.data_storage import DataStorage

url = 'https://example.com'

# Scrape the data from the website
scraper_obj = Scraper(url)
data = scraper_obj.get_html()

if data:
    # Parse the data
    parser_obj = Parser(data)
    parsed_data = parser_obj.parse_data()

    # Save the data to a CSV file
    file_name = 'example_output.csv'
    data_storage_obj = DataStorage(parsed_data, file_name)
    data_storage_obj.save_data()
else:
    print("An error occurred while scraping the website")
```

## Dependencies
```
beautifulsoup4
requests
```
## Contributing
If you want to contribute to this project, please fork the repository and make a pull request.

## License
This project is licensed under the MIT License.


