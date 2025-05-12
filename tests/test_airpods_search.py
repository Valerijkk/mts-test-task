# tests/test_airpods_search.py
import os
from selenium import webdriver
from pages.home_page import HomePage
from pages.product_page import ProductPage

def test_find_airpods_and_screenshot():
    driver = webdriver.Chrome()
    driver.maximize_window()

    home = HomePage(driver)
    home.open()
    home.search("AirPods 4")
    home.go_to_product()

    product = ProductPage(driver)
    product.wait_for_page()

    # скриншот
    os.makedirs("screenshots", exist_ok=True)
    driver.save_screenshot("screenshots/airpods4.png")

    driver.quit()
