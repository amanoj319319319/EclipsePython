'''
import unittest
import pytest
from selenium import webdriver
import time
from Pages.Login_page_5 import LoginPage
from selenium.webdriver.common.by import By
from Bases.conftest import *

@pytest.mark.usefixtures("setup")
class Testing:
    def test_login_method_1(self):
        driver =self.driver
        driver.get("https://letskodeit.teachable.com/")
        lp=LoginPage(driver)
        lp.login("a.manoj16@gmail.com","319319319")
        print ("Title of the webpage is:-",self.driver.title)

'''

