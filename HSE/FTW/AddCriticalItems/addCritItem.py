from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException

class CriticalItemsTest:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        
    def login(self):
        driver = self.driver
        driver.get("https://beats-stg.beraucoal.co.id/login")
        
        username = driver.find_element(By.XPATH, '//input[@placeholder="BeatsID"]')
        password = driver.find_element(By.XPATH, '//input[@placeholder="Password"]')
        
        username.send_keys("XIIKM")
        password.send_keys("*!keykey")
        
        login_button = driver.find_element(By.XPATH, '//div[@class="v-button v-widget friendly v-button-friendly v-has-width"]')
        login_button.click()
        
        # Wait for login to complete, e.g., by waiting for a specific element to be visible
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="v-accordion-item-caption"]')))

    # def navigate_to_critical_items(self):
    #     driver = self.driver
        
        # Click on the "Administration" accordion item
        admin_accordion = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="v-accordion-item-caption"]/div[@class="v-caption"]/div[@class="v-captiontext" and text()="Administration"]')))
        admin_accordion.click()
        
        # Wait for the "Master Critical Items" button to be visible and click it
        master_critical_items_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="v-slot v-slot-borderless v-slot-small v-slot-quiet v-slot-v-fusi-button-left-menu v-slot-fusi-btn"]/div[@class="v-button v-widget borderless v-button-borderless small v-button-small quiet v-button-quiet v-fusi-button-left-menu v-button-v-fusi-button-left-menu fusi-btn v-button-fusi-btn v-has-width"]//span[text()="Master Critical Items"]')))
        master_critical_items_button.click()
    
    def add_critical_item(self):
        driver = self.driver
        # Assuming you have the form or button to add a critical item
        add_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Add Critical Item")]')))
        add_button.click()
        
        # Fill out the form, for example:
        item_name = self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="itemName"]')))
        item_name.send_keys("New Critical Item")
        
        # Submit the form
        submit_button = driver.find_element(By.XPATH, '//button[contains(text(), "Submit")]')
        submit_button.click()
        
        # Verify the item was added
        success_message = self.wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Critical Item added successfully")]')))
        print(success_message.text)
    
    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    test = CriticalItemsTest()
    
    test.login()
    # test.navigate_to_critical_items()
    # test.add_critical_item()
    
    test.close()
