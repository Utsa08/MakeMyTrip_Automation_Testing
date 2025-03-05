from selenium.webdriver.common.by import By


class AllLocators:
    #AlertPage
    cross = (By.XPATH, "(//span[@class='commonModal__close'])[1]")

    #HomePage
    flight = (By.CSS_SELECTOR, "a[class='headerIcons makeFlex hrtlCenter column active']")
    city1 = (By.XPATH, "//label[@for='fromCity']")
    city1Input = (By.XPATH, "//input[@placeholder='From']")
    locationDropDown1 = (By.XPATH, "(//p[@class='font12 greyText appendBottom3'])[1]")
    city2 = (By.CSS_SELECTOR, "label[for='toCity']")
    city2Input = (By.XPATH, "//input[@placeholder='To']")
    locationDropDown2 = (By.XPATH, "(//p[contains(@class,'searchedResult font14 blackText appendBottom5')])[1]")
    date = (By.XPATH, "(//div[@class='DayPicker-Day'])[1]")
    search = (By.XPATH, "(//a[normalize-space()='Search'])[1]")
