import sys, os
script_path = os.path.realpath(os.path.dirname(__name__))
os.chdir(script_path)
sys.path.append("..")

import unittest
from template_web_scraper.scraper import Scraper

class TestScraper(unittest.TestCase):
    def test_get_html(self):
        # Add test cases here
        pass
