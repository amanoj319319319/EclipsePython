##https://www.tutorialspoint.com/pytest/pytest_tutorial.pdf
#https://www.guru99.com/pytest-tutorial.html

import unittest
import pytest
from selenium import webdriver
import time
import pytest_ordering
import pytest_html
from selenium.webdriver.common.by import By
import pytest_rerunfailures
import pytest_dependency
import pytest_depends
class Test_Testing2():
    a=10
    b=20
    @pytest.yield_fixture(scope="module")
    def setup(self):
        print("it will be printed only once before execution of a module")
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(6)
        yield
        print ("i will be printed after only once after execution of a module")
        driver.close()

#    @pytest.mark.skip("Dont want to excute this test in this batch")
#st     @pytest.mark.skipif(a<b , reason="a is less than b")
#    @pytest.mark.smoke
#    @pytest.mark.flasky(reruns=2)
    def test_method_1(self,setup):
        driver.get("https://learn.letskodeit.com")
        print ("Title of the page is:-",driver.title)


#    @pytest.mark.regression
#    @pytest.mark.flasky(reruns=3,reruns_delay=6)
#    @pytest.mark.depends(on=["test_method_1"])
#    @pytest.mark.dependency(depends=["test_method_1"])
 #   @pytest.mark.xfail
    def test_method_2(self,setup):
        driver.get("https://learn.letskodeit.com/p/practice")
        print ("Title of the page is:-",driver.title)
        ele=driver.find_element_by_id("name").send_keys("Manoj")
        time.sleep(5)

#https://pypi.org/project/pytest-depends/(for pytest dependencies)