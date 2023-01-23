import sys, os
script_path = os.path.realpath(os.path.dirname(__name__))
os.chdir(script_path)
sys.path.append("..")
import unittest
from template_web_scraper.utils import 

class TestUtils(unittest.TestCase):
    # Add test cases here
    pass
