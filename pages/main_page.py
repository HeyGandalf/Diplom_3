import allure
from locators.locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Клик на кнопку Конструктор и проверка перехода на страницу')
    def click_constructor_and_check_redirect(self):
        self.wait_for_element(MainPageLocators.ORDERS_FEED_BUTTON)
        self.find_element_and_click(MainPageLocators.ORDERS_FEED_BUTTON)
        self.check_element_is_visible(MainPageLocators.READY_TEXT)
        self.wait_for_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.find_element_and_click(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.check_element_is_visible(MainPageLocators.CREATE_BURGER_TEXT)

    @allure.step('Клик на кнопку Лента заказов и проверка переход на страницу')
    def click_orders_and_check_redirect(self):
        self.wait_for_element(MainPageLocators.ORDERS_FEED_BUTTON)
        self.find_element_and_click(MainPageLocators.ORDERS_FEED_BUTTON)
        self.check_element_is_visible(MainPageLocators.READY_TEXT)

    @allure.step('Клик на ингредиент и проверка popup')
    def click_ingredient_and_check_popup(self):
        self.wait_for_element(MainPageLocators.BUN_INGREDIENT)
        self.find_element_and_click(MainPageLocators.BUN_INGREDIENT)
        self.check_element_is_visible(MainPageLocators.INGREDIENT_DETAILS)

    @allure.step('Клик на крестик на popup и проверка закрытия')
    def click_close_pop_up(self):
        self.wait_for_element(MainPageLocators.BUN_INGREDIENT)
        self.find_element_and_click(MainPageLocators.BUN_INGREDIENT)
        self.check_element_is_visible(MainPageLocators.INGREDIENT_DETAILS)
        self.wait_for_element(MainPageLocators.CLOSE_POP_UP_INGREDIENT_DETAILS_BUTTON)
        self.find_element_and_click(MainPageLocators.CLOSE_POP_UP_INGREDIENT_DETAILS_BUTTON)
        self.check_element_not_visible(MainPageLocators.INGREDIENT_DETAILS)

    @allure.step('Добавление ингредиента и проверка счетчика')
    def add_ingredient_and_check_counter(self):
        self.wait_for_element(MainPageLocators.SAUCES_BUTTON)
        self.find_element_and_click(MainPageLocators.SAUCES_BUTTON)
        self.drag_and_drop(MainPageLocators.SPICY_SAUCE, MainPageLocators.CONSTRUCTOR_FIELD)
        counter_element = self.find_element(MainPageLocators.COUNTER)
        assert counter_element.text == "1"

    @allure.step('Оформление заказа')
    def place_order_and_check(self):
        self.wait_for_element(MainPageLocators.ORDER_BUTTON)
        self.find_element_and_click(MainPageLocators.ORDER_BUTTON)
        self.check_element_is_visible(MainPageLocators.ORDER_POP_UP)
        self.check_element_is_visible(MainPageLocators.ORDER_ID)

    @allure.step('Закрытие popup')
    def click_close_order_pop_up(self):
        self.wait_for_element(MainPageLocators.ORDER_POP_UP)
        self.find_element_and_click(MainPageLocators.CLOSE_POP_UP_ORDER)
        self.check_element_not_visible(MainPageLocators.ORDER_POP_UP)