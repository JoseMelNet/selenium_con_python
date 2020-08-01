#This module can interact with buttons who make something on screen
import unittest
from selenium import webdriver
from time import sleep

# TestCase that implements the test_add_remove() method
class AddRemoveElements(unittest.TestCase):

    # Setup: Call to webdriver; open page with .get() method and .click() in "Add/Remove Elements" option
    def setUp(self):
      self.driver = webdriver.Chrome(executable_path='./chromedriver')
      driver = self.driver
      driver.get('https://the-internet.herokuapp.com/')
      driver.find_element_by_link_text('Add/Remove Elements').click()

    # Principal method: It can interact with differents buttons on screen
    def test_add_remove(self):
        driver = self.driver

        #Asign the number of elements to add and to remove
        elements_added = int(input('How many elements will you add?: '))
        elements_removed = int(input('How many elements will you remove?: '))
        total_elements = elements_added - elements_removed

        #Checking that the button "Add Element" is available
        add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')

        sleep(3)

        #Clicking (n) times on button "Add Element"
        for i in range(elements_added):
            add_button.click()

        #Clicking (n) times on button "Add Element"
        #Try-Except added in this case: elements_removed > elements_added
        for i in range(elements_removed):
            try:
                delete_button = driver.find_element_by_xpath('//*[@id="elements"]/button[1]')
                delete_button.click()
            except:
                print("You're trying to delete more elements that the existent")
                break
        
        #Aditional Information on screen
        if total_elements > 0: 
            print(f"There are {total_elements} elements on screen")
        else:
            print("There are 0 elements on screen")
        
        sleep(3)

    # Closing TestCase
    def tearDown(self):
      self.driver.close()

if __name__ == "__main__":
    unittest.main()