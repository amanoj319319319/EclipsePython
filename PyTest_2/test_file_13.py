from selenium import webdriver
import time
import unittest
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By

class LoginPage():
    def __init__(self,driver):
        self.driver=driver

        # Locators
        self._login_link = "Login"
        self._email_field = "user_email"
        self._password_field = "user_password"
        self._login_button = "commit"

    def click_on_login_link(self):
        self.driver.find_element(By.LINK_TEXT, self._login_link).click()
    def enter_username(self,username):
        self.driver.find_element(By.ID, self._email_field).clear()
        time.sleep(2)
        self.driver.find_element(By.ID, self._email_field).send_keys(username)
    def enter_password(self,password):
        self.driver.find_element(By.ID, self._password_field).clear()
        time.sleep(2)
        self.driver.find_element(By.ID, self._password_field).send_keys(password)
    def click_on_login_button(self):
        self.driver.find_element(By.NAME, self._login_button).click()

    def login(self,username,password):
        self.click_on_login_link()
        self.enter_username(username)
        self.enter_password(password)
        self.click_on_login_button()
        time.sleep(3)
        return CoursePage(self.driver)


class CoursePage():
    def __init__(self,driver):
        self.driver=driver

        # Locators
        self._javacourse = "/html/body/div[1]/div/div/div[2]/div[4]/div/div[1]/a/div/div[2]"

    def enter_course_name(self):
        course=self.driver.find_element(By.XPATH, self._javacourse).click()


    def courses(self):
        self.enter_course_name()


class LoginTest(unittest.TestCase):
    #This test will going to be executed on chrome browser
    def test_Login(self):
        driver = webdriver.Chrome()
        driver.get("https://learn.letskodeit.com")
        driver.maximize_window()
        driver.implicitly_wait(8)
        lp = LoginPage(driver)
        cc = CoursePage(driver)
        cc=lp.login("a.manoj16@gmail.com","319319319")
        cc.courses()
        time.sleep(5)

if __name__ == "__main__":
     unittest.main()
