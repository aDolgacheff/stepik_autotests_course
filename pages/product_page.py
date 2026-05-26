from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    def click_add_to_basket_btn(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        btn.click()

    def should_be_product_name_in_message(self, product_name):
        successful_adding_message = self.browser.find_element(*ProductPageLocators.MESSAGE_SUCCESSFUL_ADDING).text
        assert product_name == successful_adding_message, "Название товара не соответсвует названию в уведомлении"

    def should_be_product_price_in_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price_message = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_PRICE).text
        assert product_price in basket_price_message, "Сумма корзины не соответсвует цене товара"
