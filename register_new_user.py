import unittest
from selenium import webdriver

class RegisterNewUser(unittest.TestCase):

# TesCase Initialization
    def setUp(self):
      self.driver = webdriver.Chrome(executable_path=r'C:\Users\melen\Dropbox\Python\Selenium_con_Python\chromedriver.exe')
      driver = self.driver
      driver.implicitly_wait(30)
      driver.maximize_window()
      driver.get('http://demo-store.seleniumacademy.com/')

# TestCase Methods
    def test_new_user(self):
      driver = self.driver
      driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a/span[2]').click()
      driver.find_element_by_link_text('Log In').click()

      #Method to acces a Create an account - button
      create_account_button = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[2]/form/div/div[1]/div[2]/a/span/span')
      self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
      create_account_button.click()

      # Confirmation access to correct page
      self.assertTrue('Create New Customer Account', driver.title)

      #Finding elements of Register Form
      first_name = driver.find_element_by_id('firstname')
      driver.implicitly_wait(1)
      middle_name = driver.find_element_by_id('middlename')
      driver.implicitly_wait(1)
      last_name = driver.find_element_by_id('lastname')
      driver.implicitly_wait(1)
      email_address = driver.find_element_by_id('email_address')
      driver.implicitly_wait(1)
      password = driver.find_element_by_id('password')
      driver.implicitly_wait(1)
      confirm_password = driver.find_element_by_id('confirmation')
      driver.implicitly_wait(1)
      newsletter_subscription = driver.find_element_by_id('is_subscribed')
      driver.implicitly_wait(1)
      submitt_buttton = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button/span/span')

      #Confirmation elements is enabled
      self.assertTrue(first_name.is_enabled()
      and middle_name.is_enabled()
      and last_name.is_enabled()
      and email_address.is_enabled()
      and password.is_enabled()
      and confirm_password.is_enabled()
      and newsletter_subscription.is_enabled()
      and submitt_buttton.is_enabled())

      #Sending data to fields in form
      first_name.send_keys('Test')
      middle_name.send_keys('Test')
      last_name.send_keys('Test')
      email_address.send_keys('Test')
      password.send_keys('Test')
      confirm_password.send_keys('Test@testing.mail.com')
      newsletter_subscription.click()
      submitt_buttton.click()

# TestCase Finalization

    def tearDown(self):
      self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity =2)

