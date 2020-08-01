#This module interacts with dynamic controls
#Dynamic controls are elements that showed on screen in special conditions
#Dynamic controls can be avalaible or not in any time
#The program must validate if this controls are available and then do determined action
#Steps:
#1. Enter to https://the-internet.herokuapp.com/
#2. Select "Disappearing Elements" - This module simulate dynamic controls
#3. The Script must recharge the times necessary to show "Gallery" button
#4. Count the number of times the Script was recharge to "Gallery" button was available

import unittest
from selenium import webdriver
from time import sleep

# TestCase that implements the test_name_elements() method
class DynamicElement(unittest.TestCase):

    # Setup: Call to webdriver; open page with .get() method and .click() in "Disappearing Elements" option
    def setUp(self):
      self.driver = webdriver.Chrome(executable_path='./chromedriver')
      driver = self.driver
      driver.get("http://the-internet.herokuapp.com")
      driver.find_element_by_link_text("Disappearing Elements").click()

    # Principal method: It can recharge self until "Gallery button" will be available
    def test_name_elements(self):
        driver = self.driver

        #click in options buttons available
        options = []
        menu = 5 # Number of option buttons available. Gallery is included
        tries = 1

        #This "while-Cicle" runs until will there 5 options on screen
        while len(options) < 5:            
            options.clear() # Cleaning the list "options". Because "tries" can be greater "menu"
            
            #This "For-Cicle" runs between options menu on screen
            for i in range(menu):
                try:
                    options_name = driver.find_element_by_xpath(f'//*[@id="content"]/div/ul/li[{i+1}]/a')
                    options.append(options_name.text)
                    print(options)

                except:
                    print(f'Option number {i+1} is NOT FOUND')
                    tries += 1
                    driver.refresh() #This line runs if number options < 5
                
        print(f"Finished in {tries} tries")


    # Closing TestCase
    def tearDown(self):
      self.driver.close()

if __name__ == "__main__":
    unittest.main()
