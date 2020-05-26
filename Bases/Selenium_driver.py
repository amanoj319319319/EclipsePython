'''
import unittest
from selenium import webdriver
import time
from Pages.Login_page import LoginPage
from selenium.webdriver.common.by import By
import HtmlTestRunner
import pytest_html

class Testing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ("it will be printed only once before all methods in a file")
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(6)

    @classmethod
    def tearDownClass(cls):
        print ("it will be printed after each method")
        cls.driver.close()

if __name__ == "__main__":
    unittest.main()

'''

import unittest
from selenium import webdriver
import time
from Pages.Login_page import LoginPage
from selenium.webdriver.common.by import By
import HtmlTestRunner
import pytest_html

class Testing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ("it will be printed only once before all methods in a file")
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(6)

    @classmethod
    def tearDownClass(cls):
        print ("it will be printed after each method")
        cls.driver.close()

if __name__ == "__main__":
    unittest.main()
