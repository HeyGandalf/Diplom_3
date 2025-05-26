from pages.base_page import BasePage
import allure
from locators.locators import AccountPageLocators, ForgotPasswordPageLocators, MainPageLocators

class AccountPage(BasePage):

    @allure.step('Переход в личный кабинет')
    def switch_to_account(self):
        self.find_element_and_click(MainPageLocators.ACCOUNT_BUTTON)
        self.check_element_is_visible(AccountPageLocators.PROFILE_BUTTON)

    @allure.step('Проверка, что личный кабинет открыт')
    def check_account_page_open(self):
        self.find_element_and_click(MainPageLocators.ACCOUNT_BUTTON)
        self.check_element_is_visible(AccountPageLocators.PROFILE_BUTTON)
        self.check_element_is_visible(AccountPageLocators.HISTORY_BUTTON)

    @allure.step('Переход в историю заказов')
    def switch_to_orders(self):
        self.find_element_and_click(MainPageLocators.ACCOUNT_BUTTON)
        self.find_element_and_click(AccountPageLocators.HISTORY_BUTTON)
        self.check_element_is_visible(AccountPageLocators.ORDER_COMPLETED_TEXT)


    @allure.step('Проверка, что открыта страница Истории заказов')
    def check_switch_to_orders_history(self):
        self.find_element_and_click(MainPageLocators.ACCOUNT_BUTTON)
        self.find_element_and_click(AccountPageLocators.HISTORY_BUTTON)
        self.wait_for_element(AccountPageLocators.HISTORY_BUTTON_ACTIVE)

    @allure.step('Выход')
    def log_out(self):
        self.find_element_and_click(MainPageLocators.ACCOUNT_BUTTON)
        self.find_element_and_click(AccountPageLocators.EXIT_BUTTON)
        self.check_element_is_visible(ForgotPasswordPageLocators.EMAIL_FIELD)
