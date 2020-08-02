# This script works with dynamic controls
# The functionality of dynamic controls can vary when we interact with them
# And we must wait while these controls change or become available again
# Steps:
#1. Enter to https://the-internet.herokuapp.com/
#2. Select "Dynamic Controls" - This module simulate dynamic controls
#3. In this apart there are a "check-box", two buttons, and a text-area
#4. The check-box is available. If we click on "remove.button" we must wait until check.box disappear
#5. Then we can click on "Add-Button" and repeat the process
#6. In second part we can the same process with "Text-Area". Enabling buttons and waiting 

import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# TestCase that implements the test_name_elements() method
class DynamicControls(unittest.TestCase):

    # Setup: Call to webdriver; open page with .get() method and .click() in "Disappearing Elements" option
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        driver.find_element_by_link_text("Dynamic Controls").click()

# TestCase that implements the test_dynamic_controls() method
    def test_dynamic_controls(self):
        driver = self.driver

        #Apart 1: Checkbox Button
        # Identify the elements with we go to interact
        # Identify checkbox-button
        checkbox = driver.find_element_by_css_selector("#checkbox > input[type=checkbox]")
        checkbox.click()

        # Identify Remove&Add-Button
        remover_add_button = driver.find_element_by_css_selector("#checkbox-example > button")
        remover_add_button.click()

        # Waiting until Add-Button is available
        WebDriverWait(driver, 15).until(
          EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#checkbox-example > button")
            )
            )
        remover_add_button.click()

        #Apart 2: TextArea.Button
        # Identify the elements with we go to interact
        #Identify Enable&Disable-Button 
        enable_disabled_button = driver.find_element_by_css_selector("#input-example > button")
        enable_disabled_button.click()

        # Waiting until Text-Area is available
        WebDriverWait(driver, 15).until(
          EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#input-example > button")
            )
            )

        # Identify Text-Area
        text_area = driver.find_element_by_css_selector("#input-example > input[type=text]")
        # Sending text to Text-Area
        text_area.send_keys('Platzi')

        # Click on Disable-Button
        enable_disabled_button.click()

    # Closing TestCase
    def tearDown(self):
      self.driver.close()


if __name__ == "__main__":
    unittest.main()