import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://myappventure.herokuapp.com/for-you") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/nav/div/div[2]/div[2]/a/button").click() # masuk
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[1]/input").send_keys("budi12@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/label[2]/div[2]/input").send_keys("123456") # isi pass
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[4]/button").click() # klik tombol masuk
        time.sleep(10)
        browser.find_element(By.XPATH,"/html/body/div/nav/div/div[1]/div/div/div/button").click() # klik menu
        time.sleep(5)
        browser.find_element(By.XPATH,"/html/body/div/nav/div/div[1]/div/div/div[2]/div/a[5]/div").click() # klik akun
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/section/div[2]/div[4]/button").click() # klik akun
        time.sleep(1)
        

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()