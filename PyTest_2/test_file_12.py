'''
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class LoginPage():
    def __init__(self,driver):
        # It is necessary to to initialise driver as page class member to implement Page Factory
        self.driver = driver

        #locaters
        self.__id="name"

    def method1(self):
        self.driver.find_element(By.ID, self.__id).send_keys("Manoj")

    def Login(self):
        self.method1()

class LoginTest(unittest.TestCase):
    #This test will going to be executed on chrome browser
    def test_Login(self):
        driver = webdriver.Chrome()
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.maximize_window()
        time.sleep(4)
        pglogin = LoginPage(driver)
        pglogin.Login()
        time.sleep(5)

if __name__ == "__main__":
     unittest.main()

'''







