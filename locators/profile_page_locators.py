from selenium.webdriver.common.by import By




class ProfilePageLocators:
    reg_button = [By.LINK_TEXT, 'Зарегистрироваться'] # кнопка "зарегистрироваться" в форме логин в форме регистрации

    login_reg = (By.XPATH,".//a[text()='Войти']") #кнопка  "Войти" в форме входа для зарегистрированных пользователей
    exit_button = [By.XPATH, ".//button[text()='Выход']"] # кнопка выход из аккаунта

    current_scroll = (By.XPATH,".//*[contains(@class, 'current')]") #

    reg_button_2 = (By.XPATH, ".//button[text()='Зарегистрироваться']")# кнопка "зарегистрироваться" в форме логин в форме регистрации

    order_hystory_button = [By.XPATH, ".//a[text()='История заказов']"]
    order_from_order_history = [By.CLASS_NAME, "1111@mskghf.ru"]
    profile_form = [By.CLASS_NAME, "Profile_profile__3dzvr"]







