from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class filters:

    def __init__(self, browser):
        self.driver = browser

    def choose_brand(self, brand):
        try:
            internal_xpath = '//div[contains(text(), "Brand")]'
            internal_element = self.driver.find_element(By.XPATH, internal_xpath)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, internal_xpath)))
            ActionChains(self.driver).move_to_element(internal_element).click().perform()
            self.driver.find_element(By.CLASS_NAME, "XPD6hh").send_keys(brand)
            processor_xpath = f'//div[@class="_6i1qKy" and contains(text(), "{brand}")]'
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, processor_xpath)))
            self.driver.find_element(By.XPATH, processor_xpath).click()

        except NoSuchElementException:
            print("Entered brand is not available")

    def price_range_slider(self):
        slider = self.driver.find_element(By.CLASS_NAME, 'PYKUdo')
        ActionChains(self.driver).click_and_hold(slider).move_by_offset(150, 0).release().perform()

    def offers(self, offer_Type):
        offers = self.driver.find_element(By.XPATH, '//div[contains(text(), "Offers")]')
        ActionChains(self.driver).move_to_element(offers).click().perform()
        offers.click()
        if offer_Type == "Buy More, Save More":
            self.driver.find_element(By.XPATH, '//div[@class="_6i1qKy" and contains(text(), "Buy More, Save More")]').click()
        elif offer_Type == "No Cost Emi":
            self.driver.find_element(By.XPATH, '//div[@class="_6i1qKy" and contains(text(), "No Cost EMI")]').click()
        else:
            self.driver.find_element(By.XPATH, '//div[contains(text(), "Special Price")]').click()

    def customer_rating_4(self, rating):
        if rating == 4:
            self.driver.find_element(By.XPATH, "//div[@class='_6i1qKy' and contains(text(),'4★')]").click()
        else:
            self.driver.find_element(By.XPATH, "//div[@class='_6i1qKy' and contains(text(),'3★')]").click()

    def flip_cart_assured(self):
        try:
            assured = self.driver.find_elements(By.CLASS_NAME, "vn9L2C")
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "vn9L2C")))
            assured.click()

        except NoSuchElementException:
            print("Internal Storage filter is not found.")

    def ram(self, ram_size):
        try:
            internal_xpath = '//div[contains(text(), "Ram")]'
            internal_element = self.driver.find_element(By.XPATH, internal_xpath)
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, internal_xpath)))
            ActionChains(self.driver).move_to_element(internal_element).click().perform()
            storage_xpath = f'//div[@class="_6i1qKy" and contains(text(), "{ram_size}")]'
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, storage_xpath)))
            self.driver.find_element(By.XPATH, storage_xpath).click()

        except NoSuchElementException:
            print("Internal Storage filter is not found.")

    def internal_storage(self, storage):
        try:
            internal_xpath = '//div[contains(text(), "Internal Storage")]'
            internal_element = self.driver.find_element(By.XPATH, internal_xpath)
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, internal_xpath)))
            ActionChains(self.driver).move_to_element(internal_element).click().perform()
            storage_xpath = f'//div[@class="_6i1qKy" and contains(text(), "{storage}")]'
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, storage_xpath)))
            self.driver.find_element(By.XPATH, storage_xpath).click()

        except NoSuchElementException:
            print("Internal Storage filter is not found.")


    def gst_applicable(self):
        try:
            internal_xpath = '//div[contains(text(), "GST Invoice Available")]'
            internal_element = self.driver.find_element(By.XPATH, internal_xpath)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, internal_xpath)))
            ActionChains(self.driver).move_to_element(internal_element).click().perform()
            gst_xpath = f'//div[@class="_6i1qKy" and contains(text(), "GST Invoice Available")]'
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, gst_xpath)))
            self.driver.find_element(By.XPATH, gst_xpath).click()

        except NoSuchElementException:
            print("GST option is not found.")

    def battery_capacity(self, capacity):
        try:
            internal_xpath = '//div[contains(text(), "Battery Capacity")]'
            internal_element = self.driver.find_element(By.XPATH, internal_xpath)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, internal_xpath)))
            ActionChains(self.driver).move_to_element(internal_element).click().perform()
            battery_xpath = f'//div[@class="_6i1qKy" and contains(text(), "{capacity}")]'
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, battery_xpath)))
            self.driver.find_element(By.XPATH, battery_xpath).click()

        except NoSuchElementException:
            print("Battery capacity is not found.")

    def screen_size(self, size):
        try:
            internal_xpath = '//div[contains(text(), "Screen Size")]'
            internal_element = self.driver.find_element(By.XPATH, internal_xpath)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, internal_xpath)))
            ActionChains(self.driver).move_to_element(internal_element).click().perform()
            screen_xpath = f'//div[@class="_6i1qKy" and contains(text(), "{size}")]'
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,screen_xpath)))
            self.driver.find_element(By.XPATH, screen_xpath).click()

        except NoSuchElementException:
            print("Entered size is not available")

    def primary_camera(self, size):
        try:
            internal_xpath = '//div[contains(text(), "Primary Camera")]'
            internal_element = self.driver.find_element(By.XPATH, internal_xpath)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, internal_xpath)))
            ActionChains(self.driver).move_to_element(internal_element).click().perform()
            camera_xpath = f'//div[@class="_6i1qKy" and contains(text(), "{size}")]'
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,camera_xpath)))
            self.driver.find_element(By.XPATH, camera_xpath).click()

        except NoSuchElementException:
            print("Entered Camera is not available")

    def secondary_camera(self, size):
        try:
            internal_xpath = '//div[contains(text(), "Secondary Camera")]'
            internal_element = self.driver.find_element(By.XPATH, internal_xpath)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, internal_xpath)))
            ActionChains(self.driver).move_to_element(internal_element).click().perform()
            camera_xpath = f'//div[@class="_6i1qKy" and contains(text(), "{size}")]'
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,camera_xpath)))
            self.driver.find_element(By.XPATH, camera_xpath).click()

        except NoSuchElementException:
            print("Entered Camera is not available")

    def processor_brand(self, size):
        try:
            internal_xpath = '//div[contains(text(), "Processor Brand")]'
            internal_element = self.driver.find_element(By.XPATH, internal_xpath)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, internal_xpath)))
            ActionChains(self.driver).move_to_element(internal_element).click().perform()
            processor_xpath = f'//div[@class="_6i1qKy" and contains(text(), "{size}")]'
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,processor_xpath)))
            self.driver.find_element(By.XPATH, processor_xpath).click()

        except NoSuchElementException:
            print("Entered processor is not available")

    def processor(self, size):
        try:
            internal_xpath = '//div[contains(text(), "Processor")]'
            internal_element = self.driver.find_element(By.XPATH, internal_xpath)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, internal_xpath)))
            ActionChains(self.driver).move_to_element(internal_element).click().perform()
            processor_xpath = f'//div[@class="_6i1qKy" and contains(text(), "{size}")]'
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,processor_xpath)))
            self.driver.find_element(By.XPATH, processor_xpath).click()

        except NoSuchElementException:
            print("Entered processor is not available")

    def specaility(self, size):
        try:
            internal_xpath = '//div[contains(text(), "Speciality")]'
            internal_element = self.driver.find_element(By.XPATH, internal_xpath)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, internal_xpath)))
            ActionChains(self.driver).move_to_element(internal_element).click().perform()
            processor_xpath = f'//div[@class="_6i1qKy" and contains(text(), "{size}")]'
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,processor_xpath)))
            self.driver.find_element(By.XPATH, processor_xpath).click()

        except NoSuchElementException:
            print("Entered processor is not available")

    def resolution_type(self, size):
        try:
            internal_xpath = '//div[contains(text(), "Resolution Type")]'
            internal_element = self.driver.find_element(By.XPATH, internal_xpath)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, internal_xpath)))
            ActionChains(self.driver).move_to_element(internal_element).click().perform()
            processor_xpath = f'//div[@class="_6i1qKy" and contains(text(), "{size}")]'
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,processor_xpath)))
            self.driver.find_element(By.XPATH, processor_xpath).click()

        except NoSuchElementException:
            print("Entered processor is not available")

    def os_type(self, size):
        try:
            internal_xpath = '//div[contains(text(), "Operating System")]'
            internal_element = self.driver.find_element(By.XPATH, internal_xpath)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, internal_xpath)))
            ActionChains(self.driver).move_to_element(internal_element).click().perform()
            processor_xpath = f'//div[@class="_6i1qKy" and contains(text(), "{size}")]'
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,processor_xpath)))
            self.driver.find_element(By.XPATH, processor_xpath).click()

        except NoSuchElementException:
            print("Entered processor is not available")

    def network_type(self, size):
        try:
            internal_xpath = '//div[contains(text(), "Network Type")]'
            internal_element = self.driver.find_element(By.XPATH, internal_xpath)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, internal_xpath)))
            ActionChains(self.driver).move_to_element(internal_element).click().perform()
            processor_xpath = f'//div[@class="_6i1qKy" and contains(text(), "{size}")]'
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,processor_xpath)))
            self.driver.find_element(By.XPATH, processor_xpath).click()

        except NoSuchElementException:
            print("Entered processor is not available")

    def sim_type(self, size):
        try:
            internal_xpath = '//div[contains(text(), "Sim Type")]'
            internal_element = self.driver.find_element(By.XPATH, internal_xpath)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, internal_xpath)))
            ActionChains(self.driver).move_to_element(internal_element).click().perform()
            processor_xpath = f'//div[@class="_6i1qKy" and contains(text(), "{size}")]'
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,processor_xpath)))
            self.driver.find_element(By.XPATH, processor_xpath).click()

        except NoSuchElementException:
            print("Entered processor is not available")

    def features(self, feature):
        try:
            internal_xpath = '//div[contains(text(), "Features")]'
            internal_element = self.driver.find_element(By.XPATH, internal_xpath)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, internal_xpath)))
            ActionChains(self.driver).move_to_element(internal_element).click().perform()
            feature_xpath = f'//div[@class="_6i1qKy" and contains(text(), "{feature}")]'
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, feature_xpath)))
            self.driver.find_element(By.XPATH, feature_xpath).click()

        except NoSuchElementException:
            print("Entered feature is not available")

    def type(self, size):
        try:
            internal_xpath = '//div[contains(text(), "Type")]'
            internal_element = self.driver.find_element(By.XPATH, internal_xpath)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, internal_xpath)))
            ActionChains(self.driver).move_to_element(internal_element).click().perform()
            processor_xpath = f'//div[@class="_6i1qKy" and contains(text(), "{size}")]'
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,processor_xpath)))
            self.driver.find_element(By.XPATH, processor_xpath).click()

        except NoSuchElementException:
            print("Entered type is not available")

    def number_of_cores(self, size):
        try:
            internal_xpath = '//div[contains(text(), "Number of Cores")]'
            internal_element = self.driver.find_element(By.XPATH, internal_xpath)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, internal_xpath)))
            ActionChains(self.driver).move_to_element(internal_element).click().perform()
            processor_xpath = f'//div[@class="_6i1qKy" and contains(text(), "{size}")]'
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,processor_xpath)))
            self.driver.find_element(By.XPATH, processor_xpath).click()

        except NoSuchElementException:
            print("Entered cores is not available")

    def availability(self, size):
        try:
            internal_xpath = '//div[contains(text(), "Availability")]'
            internal_element = self.driver.find_element(By.XPATH, internal_xpath)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, internal_xpath)))
            ActionChains(self.driver).move_to_element(internal_element).click().perform()
            processor_xpath = f'//div[@class="_6i1qKy" and contains(text(), "{size}")]'
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,processor_xpath)))
            self.driver.find_element(By.XPATH, processor_xpath).click()

        except NoSuchElementException:
            print("Entered availability is not available")

    def discount(self, size):
        try:
            internal_xpath = '//div[contains(text(), "Discount")]'
            internal_element = self.driver.find_element(By.XPATH, internal_xpath)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, internal_xpath)))
            ActionChains(self.driver).move_to_element(internal_element).click().perform()
            discount_xpath = f'//div[@class="_6i1qKy" and contains(text(), "{size}")]'
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, discount_xpath)))
            self.driver.find_element(By.XPATH, discount_xpath).click()

        except NoSuchElementException:
            print("Entered discount is not available")

    def operating_version(self, size):
        try:
            internal_xpath = '//div[contains(text(), "Operating System Version Name")]'
            internal_element = self.driver.find_element(By.XPATH, internal_xpath)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, internal_xpath)))
            ActionChains(self.driver).move_to_element(internal_element).click().perform()
            version_xpath = f'//div[@class="_6i1qKy" and contains(text(), "{size}")]'
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, version_xpath)))
            self.driver.find_element(By.XPATH, version_xpath).click()

        except NoSuchElementException:
            print("Entered OS is not available")

    def clock_speed(self, speed):
        try:
            internal_xpath = '//div[contains(text(), "Clock Speed")]'
            internal_element = self.driver.find_element(By.XPATH, internal_xpath)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, internal_xpath)))
            ActionChains(self.driver).move_to_element(internal_element).click().perform()
            speed_xpath = f'//div[@class="_6i1qKy" and contains(text(), "{speed}")]'
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, speed_xpath)))
            self.driver.find_element(By.XPATH, speed_xpath).click()

        except NoSuchElementException:
            print("Entered clock speed is not available")













