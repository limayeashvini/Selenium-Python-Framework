import json
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pageObject.login import loginPage
from pageObject.shopPage import shopPage
from pageObject.checkout_confirmation import checkout_confirmation
from utils.browserUtils import browserUtils

class TestFramework:
    with open("./data/test_e2e_framework.json","r") as f:
        test_data = json.load(f)
        test_list = test_data["data"]

    @pytest.mark.smoke
    @pytest.mark.parametrize("item",test_list)
    def test_e2e(self, driverInvoke, item):
        driver = driverInvoke
        self.driver = driver
        driver.get("https://rahulshettyacademy.com/loginpagePractise/")
        driver.maximize_window()

        loginin = loginPage(driver)
        print(loginin.getTitile())
        shop=loginin.login(item["userEmail"],item["userPassword"])

        shop.shop(item["productName"])
        print(shop.getTitile())
        checkout_confirm=shop.gotocart()

        checkout_confirm.checkout()
        print(checkout_confirm.getTitile())
        checkout_confirm.enter_delivery_address("Ind")
        checkout_confirm.validate_delivery()

