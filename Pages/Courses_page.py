from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class CoursePage():
    def __init__(self,driver):
        self.driver=driver

        # Locators
        self._javacourse = "/html/body/div[1]/div/div/div[2]/div[4]/div/div[1]/a/div/div[2]"

    def enter_course_name(self):
        course=self.driver.find_element(By.XPATH, self._javacourse).click()


    def courses(self):
        self.enter_course_name()


