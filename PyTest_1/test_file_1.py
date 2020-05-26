#if you write code like this , test_setUp works , but tear_down wont work
'''
import unittest
import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Test_Testing2():
    @pytest.fixture()
    def test_setUp(self):
        print("it will be printed before each method")
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(6)

    def test_method_1(self,test_setUp):
        driver.get("https://learn.letskodeit.com")
        print ("Title of the page is:-",driver.title)

    def test_method_2(self,test_setUp):
        driver.get("https://learn.letskodeit.com/p/practice")
        print ("Title of the page is:-",driver.title)
        ele=driver.find_element_by_id("name").send_keys("Manoj")
        time.sleep(5)

    @pytest.fixture()
    def test_tearDown(self):
        print("it will be printed after each method")
        driver.close()
'''

#if you write code like this , test_setUp works , but tear_down wont work
'''
import unittest
import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Test_Testing2():
    @pytest.fixture()
    def setUp(self):
        print("it will be printed before each method")
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(6)

    def test_method_1(self,setUp):
        driver.get("https://learn.letskodeit.com")
        print ("Title of the page is:-",driver.title)

    def test_method_2(self,setUp):
        driver.get("https://learn.letskodeit.com/p/practice")
        print ("Title of the page is:-",driver.title)
        ele=driver.find_element_by_id("name").send_keys("Manoj")
        time.sleep(5)

    @pytest.fixture()
    def tearDown(self):
        print("it will be printed after each method")
        driver.quit()

'''

#working fine
#setupteardown_method works before each method of a class and also after each method of a class
'''
import unittest
import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Test_Testing2():
    @pytest.yield_fixture()
    def setupteardown_method(self):
        print("it will be printed before each method")
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(6)
        yield
        print ("it will be printed after each method")
        driver.close()

    def test_method_1(self,setupteardown_method):
        driver.get("https://learn.letskodeit.com")
        print ("Title of the page is:-",driver.title)

    def test_method_2(self,setupteardown_method):
        driver.get("https://learn.letskodeit.com/p/practice")
        print ("Title of the page is:-",driver.title)
        ele=driver.find_element_by_id("name").send_keys("Manoj")
        time.sleep(5)
'''


#Good .. working fine
#how to execute setup and teardown methods for each method of a class
#always follow this one
'''
import unittest
import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Test_Testing2():
    @pytest.yield_fixture()
    def setup(self):
        print("it will be printed before each method of a class")
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(6)
        yield
        print ("it will be printed after each method of a class")
        driver.close()

    def test_method_1(self,setup):
        driver.get("https://learn.letskodeit.com")
        print ("Title of the page is:-",driver.title)

    def test_method_2(self,setup):
        driver.get("https://learn.letskodeit.com/p/practice")
        print ("Title of the page is:-",driver.title)
        ele=driver.find_element_by_id("name").send_keys("Manoj")
        time.sleep(5)
'''

#Good working fine
#how to execute setup and teardown methods only once before and after execution of a module
#always follow this one
'''
import unittest
import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Test_Testing2():
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

    def test_method_1(self,setup):
        driver.get("https://learn.letskodeit.com")
        print ("Title of the page is:-",driver.title)

    def test_method_2(self,setup):
        driver.get("https://learn.letskodeit.com/p/practice")
        print ("Title of the page is:-",driver.title)
        ele=driver.find_element_by_id("name").send_keys("Manoj")
        time.sleep(5)
'''

#working fine
#observer very carefully
#especially both setupteardown_class,setupteardown_method
'''
import unittest
import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Test_Testing2():
    @pytest.yield_fixture(scope="module")
    def setupteardown_class(self):
        print("it will be printed only once before execution of a module")
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(6)
        yield
        print ("i will be printed after only once after execution of a module")
        driver.close()

    @pytest.yield_fixture()
    def setupteardown_method(self):
        print ("it will be printed before each method of a class")
        yield
        print ("it will be printed after each method of a class")

    def test_method_1(self,setupteardown_class,setupteardown_method):
        driver.get("https://learn.letskodeit.com")
        print ("Title of the page is:-",driver.title)

    def test_method_2(self,setupteardown_class,setupteardown_method):
        driver.get("https://learn.letskodeit.com/p/practice")
        print ("Title of the page is:-",driver.title)
        ele=driver.find_element_by_id("name").send_keys("Manoj")
        time.sleep(5)

'''

#it is working fine
#i opened driver in setUp method and closed the driver in corresponding methods of a class
'''
import unittest
import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Test_Testing2():
    @pytest.yield_fixture()
    def setUp(self):
        print("it will be printed before each method")
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(6)

    def test_method_1(self,setUp):
        driver.get("https://learn.letskodeit.com")
        print ("Title of the page is:-",driver.title)
        driver.close()

    def test_method_2(self,setUp):
        driver.get("https://learn.letskodeit.com/p/practice")
        print ("Title of the page is:-",driver.title)
        ele=driver.find_element_by_id("name").send_keys("Manoj")
        time.sleep(5)
        driver.close()

'''

#working very fine
'''
import unittest
import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Test_Testing2():
    @pytest.yield_fixture(scope="class")#we can give scope either class or module 
    def setupteardown_class(self):
        print("it will be printed only once before execution of a module")
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(6)
        yield
        print ("i will be printed after only once after execution of a module")
        driver.close()

    @pytest.yield_fixture()
    def setupteardown_method(self):
        print ("it will be printed before each method of a class")
        yield
        print ("it will be printed after each method of a class")

    def test_method_1(self,setupteardown_class,setupteardown_method):
        driver.get("https://learn.letskodeit.com")
        print ("Title of the page is:-",driver.title)

    def test_method_2(self,setupteardown_class,setupteardown_method):
        driver.get("https://learn.letskodeit.com/p/practice")
        print ("Title of the page is:-",driver.title)
        ele=driver.find_element_by_id("name").send_keys("Manoj")
        time.sleep(5)

'''
