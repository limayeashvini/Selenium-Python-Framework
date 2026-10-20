import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from conftest import driverInvoke


# Checks that clicking the first column header sorts the vegetable names alphabetically
def test_sorting(driverInvoke):
    driver = driverInvoke
    OrList=[]
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    driver.maximize_window()
    # Click the first column header to sort the table
    driver.find_element(By.XPATH,"//th[@role='columnheader'][1]").click()
    # Read the names from the first column, in the order the browser shows them
    OrListWE=driver.find_elements(By.XPATH,"//tr/td[1]")
    for i in OrListWE:
        OrList.append(i.text)

    # Keep a copy of the browser's order, then sort the original in Python
    OrList1=OrList.copy()

    OrList.sort()

    # If the browser sorted the table correctly, both lists are the same
    assert OrList==OrList1