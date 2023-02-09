
from selenium.webdriver.common.by import By


class HomePageLocators:

    ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'a.add_to_cart_button')
    VIEW_CART = (By.XPATH, "//a[@title='View cart']")

