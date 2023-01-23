from setuptools import setup, find_packages

setup(
    name="WebScraperAPI",
    version="1.0.0",
    author="Robbie Walmsley",
    author_email="robbiebusinessacc@gmail.com",
    description="A web scraping API that allows users to easily extract data from any website by simply providing the URL. The API utilizes advanced parsing and data storage techniques to ensure accurate and efficient data extraction. The package is easy to install and use, making it perfect for data scientists, researchers, and developers looking to quickly and easily access web data.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/robbiebusinessacc/web_scraper_api/",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "beautifulsoup4",
        "requests",
    ],
)
