from selenium.webdriver.common.by import By


class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    promoCode_box = (By.CLASS_NAME, 'promoCode')
    apply_button = (By.CLASS_NAME, 'promoBtn')
    promo_text = (By.XPATH, '//span[@class="promoInfo"]')

    def promoCodeBox(self):
        return self.driver.find_element(*OrderPage.promoCode_box)

    def applyButton(self):
        return self.driver.find_element(*OrderPage.apply_button)

    def promoText(self):
        return self.driver.find_element(*OrderPage.promo_text)