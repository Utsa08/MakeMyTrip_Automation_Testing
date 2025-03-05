import pytest
from selenium import webdriver

#browser invocation
@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    # implicit timing
    driver.implicitly_wait(10)
    driver.get(
        "https://www.makemytrip.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
