import time

from Pages.filters_page import filters
from Pages.home_page import home

class Test_booking1:
    def test_booking(self, browser):
        browser.get("https://www.flipkart.com/")
        hm = home(browser)
        fl = filters(browser)
        hm.search_bar()
        fl.ram(ram_size="8")
        time.sleep(5)
        fl.internal(internal_size="32")
        time.sleep(15)