import time

from selenium.webdriver.common.by import By

from pageObject.checkout_confirmation import checkout_confirmation

from utils.browserUtils import browserUtils


class shopPage(browserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.clickShop=(By.CSS_SELECTOR, "a[href*='shop']")
        self.selectItem=(By.XPATH, "//div[@class='card h-100']")
        self.checkoutProcess=(By.XPATH, "//a[contains(text(),'Checkout')]")

    def shop(self,productName):
        self.driver.find_element(*self.clickShop).click()
        items = self.driver.find_elements(*self.selectItem)

        for item in items:
            itemname = item.find_element(By.XPATH, "div/h4").text
            if itemname == productName:
                item.find_element(By.XPATH, "div/button").click()
                break
        time.sleep(2)

    def gotocart(self):
        self.driver.find_element(*self.checkoutProcess).click()
        return checkout_confirmation(self.driver)