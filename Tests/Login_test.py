import unittest
from selenium import webdriver
import time
from Pages.Login_page import LoginPage
from selenium.webdriver.common.by import By


class Testing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ("it will be printed only once before all methods in a file")
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(6)

    def test_login_method_1(self):
        driver =self.driver
        driver.get("https://letskodeit.teachable.com/")
        lp=LoginPage(driver)
        lp.login("a.manoj16@gmail.com","319319319")
        print ("Title of the webpage is:-",self.driver.title)

    @classmethod
    def tearDownClass(cls):
        print ("it will be printed after each method")
        cls.driver.close()

if __name__ == "__main__":
    unittest.main()
