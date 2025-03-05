import time

from pageObject.AlertPage import AlertPage
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestMain(BaseClass):


    def test_main(self):
        log = self.get_logger()

        #AlertPage
        alertPage = AlertPage(self.driver)
        alertPage.getCross()
        log.info("Crossed the Alert")

        #HomePage
        homePage = HomePage(self.driver)
        homePage.getFlight()
        homePage.getCity1()
        homePage.getLocationDropDown1()
        log.info("Choosing First Location")
        homePage.getCity2()
        homePage.getLocationDropDown2()
        log.info("Choosing Destination")
        time.sleep(5)
        homePage.getDate()
        time.sleep(5)
        homePage.getSearch()
        log.info("Searching Flights")
