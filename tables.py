#This script interact with tables anda capture its data
#Steps:
#1. Visit to https://the-internet.herokuapp.com/
#2. Enter to "Sortable Data Tables"
#3. There are 2 tables
#   Table #1 don't have significative information like as Class or ID
#   Table #2 have Class or ID attributes
#4. We going to work with Table 1

import unittest
from selenium import webdriver
from time import sleep

# TestCase that implements the test_sort_tables() method
class Tables(unittest.TestCase):

    # Setup: Call to webdriver; open page with .get() method and .click() in "Sortable Data Tables" option
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = "./chromedriver")
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/")
        driver.find_element_by_link_text("Sortable Data Tables").click()

    # Method 
    def test_sort_tables(self):
        driver = self.driver

        #Arrays where will be saved the table data
        # ¡¡¡Please Change the number 5 for a variable!!!
        table_data = [[] for i in range(5)]
        print(table_data)

        #Iterating on the table headers
        for i in range(5):
            header = driver.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{i + 1}]/span')
            table_data[i].append(header.text)

            #Iterating on the tabe rows
            for j in range(4):
              row_data = driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{j + 1}]/td[{j + 1}]')
              table_data[i].append(row_data.text)

        print(table_data)

    # Closing TestCase
    def tearDown(self):
      self.driver.close()

if __name__ == "__main__":
    unittest.main()