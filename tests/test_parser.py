import sys, os
script_path = os.path.realpath(os.path.dirname(__name__))
os.chdir(script_path)
sys.path.append("..")


import unittest
from template_web_scraper.parser import Parser

class TestParser(unittest.TestCase):
    def test_get_data(self):
        # Add test cases here
        pass
