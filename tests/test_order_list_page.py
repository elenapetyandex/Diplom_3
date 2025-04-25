from time import sleep

import allure

from pages.order_list_page import OrderListPage
from urls import Urls

@allure.feature('страница "Лента заказов".')
class TestOrderListPage:
    @allure.title('Проверка появления модального окна с информацией о заказе при клике на заказ в ленте заказов')
    def test_click_on_order_get_modal_window(self, driver, get_order_number): #
        ordelistpage = OrderListPage(driver)
        ordelistpage.get_url(Urls.main_url)
        login_list = get_order_number
        order_number = login_list[3]
        ordelistpage.click_order_list_button()
        ordelistpage.wait_url(Urls.order_list_page)
        ordelistpage.click_on_order_from_list(order_number)
        assert ordelistpage.check_order_modal_window()

    @allure.title('Проверка отображения созданного заказа в ленте заказов')
    def test_orders_from_history_in_order_list(self, driver, get_order_number):  # отображение заказа в истории заказов проверяется в test_profile_page
        ordelistpage = OrderListPage(driver)
        ordelistpage.get_url(Urls.main_url)
        login_list = get_order_number
        order_number = login_list[3]
        ordelistpage.click_order_list_button()
        ordelistpage.wait_url(Urls.order_list_page)
        assert ordelistpage.check_order_in_order_list(order_number)

    @allure.title('Проверка увеличения числа счетчика заказов "Выполнено за все время" при создании заказа')
    def test_counter_value_increase_with_creating_order(self, driver, get_order_number):
        ordelistpage = OrderListPage(driver)
        ordelistpage.get_url(Urls.order_list_page)
        counter_before = ordelistpage.get_caunter_all_time_value()
        new_order = get_order_number
        order_number = new_order[3]
        ordelistpage.refresh()
        ordelistpage.wait_url(Urls.order_list_page)

        counter_after = ordelistpage.get_caunter_all_time_value(order_number)
        assert counter_after > counter_before

    @allure.title('Проверка появления номера заказа в списке "В работе" при создании заказа')
    def test_order_is_in_process_when_create_order(self, driver, get_order_number):
        ordelistpage = OrderListPage(driver)
        ordelistpage.get_url(Urls.main_url)
        ordelistpage.wait_url(Urls.main_url)
        new_order = get_order_number
        order_string = f'0{new_order[3]}'

        ordelistpage.click_order_list_button()
        ordelistpage.wait_url(Urls.order_list_page)
        ordelistpage.refresh()

        orders_in_process = ordelistpage.get_list_orders_in_process()

        assert order_string in orders_in_process

    @allure.title('Проверка увеличения числа счетчика заказов "выполнено за сегодня" при создании заказа')
    def test_counter_today_get_add_orders(self, driver, get_order_number):
        ordelistpage = OrderListPage(driver)
        ordelistpage.get_url(Urls.order_list_page)
        ordelistpage.wait_url(Urls.order_list_page)
        count_before = ordelistpage.get_today_order_counter_count()
        new_order = get_order_number
        order_string = f'0{new_order[3]}'
        count_after = ordelistpage.get_today_order_counter_count()
        assert count_after > count_before

