import allure
from pages.base_page import BasePage
from pages.main_page import MainPage
from helpers.urls import Urls


@allure.suite("Аккаунт пользователя")
class TestMainPage:

    @allure.title("Переход по клику на Конструктор")
    @allure.description("Проверка, что при клике на кнопку 'Конструктор' происходит переход на страницу сбора бургера.")
    def test_redirect_by_click_on_constructor(self, driver):
        base_page = BasePage(driver)
        base_page.open_page(Urls.LOGIN)
        main_page = MainPage(driver)
        main_page.click_constructor_and_check_redirect()

    @allure.title("Переход по клику на Лента заказов")
    @allure.description("Проверка, что при клике на кнопку 'Лента заказов' пользователь переходит на страницу со всеми заказами.")
    def test_redirect_by_click_on_orders_feed(self, driver):
        base_page = BasePage(driver)
        base_page.open_page(Urls.LOGIN)
        main_page = MainPage(driver)
        main_page.click_orders_and_check_redirect()

    @allure.title("Всплывающее окно с деталями ингредиента")
    @allure.description("Проверка, что при клике на ингредиент появляется всплывающее окно с его деталями.")
    def test_popup_of_ingredient(self, driver):
        base_page = BasePage(driver)
        base_page.open_page(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_ingredient_and_check_popup()

    @allure.title("Закрытие всплывающего окна ингредиента")
    @allure.description("Проверка, что всплывающее окно с деталями ингредиента закрывается при клике на крестик.")
    def test_close_ingredient_details_window(self, driver):
        base_page = BasePage(driver)
        base_page.open_page(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_close_pop_up()

    @allure.title("Увеличение счётчика после добавления ингредиента")
    @allure.description("Проверка, что счётчик ингредиента увеличивается после его добавления в заказ.")
    def test_counter_after_adding_ingredient(self, driver, login):
        main_page = MainPage(driver)
        main_page.add_ingredient_and_check_counter()

    @allure.title("Оформление заказа авторизованным пользователем")
    @allure.description("Проверка, что авторизованный пользователь может успешно оформить заказ.")
    def test_place_order(self, driver, login):
        main_page = MainPage(driver)
        main_page.place_order_and_check()
