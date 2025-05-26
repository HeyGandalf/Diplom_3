import allure
from pages.order_page import OrderPage


@allure.suite("Создание заказа")
class TestCreateOrder:

    @allure.title("Всплывающее окно с деталями заказа появляется при клике на заказ")
    @allure.description('Клик на заказ и проверка, что появилось всплывающее окно с деталями')
    def test_get_order_popup(self, driver, login):
        order_page = OrderPage(driver)
        popup_visible = order_page.click_order_and_check_pop_up()
        assert popup_visible, "Всплывающее окно с деталями заказа не появилось"

    @allure.title("Заказ из истории отображается на странице 'Лента заказов'")
    @allure.description('Создание заказа и проверка есть ли он в "Ленте заказов"')
    def test_find_order_in_list(self, driver, login):
        order_page = OrderPage(driver)
        order_found = order_page.check_order_is_on_orders_list()
        assert order_found, "Заказ не найден в 'Ленте заказов'"

    @allure.title("Счётчик 'Выполнено за всё время' увеличивается после нового заказа")
    @allure.description('Сверка счетчика заказов "Выполнено за все время"')
    def test_all_completed_orders_counter_grow(self, driver, login):
        order_page = OrderPage(driver)
        counter_grew = order_page.check_all_completed_orders_counter()
        assert counter_grew, "Счётчик 'Выполнено за всё время' не увеличился"

    @allure.title("Счётчик 'Выполнено за сегодня' увеличивается после нового заказа")
    @allure.description('Сверка счетчика заказов "Выполнено за сегодня"')
    def test_daily_orders_counter_grow(self, driver, login):
        order_page = OrderPage(driver)
        counter_grew = order_page.check_daily_orders_counter()
        assert counter_grew, "Счётчик 'Выполнено за сегодня' не увеличился"

    @allure.title("Оформленный заказ появляется в разделе 'В работе'")
    @allure.description('Получение номера нового заказа, и проверка, что номер заказа появился в разделе "В работе"')
    def test_new_order_appeears_in_work_list(self, driver, login):
        order_page = OrderPage(driver)
        order_in_work = order_page.check_new_order_appeears_in_work_list()
        assert order_in_work, "Оформленный заказ не появился в разделе 'В работе'"
