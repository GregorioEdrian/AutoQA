import unittest
from metodos.set_up import SetUp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from metodos.tear_down import  TearDown
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager #noqa
from selenium.webdriver.chrome.options import Options

class click_switch(unittest.TestCase):
    
    def setUp(self):
        SetUp.set_up(self, 'https://www.w3schools.com/howto/howto_css_switch.asp')
        
        
    def test_clickToggle(self):
        driver = self.driver
        driver.implicitly_wait(3)
        toggle = driver.find_element(By.XPATH, '//*[@id="main"]/label[3]/div')
        toggle.click()
        time.sleep(3)
        toggle.click()
        time.sleep(3)
    
    def tearDown(self):
        TearDown.tearDown(self)
    
if __name__ == '__main__':
    unittest.main()