#1st way
'''
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.mark.usefixtures("setup")
class TestExampleOne:
    def test_method_1(self):
        self.driver.get("https://learn.letskodeit.com")
        print ("Title of the page is:-",self.driver.title)


    def test_method_2(self):
        self.driver.get("https://learn.letskodeit.com/p/practice")
        print ("Title of the page is:-",self.driver.title)
        ele=self.driver.find_element_by_id("name").send_keys("Manoj")
        time.sleep(5)

'''


#2nd way
#C:\Users\Manoj\PycharmProjects\EclipseProject\PyTest_4_Conftest\test_exampleone.py(refer this)

'''
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
@pytest.mark.usefixtures("setup")
class TestExampleOne:
    @pytest.mark.parametrize("url", ["https://learn.letskodeit.com"])
    def test_method_1(self,url):
        self.driver.get(url)
        print ("Title of the page is:-",self.driver.title)
        

    def test_method_2(self):
        self.driver.get("https://learn.letskodeit.com/p/practice")
        print ("Title of the page is:-",self.driver.title)
        ele=self.driver.find_element_by_id("name").send_keys("Manoj")
        time.sleep(5)
'''

