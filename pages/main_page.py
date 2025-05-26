import allure
from locators.locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Клик на кнопку Конструктор')
    def click_constructor(self):
        self.wait_for_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.find_element_and_click(MainPageLocators.CONSTRUCTOR_BUTTON)

    def is_constructor_section_visible(self):
        return self.check_element_is_visible(MainPageLocators.CREATE_BURGER_TEXT)

    def is_orders_feed_visible(self):
        return self.check_element_is_visible(MainPageLocators.READY_TEXT)

    def is_ingredient_popup_visible(self):
        return self.check_element_is_visible(MainPageLocators.INGREDIENT_DETAILS)

    def is_ingredient_popup_not_visible(self):
        return self.check_element_not_visible(MainPageLocators.INGREDIENT_DETAILS)

    def get_ingredient_counter_value(self):
        self.wait_for_element(MainPageLocators.COUNTER)
        return self.find_element(MainPageLocators.COUNTER).text

    def is_order_id_visible(self):
        return self.check_element_is_visible(MainPageLocators.ORDER_ID)

    def open_orders_feed(self):
        self.wait_for_element(MainPageLocators.ORDERS_FEED_BUTTON)
        self.find_element_and_click(MainPageLocators.ORDERS_FEED_BUTTON)

    def click_ingredient(self):
        self.wait_for_element(MainPageLocators.BUN_INGREDIENT)
        self.find_element_and_click(MainPageLocators.BUN_INGREDIENT)

    def close_ingredient_popup(self):
        self.wait_for_element(MainPageLocators.CLOSE_POP_UP_INGREDIENT_DETAILS_BUTTON)
        self.find_element_and_click(MainPageLocators.CLOSE_POP_UP_INGREDIENT_DETAILS_BUTTON)

    def add_ingredient(self):
        self.wait_for_element(MainPageLocators.SAUCES_BUTTON)
        self.find_element_and_click(MainPageLocators.SAUCES_BUTTON)
        self.drag_and_drop(MainPageLocators.SPICY_SAUCE, MainPageLocators.CONSTRUCTOR_FIELD)

    def place_order(self):
        self.wait_for_element(MainPageLocators.ORDER_BUTTON)
        self.find_element_and_click(MainPageLocators.ORDER_BUTTON)
