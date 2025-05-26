import allure
from pages.account_page import AccountPage
from locators.locators import AccountPageLocators


@allure.suite("Личный кабинет")
class TestAccount:

    @allure.title("Переход в личный кабинет по клику")
    @allure.description("Проверка, что при клике на «Личный кабинет» отображаются кнопки 'Профиль' и 'История заказов'")
    def test_switch_to_account_by_click(self, driver, login):
        account_page = AccountPage(driver)
        account_page.check_account_page_open()
        assert account_page.check_element_is_visible(AccountPageLocators.PROFILE_BUTTON)
        assert account_page.check_element_is_visible(AccountPageLocators.HISTORY_BUTTON)

    @allure.title("Переход в раздел 'История заказов'")
    @allure.description("Проверка, что пользователь может перейти в 'Историю заказов' и видит завершённые заказы")
    def test_switch_to_orders_history(self, driver, login):
        account_page = AccountPage(driver)
        account_page.check_switch_to_orders_history()
        assert account_page.check_element_is_visible(AccountPageLocators.ORDER_COMPLETED_TEXT)
        assert account_page.check_element_is_visible(AccountPageLocators.HISTORY_BUTTON_ACTIVE)

    @allure.title("Выход из аккаунта")
    @allure.description("Проверка, что пользователь может выйти из аккаунта и элементы личного кабинета исчезают")
    def test_log_out(self, driver, login):
        account_page = AccountPage(driver)
        account_page.log_out()
        assert account_page.check_element_not_visible(AccountPageLocators.PROFILE_BUTTON)
