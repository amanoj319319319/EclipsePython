#working very fine with unit test setUp and tearDown methods
'''
import pytest
import unittest
from ddt import ddt, unpack, data
from selenium import  webdriver
import time
@ddt
class Test_Class_1(unittest.TestCase):
    def setUp(scope="module"):
        global driver
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://learn.letskodeit.com/p/practice")
        time.sleep(5)

    @data(("Ruby", "Cucumber"), ("Python", "Behave"))
    @unpack
    def test_1(self, switchname, hidename):
        switch = driver.find_element_by_id("name")
        switch.send_keys(switchname)
        time.sleep(3)
        switch.clear()

        hide = driver.find_element_by_id("displayed-text")
        hide.send_keys(hidename)
        time.sleep(3)
        hide.clear()

    def tearDown(scope="module"):
        driver.close()

if __name__ == "__main__":
    unittest.main()
'''


#working very fine with unit test setUpClass and tearDownClass methods
'''
import pytest
import unittest
from ddt import ddt, unpack, data
from selenium import  webdriver
import time

@ddt
class Testexample1(unittest.TestCase):

    def setUpClass(scope="module"):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.maximize_window()

    @data(("Ruby", "Cucumber"), ("Python", "Behave"))
    @unpack
    def test_1(self, switchname, hidename):
        switch = driver.find_element_by_id("name")
        switch.send_keys(switchname)
        time.sleep(3)
        switch.clear()

        hide = driver.find_element_by_id("displayed-text")
        hide.send_keys(hidename)
        time.sleep(3)
        hide.clear()


    def tearDownClass(scope="module"):
        driver.close()

if __name__ == "__main__":
    unittest.main()

'''







































