import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utilities.readProperties import ReadConfig


@pytest.fixture(scope="class")
def setUp(request):
    service_obj = Service("C:\\Users\\sumes\\Music\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    baseUrl = ReadConfig.getApplicationUrl()
    driver.get(baseUrl)
    driver.implicitly_wait(4)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
