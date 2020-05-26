'''
import unittest
import pytest
from selenium import webdriver
import time
from Pages.Login_page_3 import LoginPage
from Pages.Courses_page_3 import CoursePage
from selenium.webdriver.common.by import By
from Bases.conftest import *

@pytest.mark.usefixtures("setup")
class Testing:
#    @pytest.mark.smoke
    def test_Course_method_1(self,setup):
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
