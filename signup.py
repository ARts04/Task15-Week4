import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestSignup(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_signup(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys("indra1") # isi name
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[2]").send_keys("indra1@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password_register").send_keys("123456") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('berhasil', response_data)
        self.assertEqual(response_message, 'created user!')

    def test_a_failed_signup(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[1]").send_keys(" ") # isi name
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/input[2]").send_keys(" ") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password_register").send_keys("123456") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('ops', response_data)
        self.assertEqual(response_message, 'Gagal Register!')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()