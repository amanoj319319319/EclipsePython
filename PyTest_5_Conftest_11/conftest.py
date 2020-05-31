#working very fine
#we can run our automated test cases against different browsers
import pytest
@pytest.fixture(params=["chrome", "firefox"],scope="class")
def driver_init(request):
    from selenium import webdriver
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    yield
    web_driver.close()

#https://dzone.com/articles/improve-your-selenium-webdriver-tests-with-pytest