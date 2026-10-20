from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.browserUtils import browserUtils


class checkout_confirmation(browserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.checkoutbtn=(By.CSS_SELECTOR, "button.btn-success")
        self.countryName=(By.ID, "country")
        self.enter_country=(By.LINK_TEXT, "India")
        self.select_country=(By.CSS_SELECTOR, "label[for='checkbox2']")
        self.chkboxSelection=(By.ID, "checkbox2")
        self.clickPurchase=(By.XPATH, "//input[@value='Purchase']")
        self.message=(By.XPATH, "//div[contains(@class,'alert')]")

    def checkout(self):
        self.driver.find_element(*self.checkoutbtn).click()

    def enter_delivery_address(self,country):
        self.driver.find_element(*self.countryName).send_keys(country)

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((self.enter_country))).click()

        # changed: click the visible label (the real input is hidden), then verify
        self.driver.find_element(*self.select_country).click()
        assert self.driver.find_element(*self.chkboxSelection).is_selected()
        self.driver.find_element(*self.clickPurchase).click()

    def validate_delivery(self):
        msg = self.driver.find_element(*self.message).text
        assert "Success" in msg