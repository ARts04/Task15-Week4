import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

class TestCart(unittest.TestCase): 
    
    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_cart(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://automationpractice.com/index.php?id_category=8&controller=category") # buka situs
        time.sleep(3)
        drop = Select(browser.find_element(By.ID,"selectProductSort"))
        drop.select_by_visible_text("In stock")
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR,"input#layered_id_attribute_group_13").click() # klik warna
        time.sleep(5)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/div/div[3]/div[2]/ul/li[1]/div/div[1]/div/a[1]/img").click()
        time.sleep(10)
        browser.find_element(By.ID, "quantity_wanted").send_keys(Keys.CONTROL, "a")
        browser.find_element(By.ID, "quantity_wanted").send_keys("5")
        time.sleep(10)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/div/div[3]/div/div/div/div[4]/form/div/div[3]/div/p/button/span").click()
        time.sleep(5)        


if __name__ == "__main__": 
    unittest.main()