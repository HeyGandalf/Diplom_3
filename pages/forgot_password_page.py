import allure
from helpers.data import PersonalData
from locators.locators import ForgotPasswordPageLocators, MainPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    @allure.step('Переход на страницу восстановления пароля со страницы Вход')
    def switch_to_reset_password(self):
        self.wait_for_element(MainPageLocators.LOG_IN_BUTTON)
        self.find_element_and_click(MainPageLocators.LOG_IN_BUTTON)
        self.wait_for_element(ForgotPasswordPageLocators.RESET_PASSWORD_BUTTON)
        self.find_element_and_click(ForgotPasswordPageLocators.RESET_PASSWORD_BUTTON)
        self.wait_for_element(ForgotPasswordPageLocators.RESETTING_PASSWORD_TEXT)

    @allure.step('Переход на страницу восстановления пароля по кнопке Восстановить')
    def click_reset_password_and_check_redirect(self):
        self.wait_for_element(ForgotPasswordPageLocators.RESET_PASSWORD_BUTTON)
        self.find_element_and_click(ForgotPasswordPageLocators.RESET_PASSWORD_BUTTON)
        self.wait_for_element(ForgotPasswordPageLocators.RESETTING_PASSWORD_TEXT)
        self.wait_for_element(ForgotPasswordPageLocators.EMAIL_FIELD)
        self.add_text_to_form(ForgotPasswordPageLocators.EMAIL_FIELD, PersonalData.REGISTRATION_EMAIL)
        self.find_element_and_click(ForgotPasswordPageLocators.RESET_BUTTON)
        self.wait_for_element(ForgotPasswordPageLocators.RESETTING_PASSWORD_TEXT)

    @allure.step('Ввод почты и клик на кнопку Восстановить')
    def fill_in_email_and_reset(self, email):
        self.wait_for_element(ForgotPasswordPageLocators.EMAIL_FIELD)
        self.add_text_to_form(ForgotPasswordPageLocators.EMAIL_FIELD, email)
        self.find_element_and_click(ForgotPasswordPageLocators.RESET_BUTTON)
        self.wait_for_element(ForgotPasswordPageLocators.SAVE_BUTTON)

    @allure.title('Ввод пароля и проверка кнопки Скрыть пароль')
    def fill_password_in_and_check_visibility(self, password):
        self.add_text_to_form(ForgotPasswordPageLocators.PASSWORD_FIELD, password)
        self.find_element_and_click(ForgotPasswordPageLocators.SHOW_PASSWORD_BUTTON)
        self.wait_for_element(ForgotPasswordPageLocators.PASSWORD_INPUT_ACTIVE)

    @allure.step('Ввод пароля')
    def fill_password_in(self, password):
        self.add_text_to_form(ForgotPasswordPageLocators.PASSWORD_FIELD, password)

    @allure.step('Проверка кнопки Скрыть пароль/Показать пароль')
    def check_visibility(self):
        self.find_element_and_click(ForgotPasswordPageLocators.SHOW_PASSWORD_BUTTON)
        self.wait_for_element(ForgotPasswordPageLocators.PASSWORD_INPUT_ACTIVE)

    def is_element_visible(self, locator):
        try:
            return self.check_element_is_visible(locator)
        except:
            return False
