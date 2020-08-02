#This is a page-object
#In this script there a object who execute the tests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Test Class created 
class GooglePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://google.com'
        self.search_locator = 'q'

    #Property defined 
    @property
    def is_loaded(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))
        return True
    
    @property
    def keyword(self):
        input_field = self.driver.find_element_by_name('q') # Identiy the search-bar
        return input_field.get_attribute('value')

    #The methods with which the page-object will work

    #Method to enter to url
    def open(self):
        self.driver.get(self.url)
    
    #Method who find terms
    def type_search(self, keyword):
        input_field = self.driver.find_element_by_name('q') # Identiy the search-bar
        input_field.send_keys(keyword)

    #Method who click on submit
    def click_submit(self):
        input_field = self.driver.find_element_by_name('q') # Identiy the search-bar
        input_field.submit()

    #Method search
    def search(self, keyword):
        self.type_search(keyword)
        self.click_submit




