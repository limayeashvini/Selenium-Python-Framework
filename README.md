# Python Selenium Framework

Developed by: Ashvini Limaye
Created: 2026-10-20

A UI test automation framework built with **Python**, **Selenium WebDriver** and **pytest**, using the **Page Object Model**. The tests run against the practice site [rahulshettyacademy.com](https://rahulshettyacademy.com).

## What the tests cover

| Test | What it checks |
|------|----------------|
| `tests/test_e2e_framework.py` | End-to-end shopping flow: login → add a product to the cart → checkout → choose a country → purchase → check the success message. It runs once for each data set in `data/test_e2e_framework.json`. |
| `tests/test_sorting.py` | Clicking the first column header on the offers table sorts the names alphabetically. |

## Features

- **Page Object Model:** each page has its own class in `pageObject/`, so locators and page actions are kept out of the tests.
- **Data-driven tests:** login details and product names come from a JSON file.
- **Chrome or Firefox:** choose the browser from the command line.
- **HTML report:** written to `reports/report.html` after every run.
- **Screenshots on failure:** saved to `reports/` and embedded in the HTML report.

## Project structure

```
pythonSeleniumProject/
├── conftest.py               # Browser fixture, --browserName option, HTML report and failure screenshots
├── pytest.ini                # pytest settings and markers (smoke)
├── requirements.txt          # Python packages to install
├── data/
│   └── test_e2e_framework.json   # Test data: username, password, product name
├── pageObject/
│   ├── login.py                  # Login page
│   ├── shopPage.py               # Shop / product list page
│   └── checkout_confirmation.py  # Cart, checkout and purchase pages
├── tests/
│   ├── test_e2e_framework.py     # End-to-end purchase test
│   └── test_sorting.py           # Table sorting test
├── utils/
│   └── browserUtils.py       # Base class shared by all page objects
├── assets/                   # CSS for the HTML report
└── reports/                  # Generated reports and screenshots (not committed to git)
```

## Prerequisites

- **Python 3.10 or newer** (developed on Python 3.12)
- **Google Chrome** and/or **Mozilla Firefox** installed
- **Git**

You don't need to download ChromeDriver or GeckoDriver yourself. Selenium 4 includes Selenium Manager, which downloads the matching driver automatically on the first run.

## Setup

Run these commands one at a time.

**1. Clone the repository**
```bash
git clone <repository-url>
```

**2. Go into the project folder**
```bash
cd pythonSeleniumProject
```

**3. Create a virtual environment**
```bash
python -m venv .venv
```

**4. Activate it**

Windows (PowerShell):
```powershell
.venv\Scripts\Activate.ps1
```
macOS / Linux:
```bash
source .venv/bin/activate
```

**5. Install the packages**
```bash
pip install -r requirements.txt
```

## Running the tests

Always run pytest **from the project folder**, because the test data is loaded with a relative path.

| Command | What it does |
|---------|--------------|
| `pytest` | Runs all tests in Chrome |
| `pytest --browserName firefox` | Runs all tests in Firefox |
| `pytest -m smoke` | Runs only tests marked `smoke` |
| `pytest tests/test_sorting.py` | Runs a single test file |
| `pytest -v -s` | Verbose output, and shows `print()` output |
| `pytest --html=reports/my_report.html` | Saves the HTML report somewhere else |

## Reports

- After every run, open **`reports/report.html`** in a browser to see the results.
- When a test fails, a screenshot is saved in `reports/` and attached to that test in the HTML report.
- The `reports/` folder is listed in `.gitignore`, so reports are never committed.

## Test data

Edit `data/test_e2e_framework.json` to change or add test cases. Each entry produces one test run:

```json
{
  "data": [
    {
      "userEmail": "rahulshettyacademy",
      "userPassword": "Learning@830$3mK2",
      "productName": "Blackberry"
    }
  ]
}
```

`productName` must exactly match a product title on the shop page, for example `Blackberry`, `Nokia Edge`, `iphone X` or `Samsung Note 8`.

## Adding a new page or test

1. Create a class for the page in `pageObject/` that inherits from `browserUtils`. Put its locators in `__init__` and its actions as methods.
2. Have a method return the next page's object when an action moves to another page, as `loginPage.login()` returns `shopPage`.
3. Write the test in `tests/` with a name starting `test_`, and use the `driverInvoke` fixture to get a browser.
