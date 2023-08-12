import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BaseTest:
    @pytest.fixture(autouse=True)
    def init_driver(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 30)
        yield self.driver, self.wait

        if self.driver is not None:
            self.driver.close()
