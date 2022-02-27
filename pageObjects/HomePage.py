import pytest
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    productName = (By.XPATH, '//div[@class="product"]//h4[@class="product-name"]')
    increment_button = (By.XPATH, '//div[@class="product"]//a[@class="increment"]')
    addToCart_button = (By.XPATH, '//div[@class="product-action"]/button[@type="button"]')
    cart_icon = (By.XPATH, '//img[@alt="Cart"]')
    veg_name = (By.XPATH, '//div[@class="product-info"]/p[@class="product-name"]')
    checkout_button = (By.XPATH, '//div[@class="action-block"]/button[@type="button"][1]')

    def productNames(self):
        return self.driver.find_elements(*HomePage.productName)

    def incrementbutton(self):
        return self.driver.find_element(*HomePage.increment_button)

    def addToCartButton(self):
        return self.driver.find_element(*HomePage.addToCart_button)

    def cartIcon(self):
        return self.driver.find_element(*HomePage.cart_icon)

    def vegName(self):
        return self.driver.find_element(*HomePage.veg_name)

    def checkoutButton(self):
        return self.driver.find_element(*HomePage.checkout_button)


#This method is used to pass data and run mutiple times using each tuple in array
    @pytest.fixture(params=[(), ()])
    def getData(self, request):
        return request.params
