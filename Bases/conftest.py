import unittest
import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    print ("it will be executed only once before module execution")
    print("initiating chrome driver")
    driver = webdriver.Chrome()
    driver.get("https://letskodeit.teachable.com/")
    driver.maximize_window()
    driver.implicitly_wait(6)
    request.cls.driver = driver

    yield driver
    print ("it will be executed only once after module execution")
    driver.close()






#The below code doesntwork in base class
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

