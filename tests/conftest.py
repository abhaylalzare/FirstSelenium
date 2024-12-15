import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def setup_and_teardown():
    global driver
    driver = webdriver.Chrome(request)
    driver.get("https://www.confirmtkt.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()