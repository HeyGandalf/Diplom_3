import allure
from helpers.urls import Urls
from helpers.data import PersonalData
from locators.locators import AccountPageLocators, MainPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step("Открытие страницы логина")
    def open(self):
        self.driver.get(Urls.LOGIN)

    @allure.step("Выполнение входа в систему")
    def login(self):
        self.wait_for_element(AccountPageLocators.INPUT_PASSWORD)
        self.add_text_to_form(AccountPageLocators.INPUT_EMAIL, PersonalData.LOGIN)
        self.add_text_to_form(AccountPageLocators.INPUT_PASSWORD, PersonalData.PASSWORD)
        self.find_element_and_click(AccountPageLocators.BUTTON_ENTER)
        self.check_element_is_visible(MainPageLocators.ORDER_BUTTON)
