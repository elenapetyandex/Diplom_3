from selenium.webdriver.common.by import By

from locators.base_page_locators import BasePageLocators


class ForgotPasswordLocators(BasePageLocators):
    password_ap = [By.XPATH, ".//a[text()='Восстановить пароль']"]  # кнопка "Восстановить пароль"
    email_field_for_password_reset = [By.TAG_NAME, "input"] # Поле ввода почты в форме "Восстановление пароля"
    restore_button = [By.XPATH, ".//button[text()='Восстановить']"]  # кнопка "Восстановить" в форме "Восстановление пароля"
    password_reset_password_icon = [By.CLASS_NAME, "input__icon"]   # иконка сокрытия символов в поле "Пароль" в форме сброса пароля
    password_field = [By.XPATH, ".//label[text()='Пароль']"] # поле "Пароль" в форме сброса пароля
    password_field_active = [By.XPATH, ".//label[contains(@class, 'input__placeholder-focused')]"] # поле "Пароль" активно
    modal_window_reset_password = [By.CLASS_NAME, "Modal_modal__loading__3534A"]