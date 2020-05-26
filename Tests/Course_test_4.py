'''
import unittest
import pytest
from selenium import webdriver
import time
from Pages.Login_page_4 import LoginPage
from Pages.Courses_page_4 import CoursePage
from selenium.webdriver.common.by import By
from Bases.Selenium_driver import Testing


class Testing(Testing):
#    @pytest.mark.smoke
    def test_Course_method_1(self):
        driver =self.driver
        driver.get("https://letskodeit.teachable.com/")
        lp=LoginPage(driver)
        cp=CoursePage(driver)
        cp=lp.login("a.manoj16@gmail.com","319319319")
        print ("Title of the webpage is:-",driver.title)
        time.sleep(4)
        cp.courses()
        time.sleep(5)

'''

