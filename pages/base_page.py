import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_locators = BasePageLocators()
    @allure.step('Обнаружить элемент')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Кликнуть элемент')
    def click_on_element(self, locator):
        element = self.find_element(locator)
        element.click()

    @allure.step('Дождаться видимости элемента')
    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Дождаться невидимости элемента')
    def wait_invisibility_of_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step('Дождаться кликабельности элемента')
    def wait_clickable_of_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Прокрутить до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Перетащить элемент')
    def move_element(self, locator_source, locator_target):
        source = self.find_element(locator_source)
        target = self.find_element(locator_target)
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).pause(5).perform()

    @allure.step('Заполнить поле')
    def fill_input_field(self, locator, input):
        self.find_element(locator).send_keys(input)

    @allure.step('Очистить поле')
    def clear_field(self, locator):
        self.find_element(locator).clear()

    @allure.step('Получить текущий адрес')
    def get_current_url (self):
        current_url = self.driver.current_url
        return current_url

    @allure.step('Подождать загрузки адреса')
    def wait_url(self, url):
        return WebDriverWait(self.driver, 5).until(expected_conditions.url_contains(url))

    @allure.step('Открыть адрес страницы')
    def get_url(self, url):
        self.driver.get(url)

    @allure.step('Перетащить элемент')
    def move_element(self, locator_source, locator_target):
        source = self.driver.find_element(*locator_source)
        target = self.driver.find_element(*locator_target)
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).pause(5).perform()

    @allure.step('Кликнуть в обход перекрывающего окна')
    def click_virt_mouse(self, locator):
        action = ActionChains(self.driver)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        action.click(on_element=element).perform()

    @allure.step('Обнаружить элементы')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Кликнуть кнопку "конструктор"')
    def click_constroctor_button(self):
        self.wait_invisibility_of_element(self.base_locators.modal_window)
        self.wait_clickable_of_element(self.base_locators.constructor)
        self.click_on_element(self.base_locators.constructor)

    @allure.step('Кликнуть кнопку "Лента заказов"')
    def click_order_list_button(self):
        self.wait_invisibility_of_element(self.base_locators.modal_window)
        self.wait_clickable_of_element(self.base_locators.order_list_button)
        self.click_on_element(self.base_locators.order_list_button)

    @allure.step('Кликнуть кнопку Личный Кабинет')
    def click_on_profile_button(self):
        self.wait_invisibility_of_element(self.base_locators.modal_window)
        self.wait_clickable_of_element(self.base_locators.lk_button)
        self.click_on_element(self.base_locators.lk_button)

    @allure.step('Заполнить поле логин')
    def fill_login_input(self, email, password):
        self.click_on_profile_button()
        elements = self.find_elements(self.base_locators.login_input)
        for element in elements:
            element.clear()
        elements[0].send_keys(email)
        elements[1].send_keys(password)

    @allure.step('Нажать кнопку "Войти"')
    def click_enter_button(self):
        self.wait_clickable_of_element(self.base_locators.login_button)
        self.click_on_element(self.base_locators.login_button)

    @allure.step('Получить текс элемента')
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    @allure.step('Обновить страницу')
    def refresh(self):
        self.driver.refresh()

    @allure.step('Прокрутить до элемента')
    def scroll_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)