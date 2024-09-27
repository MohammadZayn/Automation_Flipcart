import time
from selenium.webdriver.common.by import By
from tests.conftest import browser

class login:

    def __init__(self, browser):
        self.driver = browser

    def login(self):
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Login')]").click()

    def existing_user(self):
        value = "//input[contains(@class, 'r4vIwl') and contains(@class, 'BV+Dqf')]"
        request_otp = "//button[contains(@class,'QqFHMw')]"
        submit_otp = "//input[contains(@class, 'r4vIwl') and contains(@class, 'IX3CMV')]"
        self.driver.find_element(By.XPATH, value).send_keys('localboymohammad47@gmail.com')
        self.driver.find_element(By.XPATH, request_otp).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH,submit_otp).send_keys("123456")
        time.sleep(10)
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(10)


