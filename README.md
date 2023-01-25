# WebScraperAPI

A web scraping API that allows users to easily extract data from any website by simply providing the URL. The API utilizes advanced parsing and data storage techniques to ensure accurate and efficient data extraction. The package is easy to install and use, making it perfect for data scientists, researchers, and developers looking to quickly and easily access web data.

## Installation

To install the package, use pip:

`pip install WebScraperAPI`

## Usage

You can use the package by importing it in your code and using the `scrape` function.

```python

from WebScraperAPI.WebScraperAPI import WebScraperAPI

# Create an instance of the class
scraper = WebScraperAPI(file_name='COVID.csv')

# URL
url = 'https://www.worldometers.info/coronavirus/'

# Call the scrape_website method
result = scraper.scrape_website(url)
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


