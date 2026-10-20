import time

from selenium.webdriver.common.by import By

from pageObject.checkout_confirmation import checkout_confirmation

from utils.browserUtils import browserUtils


# Page object for the shop page (product list)
class shopPage(browserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # Locators
        self.clickShop=(By.CSS_SELECTOR, "a[href*='shop']")
        self.selectItem=(By.XPATH, "//div[@class='card h-100']")
        self.checkoutProcess=(By.XPATH, "//a[contains(text(),'Checkout')]")

    # Open the shop and click "Add" on the product named productName
    def shop(self,productName):
        self.driver.find_element(*self.clickShop).click()
        items = self.driver.find_elements(*self.selectItem)

        # Go through each product card and match it by its title
        for item in items:
            itemname = item.find_element(By.XPATH, "div/h4").text
            if itemname == productName:
                item.find_element(By.XPATH, "div/button").click()
                break
        time.sleep(2)

    # Click the Checkout link at the top and return the checkout page object
    def gotocart(self):
        self.driver.find_element(*self.checkoutProcess).click()
        return checkout_confirmation(self.driver)