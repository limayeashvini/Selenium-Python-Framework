
# Base class for all page objects; holds the driver and helpers every page uses
class browserUtils:
    def __init__(self,driver):
        self.driver = driver

    # Return the current page title
    def getTitile(self):
        return self.driver.title
