import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.BaseClass import BaseClass
from pageObjects.OrderPage import OrderPage
from pageObjects.HomePage import HomePage


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        order_page = OrderPage(self.driver)
        product_names = homepage.productNames()


        for name in product_names:
            log.info(name.text)
            if "Broc" in name.text:
                homepage.incrementbutton().click()
                homepage.addToCartButton().click()

        homepage.cartIcon().click()
        assert "Brocolli" in homepage.vegName().text
        log.info("Brocolli is successfully selected")
        homepage.checkoutButton().click()

        self.WaitForElementPresence('promoCode')
        order_page.promoCodeBox().send_keys("rahulshettyacademy")
        order_page.applyButton().click()

        self.WaitForElementPresence("promoInfo")
        promo_text = order_page.promoText()
        assert "Code" in promo_text.text
