# pages/product_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    TITLE = (By.CSS_SELECTOR, 'h1.product-title')

    def wait_for_page(self):
        # ждем, пока заголовок появится
        self.find(self.TITLE)
