#working very fine ... follow this always
'''
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from DataDrivenTesting_2 import XL_utilities

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(8)
driver.get("http://www.newtours.demoaut.com/")
#time.sleep(5)
#driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[4]/div[6]/div/button").click()

path="C:\\Users\\Manoj\\Desktop\\hello.xlsx"

rows=XL_utilities.getRowcount(path,"Sheet1")

for r in range(2,rows+1):
    username=XL_utilities.readData(path,"Sheet1",r,1)
    password=XL_utilities.readData(path,"Sheet1",r,2)

    driver.find_element(By.NAME, "userName").clear()
    driver.find_element(By.NAME, "userName").send_keys(username)

    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys(password)

    driver.find_element_by_name("login").click()
    time.sleep(6)
    print ("Title is:-",driver.title)
    if driver.title=="Find a Flight: Mercury Tours:":
       print ("test is passed")
       XL_utilities.writeData(path, "Sheet1", r, 3, "test_passed")
       driver.back()
    else:
       print ("test is failed")
       XL_utilities.writeData(path, "Sheet1", r, 3, "test_failed")
    driver.find_element_by_link_text("Home").click()
    time.sleep(6)

'''





