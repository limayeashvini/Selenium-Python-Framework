import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from conftest import driverInvoke


def test_sorting(driverInvoke):
    driver = driverInvoke
    OrList=[]
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    driver.maximize_window()
    driver.find_element(By.XPATH,"//th[@role='columnheader'][1]").click()
    OrListWE=driver.find_elements(By.XPATH,"//tr/td[1]")
    for i in OrListWE:
        OrList.append(i.text)

    OrList1=OrList.copy()

    OrList.sort()

    assert OrList==OrList1