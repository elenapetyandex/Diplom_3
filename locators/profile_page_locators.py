from selenium.webdriver.common.by import By


from locators.base_page_locators import BasePageLocators


class ProfilePageLocators(BasePageLocators):
    reg_button = (By.LINK_TEXT, 'Зарегистрироваться') # кнопка "зарегистрироваться" в форме логин в форме регистрации

    login_reg = (By.XPATH,".//a[text()='Войти']") #кнопка  "Войти" в форме входа для зарегистрированных пользователей
    exit_button = [By.XPATH, ".//button[text()='Выход']"] # кнопка выход из аккаунта




    current_scroll = (By.XPATH,".//*[contains(@class, 'current')]") #



    homepage_buttons = (By.TAG_NAME, "button") # кнопки главной страницы



    reg_input = (By.TAG_NAME, "input") # форма ввода регистрации
    reg_button_2 = (By.XPATH, ".//button[text()='Зарегистрироваться']")# кнопка "зарегистрироваться" в форме логин в форме регистрации
    error_message = (By.XPATH, ".//p[@class='input__error text_type_main-default']") # сообщение о некорректном пароле
    soberite_burger = (By.XPATH, ".//h1[text()='Соберите бургер']")

    order_hystory_button = [By.XPATH, ".//a[text()='История заказов']"]
    order_from_order_history = [By.CLASS_NAME, "1111@mskghf.ru"]
    profile_form = [By.CLASS_NAME, "Profile_profile__3dzvr"]







