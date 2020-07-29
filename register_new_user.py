import unittest
from selenium import webdriver

class RegisterNewUser(unittest.TestCase):

# TesCase Initialization
    def setUp(self):
      self.driver = webdriver.Chrome(executable_path=r'C:\Users\melen\Dropbox\Python\Selenium_con_Python\chromedriver.exe')
      driver = self.driver
      driver.implicitly_wait(30)
      driver.maximize_window()
      driver.get('htpp://demo-store.seleniumacademy.com')

# TestCase Methods
    def test_new_user(self):
      driver = self.driver
      

# TestCase Finalization

    def tearDown(self):
      self.driver.quit()

if __name__ == "__main__":
    unittest.man(verbosity =2)

