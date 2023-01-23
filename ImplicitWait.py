import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager #noqa
from selenium.webdriver.chrome.service import Service

class usando_unittest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))  # noqa

    def test_implicitWait(self):
        driver = self.driver
        driver.implicitly_wait(5) # Rango en segundos de espera hasta que realiza la acción.
        driver.get("http://www.google.com")
        myDynamicElement = driver.find_element(By.NAME, "q")
        myDynamicElement.send_keys("casa")
        time.sleep(3)

def tearDown(self):
        TearDown.tear_down(self)

if __name__ == '__main__': 
    report = "Add_products_to_favorites_best_offers_unlogged"
    unittest.main()
