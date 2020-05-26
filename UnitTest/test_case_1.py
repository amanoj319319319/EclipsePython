#We can write unitest cases in  terminal by using commond like this (python path of the file)
#python C:\Users\Manoj\PycharmProjects\EclipseProject\UnitTest\test_case_1.py
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


#Refer below urls if you have doubt
#https://www.youtube.com/watch?v=ePR9QrOIbhE
#https://www.youtube.com/watch?v=H9HUVSA_78U
'''
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def setUpModule():
    print ("setUpModule will be executed before class starts ....")

def tearDownModule():
    print ("tearDownModule will be executed after completing all the methods in a module ....")

class Testing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ("it will be printed only once before all methods in a file")
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(6)

    def test_method_1(self):
        self.driver.get("https://www.google.com")
        print ("Title of the webpage is:-",self.driver.title)

    def test_method_2(self):
        self.driver.get("https://learn.letskodeit.com/p/practice")
        element=self.driver.find_element_by_id("name").send_keys("Manoj")
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        print ("it will be printed after each method")
        cls.driver.close()

if __name__ == "__main__":
    unittest.main()
'''

#ASSERTIONS CONCEPTS .. PLEASE WATCH SDET CHANNEL TO GET CLEAR IDEA AND DO GOOGLE
'''
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Assertions(unittest.TestCase):
    def test_method1(self):
        a=1
        b=10
        self.assertEqual(a,b,"a is not equal to b")
        print ("please check assertEqual properly")

    def test_method2(self):
        a=True
        self.assertTrue(a,"a is not true")
        print ("please chck assertTrue properly")

    def test_method3(self):
        a=10
        b=20
        self.assertTrue((a+b)==30,"The result is false")
        print ("please chck assertTrue properly")


    def test_method4(self):
        a=10
        b=20
        self.assertFalse((a+b)==31,"The result should not be equal to expected result")
        print ("please chck assertTrue properly")

if __name__ == "__main__":
    unittest.main()
'''
