import sys, os
script_path = os.path.realpath(os.path.dirname(__name__))
os.chdir(script_path)
sys.path.append("..")

import unittest
from template_web_scraper.data_storage import DataStorage

class TestDataStorage(unittest.TestCase):
    def test_to_csv(self):
        # Add test cases here
        pass
