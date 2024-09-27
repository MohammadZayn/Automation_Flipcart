import time

from Pages.filters_page import filters
from Pages.home_page import home

class Test_booking:
    def test_booking(self, browser):
        browser.get("https://www.flipkart.com/")
        hm = home(browser)
        fl = filters(browser)
        hm.search_bar()
        time.sleep(5)
        fl.internal_storage(storage="256 GB & Above")
        time.sleep(5)
        fl.customer_rating_4(rating=4)
        fl.ram(ram_size="8")
        fl.features(feature="WiFi")
        time.sleep(25)
