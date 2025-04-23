from locators.order_list_page_locators import OrderListPageLocators
from pages.base_page import BasePage


class OrderListPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderListPageLocators()

    def click_on_order_from_list(self, order_number):
        self.scroll_to_element(self.locators.get_order_locator(order_number))
        self.click_on_element(self.locators.get_order_locator(order_number))

    def check_order_modal_window(self):
        return self.wait_visibility_of_element(self.locators.order_modal_window)

    def check_order_in_order_list(self, order_number):
        self.scroll_to_element(self.locators.get_order_locator(order_number))
        return self.wait_visibility_of_element(self.locators.get_order_locator(order_number))

    def get_caunter_all_time_value(self):

        self.wait_visibility_of_element(self.locators.all_orders_counter)
        return self.get_text(self.locators.all_orders_counter)

    def get_list_orders_in_process(self):
        self.wait_visibility_of_element(self.locators.orders_in_process)
        orders_list = self.find_elements(self.locators.orders_in_process)
        orders_process_numbers = []
        for order in orders_list:
            text = order.text
            orders_process_numbers.append(text)

        return orders_process_numbers


    def get_today_order_counter_count(self):

        self.wait_visibility_of_element(self.locators.order_counter_today)

        element = self.find_element(self.locators.order_counter_today)
        return element.text



