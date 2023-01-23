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
import cv2

class usando_unittest(unittest.TestCase):
    
    def setUp(self):
        options = Options()
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))  # noqa
        
    def test_usandoOpencv(self):
        driver = self.driver
        driver.get("http://www.google.com")
        driver.save_screenshot('img1.png')
        time.sleep(3)
    
    def test_comparandoImagenes(self):
        img2 = cv2.imread('img2.png')
        img1 = cv2.imread('img1.png')
        tamanoImg1 = img1.shape
        img2 = cv2.resize(img2, dsize=(tamanoImg1[1],tamanoImg1[0]))
        print(img1.shape)
        print(img2.shape)
        diferencia = cv2.absdiff(img1,img2) # comparador de imagenes en img1 y img2
        imagen_gris = cv2.cvtColor(diferencia, cv2.COLOR_BGR2GRAY)
        contours,_ = cv2.findContours(imagen_gris, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for c in contours:
            if cv2.contourArea(c) >= 20:
                posicion_x,posicion_y,ancho,alto = cv2.boundingRect(c)
                cv2.rectangle(img2, (posicion_x,posicion_y), (posicion_x+ancho, posicion_y+alto), (0,0,255),2)
                
        while(1):
            cv2.imshow('imagen 2' , img2)
            cv2.imshow('imagen2', img2)
            cv2.imshow('Diferencias detectadas', diferencia)
            teclado = cv2.waitKey(5) & 0xFF
            if teclado == 27:
                break
        cv2.destroyAllWindows()
        
        

    def tearDown(self):
        TearDown.tear_down(self)
        
    

if __name__ == '__main__':
    unittest.main()
