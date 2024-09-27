from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from tests.conftest import browser

class home:
    def __init__(self, browser):
        self.driver = browser

    def search_bar(self):
        search_bar = self.driver.find_element(By.CLASS_NAME, "Pke_EE")
        actions = ActionChains(self.driver)
        actions.click(search_bar).send_keys("one plus mobiles").send_keys(Keys.ENTER).perform()

    def choose_brand(self):
        self.driver.find_element(By.CLASS_NAME, "XPD6hh").send_keys("oneplus")
        self.driver.find_element(By.CLASS_NAME,"_6i1qKy").click()