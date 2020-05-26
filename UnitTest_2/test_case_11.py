#How to skip test cases in unittest
'''
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Testing(unittest.TestCase):
    @classmethod
    def setUp(self):
        print ("it will be printed before each method")
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(6)

#    @unittest.skip("I can run this test case in the next batch...")
    def test_method_1(self):
        self.driver.get("https://www.google.com")
        print ("Title of the webpage is:-",self.driver.title)

    def test_method_2(self):
        self.driver.get("https://learn.letskodeit.com/p/practice")
        element=self.driver.find_element_by_id("name").send_keys("Manoj")
        time.sleep(5)
    @classmethod
    def tearDown(self):
        print ("it will be printed after each method")
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
'''

#HOW TO GENERATE HTML TEST REPORTS IN UNITTEST
#REFER BELOW URL
#C:\Users\Manoj\PycharmProjects\EclipseProject\UnitTest_2\test_case_11.py
#TO GENERATE HTML REPORTS YOU HAVE TO INSTALL htnl-testRunner module
#you should run following code in terminal , then only html reports can be generated
'''
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import HtmlTestRunner

class Testing(unittest.TestCase):
    @classmethod
    def setUp(self):
        print ("it will be printed before each method")
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(6)

#    @unittest.skip("I can run this test case in the next batch...")
    def test_method_1(self):
        self.driver.get("https://www.google.com")
        print ("Title of the webpage is:-",self.driver.title)

    def test_method_2(self):
        self.driver.get("https://learn.letskodeit.com/p/practice")
        element=self.driver.find_element_by_id("name").send_keys("Manoj")
        time.sleep(5)
    @classmethod
    def tearDown(self):
        print ("it will be printed after each method")
        self.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\Manoj\\PycharmProjects\\EclipseProject\\Unitest_Reports"))


'''


#https://www.youtube.com/watch?v=NBhzc3MsVWU (For test suite in unittest)

#How to skip test cases in unittest
'''
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Testing(unittest.TestCase):
    a=10
    b=20
    @classmethod
    def setUp(self):
        print ("it will be printed before each method")
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(6)

#    @unittest.skip("I can run this test case in the next batch...")
    @unittest.skipIf(a<b, "the value of a is less than b")
    def test_method_1(self):
        self.driver.get("https://www.google.com")
        print ("Title of the webpage is:-",self.driver.title)

    def test_method_2(self):
        self.driver.get("https://learn.letskodeit.com/p/practice")
        element=self.driver.find_element_by_id("name").send_keys("Manoj")
        time.sleep(5)
    @classmethod
    def tearDown(self):
        print ("it will be printed after each method")
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
'''

#How to skip test cases in unittest
'''
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Testing(unittest.TestCase):
    b=0
    @classmethod
    def setUp(self):
        print ("it will be printed before each method")
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(6)

#    @unittest.skip("I can run this test case in the next batch...")
    @unittest.skipUnless(b == 1, "skip test case based on the given condition")
    def test_method_1(self):
        self.driver.get("https://www.google.com")
        print ("Title of the webpage is:-",self.driver.title)

    def test_method_2(self):
        self.driver.get("https://learn.letskodeit.com/p/practice")
        element=self.driver.find_element_by_id("name").send_keys("Manoj")
        time.sleep(5)
    @classmethod
    def tearDown(self):
        print ("it will be printed after each method")
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
'''
#Refer this carefully
'''
1	unittest.skip(reason)

Unconditionally skip the decorated test. reason should describe why the test is being skipped.

2	unittest.skipIf(condition, reason)

Skip the decorated test if condition is true.

3	unittest.skipUnless(condition, reason)

Skip the decorated test unless condition is true.

4	unittest.expectedFailure()

Mark the test as an expected failure. If the test fails when run, the test is not counted as a failure.
'''

#https://www.tutorialspoint.com/unittest_framework/unittest_framework_skip_test.htm
'''
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Testing(unittest.TestCase):
    a=10
    b=20
    @classmethod
    def setUp(self):
        print ("it will be printed before each method")
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(6)

#    @unittest.skip("I can run this test case in the next batch...")
    @unittest.skipUnless(b == 1, "skip test case based on the given condition")
    def test_method_1(self):
        self.driver.get("https://www.google.com")
        print ("Title of the webpage is:-",self.driver.title)

    def test_method_2(self):
        self.driver.get("https://learn.letskodeit.com/p/practice")
        element=self.driver.find_element_by_id("name").send_keys("Manoj")
        time.sleep(5)
    
    @unittest.expectedFailure
    def test_mul(self):
        """mul"""
        result = self.a * self.b
        self.assertEqual(result == 0)

    @classmethod
    def tearDown(self):
        print ("it will be printed after each method")
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
'''

#test_suite file
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class Testing1(unittest.TestCase):
    a = 10
    b = 20

    @classmethod
    def setUp(self):
        print("it will be printed before each method")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(6)

#    @unittest.skip("I can run this test case in the next batch...")
#    @unittest.skipUnless(b == 1, "skip test case based on the given condition")
    def test_method_1(self):
        self.driver.get("https://www.google.com")
        print("Title of the webpage is:-", self.driver.title)

    def test_method_2(self):
        self.driver.get("https://learn.letskodeit.com/p/practice")
        element = self.driver.find_element_by_id("name").send_keys("Manoj")
        time.sleep(5)

    @classmethod
    def tearDown(self):
        print("it will be printed after each method")
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

