import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class PerformanceTest:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def test_login_performance(self):
        driver = self.driver
        driver.get("https://beats-stg.beraucoal.co.id/login")
        
        username = driver.find_element(By.XPATH, '//input[@placeholder="BeatsID"]')
        password = driver.find_element(By.XPATH, '//input[@placeholder="Password"]')
        login_button = driver.find_element(By.XPATH, '//div[@class="v-button v-widget friendly v-button-friendly v-has-width"]')
        
        # Start timing
        start_time = time.time()
        
        username.send_keys("XIIKM")
        password.send_keys("*!keykey")
        login_button.click()
        
        # Measure performance
        end_time = time.time()
        duration = end_time - start_time
        
        print(f"Login Performance Test Duration: {duration} seconds")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    test = PerformanceTest()
    test.test_login_performance()
    test.tearDown()
