from selenium.webdriver.common.by import By

from locators.base_page_locators import BasePageLocators


class HomePageLocators(BasePageLocators):
    switch_bulki = [By.XPATH, ".//span[text()='Булки']/parent::*"]  #
    switch_nachinki = [By.XPATH, ".//span[text()='Начинки']/parent::*"]  #
    ingredients = [By.XPATH,".//ul[@class='BurgerIngredients_ingredients__list__2A-mT']"]  # все ингридиенты в конструкторе. 0 - булки, 1- соусы, 2 - начинки
    switch_souses = (By.XPATH, ".//span[text()='Соусы']/parent::*")  # кнопка конструктора "Соусы"
    souses_img = (By.XPATH, ".//img[contains(@alt, 'Соус')]")  # соусы в конструкторе картинки
    bulki_img = (By.XPATH, ".//img[contains(@alt, ' ,булка')]")  # картинки булок в конструкторе
    meat_img = (By.XPATH, ".//img[contains(@alt, ' ,булка')]")  # картинка мясо в конструкторе
    ingredient_modal_window = [By.XPATH, ".//*[text()='Детали ингредиента']"] # всплывающее окно с деталями ингредиента
    modal_close = [By.XPATH,".//*[contains(@class, 'Modal_modal__close_modified__3V5XS')]"] # крестик закрытия в окне "Детали ингредиента"
    burger_constructor = [By.CLASS_NAME, 'BurgerConstructor_basket__list__l9dp_'] #конструктор бургера для заказа
    make_order_button = [By.XPATH, ".//button[text()='Оформить заказ']"] # кнопка "оформить заказ" под конструктом бургера
    modal_window_order_id = [By.XPATH, ".//p[text()='идентификатор заказа']"]  # модальное окно "идентификатор заказа"






    def get_ingredient_locator(self, ingredient):

        xpath = f".//*[text()='{ingredient}']"
        ingredient_locator = [By.XPATH, xpath]
        return ingredient_locator

    def get_ingredient_by_href(self, ingredient_id):
        xpath = f"/ingredient/{ingredient_id}"
        ingredient_locator = [By.XPATH, f".//a[@href='{xpath}']"]
        return ingredient_locator

    def get_counter_locator(self, ingredient_id):
        xpath = f"/ingredient/{ingredient_id}"

        xpath_1 = f".//a[@href='{xpath}']/div/p"
        counter_locator = [By.XPATH, xpath_1]
        return counter_locator