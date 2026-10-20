
class browserUtils:
    def __init__(self,driver):
        self.driver = driver

    def getTitile(self):
        return self.driver.title
