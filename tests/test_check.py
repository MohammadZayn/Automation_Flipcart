import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from tests.conftest import browser
from Pages.home_page import home
from Pages.results_page import results


class Test_automation:
    ''' def test_login1(self, browser):
        title = "Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!"
        browser.get("https://www.flipkart.com/")
        assert title in browser.title
        action = ActionChains(browser)
        element = browser.find_element(By.XPATH, "//img[@alt='Chevron']")
        action.move_to_element(element).perform()
        time.sleep(15) '''

    def test_res(self, browser):
        browser.get("https://www.flipkart.com/")
        hm = home(browser)
        res = results(browser)
        hm.search_bar()
        res.test_result()
