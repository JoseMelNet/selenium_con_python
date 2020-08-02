#This Script is a SuiteTest with several TestCase
import unittest
from selenium import webdriver
from google_page import GooglePage

class GoogleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = r'C:\Users\melen\Dropbox\Python\Selenium_con_Python\chromedriver.exe')

    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('Platzi')

        self.assertEqual('Platzi', google.keyword)

    @classmethod
    def tearDown(cls):
        cls.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)