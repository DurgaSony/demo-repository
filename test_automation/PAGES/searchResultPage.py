from selenium.webdriver.common.by import By

from test_automation.BASE.basepage import BaseDriver


class SearchResults(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def filter(self):
        self.driver.find_element(By.XPATH, "(//p[@class='font-lightgrey bold'])[{button}]").click()



