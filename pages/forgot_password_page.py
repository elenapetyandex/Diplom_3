import allure

from locators.forgot_password_locators import ForgotPasswordLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ForgotPasswordLocators()



    @allure.step('Заполнить поле "Пароль" в форме "Восстановление пароля"')
    def fill_email_field_for_password_reset(self, email):
        self.wait_visibility_of_element(self.locators.email_field_for_password_reset)
        self.fill_input_field(self.locators.email_field_for_password_reset, email)

    @allure.step('нажать кнопку "Восстановить пароль" в форме "Вход"')
    def click_restore_password_button(self):
        self.wait_clickable_of_element(self.locators.password_ap)
        self.click_on_element(self.locators.password_ap)

    @allure.step('Нажать кнопку "Восстановить" в форрме "Восстановление пароля"')
    def click_restore_button(self):
        self.wait_clickable_of_element(self.locators.restore_button)
        self.click_on_element(self.locators.restore_button)

    @allure.step('Нажать иконку сокрытия пароля в поле "Пароль" формы "Восстановление пароля"')
    def click_icon_hide_password(self):
        self.wait_invisibility_of_element(self.locators.modal_window_reset_password)
        self.click_virt_mouse(self.locators.password_reset_password_icon)

    @allure.step('Найти поле "Пароль" в форме "Восстановление пароля"')
    def find_password_field(self):
        self.wait_visibility_of_element(self.locators.password_field)
        return self.find_element(self.locators.password_field)

    @allure.step('Найти активное поле "Пароль" в форме "Восстановление пароля"')
    def find_password_field_active(self):
        self.wait_visibility_of_element(self.locators.password_field_active)
        return self.find_element(self.locators.password_field_active)




