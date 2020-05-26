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

