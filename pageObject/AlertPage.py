from pageObject.locators import AllLocators

class AlertPage:

    def __init__(self,driver):
        self.driver = driver
        self.locator = AllLocators

    def getCross(self):
        self.driver.find_element(*self.locator.cross).click()