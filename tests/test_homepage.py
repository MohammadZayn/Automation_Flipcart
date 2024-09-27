import time
from Pages.login_page import login

class Test_Booking:
    def __init__(self, browser):
        self.driver = browser

    def test_login(self, driver):
        title = "Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!"
        self.driver.get("https://www.flipkart.com/")
        assert title in driver.title
        lp = login(driver)
        lp.login()
        lp.existing_user()
        time.sleep(10)
