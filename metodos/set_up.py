import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class SetUp(unittest.TestCase):
    def set_up(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # noqa
        driver = self.driver
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get('https://adan-farm.web.app/')
