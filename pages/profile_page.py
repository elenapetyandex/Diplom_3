import allure

from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProfilePageLocators()


    @allure.step('Кликнуть на кнопку "История заказов" и дождаться перехода с формы "Профиль"')
    def click_order_history_button(self):
        self.wait_invisibility_of_element(self.base_locators.modal_window)
        self.wait_clickable_of_element(self.locators.order_hystory_button)
        self.click_on_element(self.locators.order_hystory_button)
        self.wait_invisibility_of_element(self.locators.profile_form)

    @allure.step('Найти заказ по номеру заказа в ленте "История заказов".')
    def find_order_in_order_history(self, order_number):
        locator = self.base_locators.get_order_locator(order_number)

        return self.wait_visibility_of_element(locator)

    @allure.step('Нажать кнопку "Выход" в форме "Профиль".')
    def log_out_from_profile(self):
        self.wait_invisibility_of_element(self.base_locators.modal_window)
        self.wait_clickable_of_element(self.locators.exit_button)
        self.click_on_element(self.locators.exit_button)

    @allure.step('Дождаться исчезновения формы "Профиль".')
    def check_profile_form_invisible(self):
        return self.wait_invisibility_of_element(self.locators.profile_form)




