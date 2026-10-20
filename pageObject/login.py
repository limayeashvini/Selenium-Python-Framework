from selenium.webdriver.common.by import By

from pageObject.shopPage import shopPage

from utils.browserUtils import browserUtils


# Page object for the login page
class loginPage(browserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

        # Locators
        self.username=(By.ID, "username")
        self.password=(By.NAME, "password")
        self.signInBtn=(By.ID, "signInBtn")



    # Enter the username and password, click Sign In and return the next page (shop)
    def login(self,username,password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.signInBtn).click()
        shop = shopPage(self.driver)
        return shop

