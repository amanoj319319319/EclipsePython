#ONE WAY .. WITH USING CSV FILE DATA
'''
import pytest
import unittest
from ddt import ddt, unpack, data
from selenium import  webdriver
import time
from DataDrivenTesting.switchreaddata import getCSVData
@ddt
class Testexample1(unittest.TestCase):

    def setUpClass(scope="module"):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.maximize_window()

#    @data(("Ruby", "Cucumber"), ("Python", "Behave"))
    @data(*getCSVData("C:\\Users\\Manoj\\PycharmProjects\\EclipseProject\\DataDrivenTesting\\switchvalues.csv"))
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

#SECOND WAY .. WITH OUT USING CSV FILE .. IT MEANNS USING DATA PROVIDER @data

import pytest
import unittest
from ddt import ddt, unpack, data
from selenium import  webdriver
import time
from DataDrivenTesting.switchreaddata import getCSVData
@ddt
class Testexample1(unittest.TestCase):

    def setUpClass(scope="module"):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.maximize_window()

    @data(("Ruby", "Cucumber"), ("Python", "Behave"))
#    @data(*getCSVData("C:\\Users\\Manoj\\PycharmProjects\\EclipseProject\\DataDrivenTesting\\switchvalues.csv"))
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

