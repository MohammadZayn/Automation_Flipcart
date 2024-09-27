from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class results:

    def __init__(self, browser):
        self.driver = browser

    def test_result(self):
        i = 0
        while i <= 10:
            lists = self.driver.find_elements(By.XPATH, '//div[@class="KzDlHZ"]')
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="KzDlHZ"]')))
            for each_item in lists:
                print(each_item.text)
            self.driver.find_element(By.XPATH, '// span[contains(text(), "Next")]').click()
            i = i + 1 