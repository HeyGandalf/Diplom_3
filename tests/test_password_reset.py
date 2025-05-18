import allure
from pages.base_page import BasePage
from pages.forgot_password_page import ForgotPasswordPage
from helpers.urls import Urls
from helpers.data import PersonalData
from locators.locators import ForgotPasswordPageLocators


@allure.suite("Восстановление пароля")
class TestResetPassword:

    @allure.title("Переход по кнопке 'Восстановить пароль' на форму сброса")
    @allure.description("Проверка, что при клике на 'Восстановить пароль' происходит переход на страницу сброса пароля.")
    def test_switch_to_reset_password_by_click_on_reset_button(self, driver):
        base_page = BasePage(driver)
        base_page.open_page(Urls.LOGIN)
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.click_reset_password_and_check_redirect()
        assert forgot_password_page.check_element_is_visible(ForgotPasswordPageLocators.RESETTING_PASSWORD_TEXT)

    @allure.title("Ввод почты и клик на кнопку 'Восстановить'")
    @allure.description("Проверка, что ввод почты и переход после клика по кнопке 'Восстановить' показывает кнопку 'Сохранить'")
    def test_reset_password_click(self, driver):
        base_page = BasePage(driver)
        base_page.open_page(Urls.FORGOT_PASSWORD)
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.fill_in_email_and_reset(PersonalData.REGISTRATION_EMAIL)
        assert forgot_password_page.check_element_is_visible(ForgotPasswordPageLocators.SAVE_BUTTON)

    @allure.title("Кнопка показать/скрыть активирует поле")
    @allure.description("Проверка, что клик по кнопке показать/скрыть пароль делает поле активным")
    def test_show_hide_password_button_activates_field(self, driver):
        base_page = BasePage(driver)
        base_page.open_page(Urls.FORGOT_PASSWORD)
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.fill_in_email_and_reset(PersonalData.REGISTRATION_EMAIL)
        forgot_password_page.fill_password_in("1234567")
        forgot_password_page.check_visibility()
