from selenium.webdriver.common.by import By

from locators.base_page_locators import BasePageLocators


class OrderListPageLocators:
    orders_list = [By.CLASS_NAME, 'OrderFeed_list__OL59'] # список заказов на странице "Лента заказов"
    order_from_list = [By.XPATH, ".//ul[@class='OrderFeed_list__OL59']/li"] # узлы списка заказов
    order_number_from_list = [By.XPATH, ".//ul[@class='OrderFeed_list__OL59']/li/a/div/p[@class='text_type_digits-default"] # элемент с номером заказа
    order_modal_window = [By.XPATH, ".//section[contains(@class, 'Modal_modal_opened__3ISw4')]"] # Окно с информацией о заказе
    all_orders_counter = [By.CSS_SELECTOR, 'p.OrderFeed_number__2MbrQ.text.text_type_digits-large'] # Счетчик заказов "Выполнено за все время"
    orders_in_process = [By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li"] # список заказов в работе
    all_orders_are_ready = [By.XPATH, ".//*[text()='Все текущие заказы готовы!']"] # Подпись под "В работе"

    order_in_process = [By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[2]"]
    order_counter_today = [By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p"]