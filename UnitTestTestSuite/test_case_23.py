#test_suite file
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Testing2(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("it will be printed before each method")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(6)

    def test_method_3(self):
        self.driver.get("https://learn.letskodeit.com")
        print ("Title of the page is:-",self.driver.title)

    @classmethod
    def tearDown(self):
        print("it will be printed after each method")
        self.driver.close()


if __name__ == "__main__":
    unittest.main()


