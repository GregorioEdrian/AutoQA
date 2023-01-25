import unittest
from selenium import webdriver
from metodos.set_up import SetUp
from metodos.tear_down import TearDown
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import select as something

class usando_select(unittest.TestCase):
    def setUp(self):
        SetUp.set_up(self, 'https://www.w3schools.com/howto/howto_custom_select.asp')
        
    
    def test_usandoSelect(self):
        driver = self.driver
        driver.implicitly_wait(10)
        select = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div[1]/select')
        opcion = select.find_elements(By.TAG_NAME, 'option')
        driver.implicitly_wait(3)
        for option in opcion:
            print("Los valores son: %s " % option.get_attribute("value"))
            option.click()
            time.sleep(1)
        seleccionar = Select(driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div[1]/select'))
        seleccionar.select_by_value("10")
        time.sleep(3)
        
    def tearDown(self):
        TearDown.tear_down(self)
    
if __name__ == '__main__':
    unittest.main()