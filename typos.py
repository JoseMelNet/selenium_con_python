# This script validates that the text on the website is equal to an expected text
# Steps:
#1. Enter to https://the-internet.herokuapp.com/
#2. Select "Typos" - This module simulate can change a line text when we recharge the website
#3. Find the text with typo

import unittest
from selenium import webdriver

# TestCase that implements the test_find_typo() method
class Typos(unittest.TestCase):

    # Setup: Call to webdriver; open page with .get() method and .click() in "Typos" option
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        driver.find_element_by_link_text("Typos").click()

# TestCase that implements the test_find_typo() method
    def test_dynamic_controls(self):
        driver = self.driver

        # Find the text that we want to check
        paragraph_to_check = driver.find_element_by_css_selector("#content > div > p:nth-child(3)")
        text_to_check = paragraph_to_check.text


        # Counting number of tries neccesary to find the correct text
        tries = 1
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won't."
        print(f'Correct text:   {correct_text}')
        print(f'Trie # {tries}: {text_to_check}')

        while text_to_check != correct_text:
            driver.refresh()
            paragraph_to_check = driver.find_element_by_css_selector("#content > div > p:nth-child(3)")
            text_to_check = paragraph_to_check.text
            tries += 1
            print(f'Trie # {tries}: {text_to_check}')

        # Aditional check to validate if the correct text was founded
        while not found:
            if text_to_check == correct_text:
              driver.refresh()
              found = True

        self.assertEqual(found, True)

        print(f'It took {tries} tries to find the typo')

    # Closing TestCase
    def tearDown(self):
      self.driver.close()


if __name__ == "__main__":
    unittest.main()