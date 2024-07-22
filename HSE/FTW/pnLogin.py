import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login_success(self):
        driver = self.driver
        driver.get("https://beats-stg.beraucoal.co.id/login")
        
        username = driver.find_element(By.XPATH, '//input[@placeholder="BeatsID"]')
        password = driver.find_element(By.XPATH, '//input[@placeholder="Password"]')
        
        username.send_keys("XIIKM")
        password.send_keys("*!keykey")
        
        login_button = driver.find_element(By.XPATH, '//div[@class="v-button v-widget friendly v-button-friendly v-has-width"]')
        login_button.click()
        
        # Wait for the specific HTML element to be present after login
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="v-horizontallayout v-layout v-horizontal v-widget v-has-height"]')))

        # Optionally, check the contents of the element
        if element:
            print("Login successful!")
        else:
            print("Error/Login Failed")

    def test_login_failure(self):
        driver = self.driver
        driver.get("https://beats-stg.beraucoal.co.id/login")
        
        username = driver.find_element(By.XPATH, '//input[@placeholder="BeatsID"]')
        password = driver.find_element(By.XPATH, '//input[@placeholder="Password"]')
        
        username.send_keys("false")
        password.send_keys("false")
        
        login_button = driver.find_element(By.XPATH, '//div[@class="v-button v-widget friendly v-button-friendly v-has-width"]')
        login_button.click()
        
        # Wait for the specific HTML element to be present after login
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "v-label-isa_error") and contains(text(), "Akun false Salah / Tidak Tersedia")]')))

        # Optionally, check the contents of the element
        if element:
            print("Login Fail!")
        else:
            print("Error")

    def tearDown(self):
        self.driver.close()

# Create a test suite and add tests in the desired order
def suite():
    suite = unittest.TestSuite()
    suite.addTest(LoginPageTest('test_login_success'))
    suite.addTest(LoginPageTest('test_login_failure'))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
