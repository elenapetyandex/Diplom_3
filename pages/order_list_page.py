from locators.order_list_page_locators import OrderListPageLocators
from pages.base_page import BasePage
import allure


class OrderListPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderListPageLocators()
    @allure.step('Кликнуть на заказ из блока "Лента заказов".')
    def click_on_order_from_list(self, order_number):
        self.scroll_to_element(self.base_locators.get_order_locator(order_number))
        self.click_on_element(self.base_locators.get_order_locator(order_number))

    @allure.step('Дождаться появления модального окна с подробностями о выбранном заказе из блока "Лента заказов". ')
    def check_order_modal_window(self):
        return self.wait_visibility_of_element(self.locators.order_modal_window)

    @allure.step('Дождаться появления заказа в блоке "Лента заказов"')
    def check_order_in_order_list(self, order_number):
        self.scroll_to_element(self.base_locators.get_order_locator(order_number))
        return self.wait_visibility_of_element(self.base_locators.get_order_locator(order_number))

    @allure.step('Получить число заказов из счетчика заказов "За все время".')
    def get_caunter_all_time_value(self):

        self.wait_visibility_of_element(self.locators.all_orders_counter)
        return self.get_text(self.locators.all_orders_counter)


    @allure.step('Получить номера заказов из списка заказов "В процессе".')
    def get_list_orders_in_process(self):

        self.wait_visibility_of_element(self.locators.orders_in_process)
        self.wait_invisibility_of_element(self.locators.all_orders_are_ready)
        orders_list = self.find_elements(self.locators.orders_in_process)

        orders_process_numbers = []
        for order in orders_list:
            text = order.text
            orders_process_numbers.append(text)
        print(orders_process_numbers)
        return orders_process_numbers

    @allure.step('Получить число заказов из счетчика заказов "За сегодня".')
    def get_today_order_counter_count(self):

        self.wait_visibility_of_element(self.locators.order_counter_today)

        element = self.find_element(self.locators.order_counter_today)
        return element.text

    def find_first_ready_order(self):
        self.wait_visibility_of_element(self.locators.ready_order_locator())
        element = self.find_element(self.locators.ready_order_locator())
        return element.text


