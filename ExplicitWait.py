import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from metodos.tear_down import  TearDown
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager #noqa
from selenium.webdriver.chrome.options import Options
import time

class usando_unittest(unittest.TestCase):
    
    def setUp(self):
        options = Options()
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))  # noqa
        
        

    def test_usando_Explicit_wait(self):
        driver = self.driver
        driver.get("http://www.google.com")
        try:
            element = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.NAME, "q")))
            element.send_keys("selenium")
            time.sleep(3)
        except Exception as e:
            print(e)
            driver.close()

    def tearDown(self):
        TearDown.tear_down(self)

if __name__ == '__main__': 
    report = "Add_products_to_favorites_best_offers_unlogged"
    unittest.main()


