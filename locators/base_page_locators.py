from selenium.webdriver.common.by import By


class BasePageLocators:
    modal_window = [By.CLASS_NAME, "Modal_modal__loading__3534A"]
    login_input = [By.TAG_NAME, "input"]  # форма заполнения страница логин

    lk_button = [By.LINK_TEXT, 'Личный Кабинет']  # кнопка "Личный Кабинет"
    constructor = [By.LINK_TEXT, 'Конструктор'] # Кнопка "крнструктор"
    logo = [By.XPATH, "//div/a/*"] # Логотип сайта на главной странице
    order_list_button = [By.LINK_TEXT, 'Лента Заказов']
    login_button = (By.XPATH, ".//button[text()='Войти']")  # кнопка "войти"

    def get_order_locator(self, order_number):
        order_number_in_form = f'#0{order_number}'
        xpath = f".//p[text()='{order_number_in_form}']"
        order_in_order_history = [By.XPATH, xpath]
        return order_in_order_history

