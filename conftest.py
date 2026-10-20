import base64
import os
import re

import pytest
from pytest_html import extras as html_extras
from selenium import webdriver
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption("--browserName",default='chrome', action="store")


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not config.getoption("htmlpath"):
        config.option.htmlpath = os.path.join(os.path.dirname(__file__), "reports", "report.html")
        config.option.self_contained_html = True

@pytest.fixture(scope="function")
def driverInvoke(request):
    browserName=request.config.getoption("--browserName")
    if browserName=="firefox":
        driver=webdriver.Firefox()
        driver.implicitly_wait(2)

    elif browserName=="chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        })
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(2)

    yield driver
    driver.close()


def _capture_screenshot(driver, nodeid):
    reports_dir = os.path.join(os.path.dirname(__file__), "reports")
    os.makedirs(reports_dir, exist_ok=True)
    file_name = os.path.join(reports_dir, re.sub(r"[^\w.-]+", "_", nodeid) + ".png")
    screenshot_b64 = driver.get_screenshot_as_base64()
    with open(file_name, "wb") as f:
        f.write(base64.b64decode(screenshot_b64))
    return file_name, screenshot_b64


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when not in ("setup", "call"):
        return
    xfail = hasattr(report, "wasxfail")
    if not ((report.skipped and xfail) or (report.failed and not xfail)):
        return

    driver = item.funcargs.get("driverInvoke")
    if driver is None:
        return

    try:
        file_name, screenshot_b64 = _capture_screenshot(driver, report.nodeid)
    except Exception as e:
        print(f"Could not capture screenshot: {e}")
        return

    print("Screenshot saved:", file_name)
    extras = getattr(report, "extras", [])
    extras.append(html_extras.png(screenshot_b64, "Failure screenshot"))
    report.extras = extras