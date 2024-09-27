import time
from Pages.login_page import login

def test_login(browser):
    title = "Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!"
    browser.get("https://www.flipkart.com/")
    assert title in browser.title
    lp = login(browser)
    lp.login()
    lp.existing_user()
    time.sleep(10)
