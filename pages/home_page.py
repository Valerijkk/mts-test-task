# pages/home_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[type="search"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    PRODUCT_LINK = (By.PARTIAL_LINK_TEXT, 'AirPods 4')

    def open(self):
        self.driver.get("https://shop.mts.ru/")

    def search(self, text):
        self.find(self.SEARCH_INPUT).send_keys(text)
        self.click(self.SEARCH_BUTTON)

    def go_to_product(self):
        self.find(self.PRODUCT_LINK).click()
