import allure

from data import Data
from pages.forgot_password_page import ForgotPasswordPage
from urls import Urls


class TestForgotPasswordPage:

    @allure.title('Переход на страницу восстановления пароля при клике на кнопку "Восстановить пароль"')
    def test_fill_registered_email_field_and_click_restore_button_go_to_forgot_password_page(self, driver):
        forgotpasswordpage = ForgotPasswordPage(driver)
        forgotpasswordpage.get_url(Urls.login_page_url)
        forgotpasswordpage.click_restore_password_button()
        assert forgotpasswordpage.get_current_url() == Urls.password_forgot_page

    @allure.title('Переход на страницу сброса пароля при клике на кнопку "Восстановить" при заполненном поле email')
    def test_fill_email_field_and_click_restore_password_button_go_to_reset_password_page(self, driver):
        forgotpasswordpage = ForgotPasswordPage(driver)
        forgotpasswordpage.get_url(Urls.login_page_url)
        forgotpasswordpage.click_restore_password_button()
        forgotpasswordpage.fill_email_field_for_password_reset(Data.user_email)
        forgotpasswordpage.click_restore_button()
        forgotpasswordpage.wait_url(Urls.password_reset_page)
        assert forgotpasswordpage.get_current_url() == Urls.password_reset_page

    @allure.title('Не происходит переход на страницу сброса пароля при клике на кнопку "Восстановить" при незаполненном поле email')
    def test_not_filled_email_and_click_restore_button_dont_go_to_reset_password_page(self, driver):
        forgotpasswordpage = ForgotPasswordPage(driver)
        forgotpasswordpage.get_url(Urls.login_page_url)
        forgotpasswordpage.click_restore_password_button()
        forgotpasswordpage.click_restore_button()
        forgotpasswordpage.wait_url(Urls.password_reset_page)
        assert not forgotpasswordpage.get_current_url() == Urls.password_reset_page

    @allure.title('Клик по иконке сокрытия пароля в поле "пароль" формы восстановления пароля делает его активным')
    def test_click_on_icon_hide_password_make_empty_field_password_active(self, driver):
        forgotpasswordpage = ForgotPasswordPage(driver)
        forgotpasswordpage.get_url(Urls.login_page_url)
        forgotpasswordpage.click_restore_password_button()
        forgotpasswordpage.fill_email_field_for_password_reset(Data.user_email)
        forgotpasswordpage.click_restore_button()
        forgotpasswordpage.wait_url(Urls.password_reset_page)
        element_password_field = forgotpasswordpage.find_password_field()
        forgotpasswordpage.wait_invisibility_of_element(forgotpasswordpage.locators.modal_window_reset_password)
        forgotpasswordpage.click_icon_hide_password()
        element_password_field_active = forgotpasswordpage.find_password_field_active()
        assert element_password_field == element_password_field_active

