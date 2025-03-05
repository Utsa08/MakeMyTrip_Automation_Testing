import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageObject.locators import AllLocators

class HomePage:

    def __init__(self,driver):
        self.driver = driver
        self.locator = AllLocators

    def getFlight(self):
        self.driver.find_element(*self.locator.flight).click()

    def getCity1(self):
        self.driver.find_element(*self.locator.city1).click()
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.visibility_of_element_located(self.locator.city1Input))
        self.driver.find_element(*self.locator.city1Input).send_keys("Kol")

    def getLocationDropDown1(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.visibility_of_element_located(self.locator.locationDropDown1))
        self.driver.find_element(*self.locator.locationDropDown1).click()

    def getCity2(self):
        self.driver.find_element(*self.locator.city2).click()
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.visibility_of_element_located(self.locator.city2Input))
        self.driver.find_element(*self.locator.city2Input).send_keys("Pun")

    def getLocationDropDown2(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.visibility_of_element_located(self.locator.locationDropDown2))
        self.driver.find_element(*self.locator.locationDropDown2).click()

    def getDate(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.visibility_of_element_located(self.locator.date))
        self.driver.find_element(*self.locator.date).click()

    def getSearch(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.visibility_of_element_located(self.locator.search))
        self.driver.find_element(*self.locator.search).click()
        time.sleep(15)
