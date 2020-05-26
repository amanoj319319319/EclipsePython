#1st way
'''
import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    print ("it will be executed only once before module execution")
    print("initiating chrome driver")
    driver = webdriver.Chrome()
#   driver.get("http://seleniumeasy.com/test")
    driver.maximize_window()
    driver.implicitly_wait(6)
    request.cls.driver = driver

    yield driver
    print ("it will be executed only once after module execution")
    driver.close()

#https://www.seleniumeasy.com/python/webdriver-tests-in-pytest-using-fixtures-and-conftest
'''

#2nd way
'''
import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def setup(request):
    print ("it will be executed only once before module execution")
    print("initiating chrome driver")
    driver = webdriver.Chrome()
#   driver.get("http://seleniumeasy.com/test")
    driver.maximize_window()
    driver.implicitly_wait(6)
    request.cls.driver = driver

    yield driver
    print ("it will be executed only once after module execution")
    driver.close()

'''

#3rd way
#need to verify
'''
import pytest
from selenium import webdriver
@pytest.yield_fixture(scope="module")
def OneTimeSetup(request,browser):
    if browser=="chrome":
        driver=webdriver.Chrome()
    elif browser=="firefox":
        driver=webdriver.Firefox()

    yield driver
    print ("it will be executed only once after module execution")
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return  request.config.getoption("--browser")
'''

import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    print ("it will be executed only once before module execution")
    print("initiating chrome driver")
    driver = webdriver.Chrome()
    driver.get("https://letskodeit.teachable.com/")
    driver.maximize_window()
    driver.implicitly_wait(6)
    request.cls.driver = driver

    yield driver
    print ("it will be executed only once after module execution")
    driver.close()
