import unittest
from selenium import webdriver
import time
from Pages.Login_page import LoginPage
from Pages.Courses_page import CoursePage
from selenium.webdriver.common.by import By


class Testing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ("it will be printed only once before all methods in a file")
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(6)

    def test_Course_method_1(self):
        driver =self.driver
        driver.get("https://letskodeit.teachable.com/")
        lp=LoginPage(driver)
        cp=CoursePage(driver)
        cp=lp.login("a.manoj16@gmail.com","319319319")
        print ("Title of the webpage is:-",self.driver.title)
        time.sleep(4)
        cp.courses()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        print ("it will be printed after each method")
        cls.driver.close()

if __name__ == "__main__":
    unittest.main()
