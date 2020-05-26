from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from Pages.Courses_page import CoursePage
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

