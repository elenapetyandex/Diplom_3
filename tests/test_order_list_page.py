from time import sleep

import allure

from pages.order_list_page import OrderListPage
from urls import Urls


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

    def test_counter_value_increase_with_creating_order(self, driver, get_order_number):
        ordelistpage = OrderListPage(driver)
        ordelistpage.get_url(Urls.order_list_page)
        ordelistpage.wait_url(Urls.order_list_page)
        counter_before = ordelistpage.get_caunter_all_time_value()
        new_order = get_order_number
        print(new_order[3])
        counter_after = ordelistpage.get_caunter_all_time_value()
        assert counter_after > counter_before

    def test_order_is_in_process_when_create_order(self, driver, get_order_number):
        ordelistpage = OrderListPage(driver)
        ordelistpage.get_url(Urls.main_url)
        ordelistpage.wait_url(Urls.main_url)
        new_order = get_order_number
        order_string = f'0{new_order[3]}'
        #sleep(3)
        ordelistpage.click_order_list_button()
        ordelistpage.wait_url(Urls.order_list_page)
        orders_in_process = ordelistpage.get_list_orders_in_process(new_order[3])
        #sleep(3)
        assert order_string in orders_in_process

    def test_counter_today_get_add_orders(self, driver, get_order_number):
        ordelistpage = OrderListPage(driver)
        ordelistpage.get_url(Urls.order_list_page)
        ordelistpage.wait_url(Urls.order_list_page)
        new_order = get_order_number
        order_string = f'0{new_order[3]}'


