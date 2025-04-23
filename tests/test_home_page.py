import random
from time import sleep

import allure
import pytest

from conftest import driver
from data import Data
from pages.home_page import HomePage
from urls import Urls


class TestHomePage:
    @allure.title('Проверка перехода на страницу ленты заказов при клике на кнопку "Лента заказов"')
    def test_click_on_order_list_go_to_order_list_page(self, driver):
        homepage = HomePage(driver)
        homepage.get_url(Urls.main_url)
        homepage.click_order_list_button()
        homepage.wait_url(Urls.order_list_page)
        assert homepage.get_current_url() == Urls.order_list_page

    @allure.title('При клике на кнопку "Конструктор" перехода с главной страницы не происходит')
    def test_click_constructor_button_stay_homepage(self, driver):
        homepage = HomePage(driver)
        homepage.get_url(Urls.main_url)
        homepage.click_constroctor_button()
        assert homepage.get_current_url() == Urls.order_list_page

    @allure.title('При клике на ингредиент в форме"Соберите бургер" появляется окно "Детали ингредиента".')
    def test_click_on_ingredient_call_modal_window(self, driver):
        homepage = HomePage(driver)
        homepage.get_url(Urls.main_url)
        homepage.wait_url(Urls.main_url)
        homepage.click_ingredient_in_constructor(Data.ingredients_names[7])
        assert homepage.check_modal_window_appear()

    @allure.title('При клике на крестик в окне "Детали ингредиент" окно исчезает.')
    def test_close_modal_ingredient_window_window_closed(self, driver):
        homepage = HomePage(driver)
        homepage.get_url(Urls.main_url)
        homepage.wait_url(Urls.main_url)
        homepage.click_ingredient_in_constructor(Data.ingredients_names[7])
        assert homepage.close_modal_window()

    @allure.title('При перетаскивании ингредиента из формы "Соберите бургер" в форму конструктор бургера, каунтер ингридиента увеличивается')
    def test_add_ingredient_from_constructor_get_count_add_ingredient(self, driver, get_access_token):
        homepage = HomePage(driver)
        homepage.get_url(Urls.main_url)
        homepage.wait_url(Urls.main_url)
        homepage.click_on_profile_button()

        homepage.wait_url(Urls.login_page_url)
        login_list = get_access_token
        email = login_list[0]
        password = login_list[1]
        homepage.fill_login_input(email, password)
        homepage.click_enter_button()
        homepage.wait_url(Urls.main_url_authorized)
        homepage.drag_ingredient_from_constructor_to_burger_constructor(Data.ingredients_names[7])
        sleep(5)

    @allure.title('При перетаскивании ингредиента из формы "Соберите бургер" в форму конструктор бургера, каунтер ингридиента увеличивается на количество перетаскиваний')
    @pytest.mark.parametrize('count_ingredient', [1, 2, 5])
    def test_add_ingredient_from_constructor_get_count_add_ingredient1(self, driver, get_access_token, count_ingredient):
        homepage = HomePage(driver)
        homepage.get_url(Urls.main_url)
        homepage.wait_url(Urls.main_url)
        homepage.click_on_profile_button()

        homepage.wait_url(Urls.login_page_url)
        login_list = get_access_token
        email = login_list[0]
        password = login_list[1]
        homepage.fill_login_input(email, password)
        homepage.click_enter_button()
        homepage.wait_url(Urls.main_url_authorized)
        for _ in range (count_ingredient):
            homepage.drag_ingredient_by_link(Data.ingredients_id[5])
        assert homepage.check_count_ingredients(Data.ingredients_id[5]) == str(count_ingredient)

    def test_logined_user_can_make_order(self,driver, get_access_token):
        homepage = HomePage(driver)
        homepage.get_url(Urls.main_url)
        homepage.wait_url(Urls.main_url)
        homepage.click_on_profile_button()

        homepage.wait_url(Urls.login_page_url)
        login_list = get_access_token
        email = login_list[0]
        password = login_list[1]
        homepage.fill_login_input(email, password)
        homepage.click_enter_button()
        homepage.wait_url(Urls.main_url_authorized)
        homepage.drag_ingredient_by_link(random.choice(Data.ingredients_id))
        homepage.drag_ingredient_by_link(random.choice(Data.ingredients_id))
        homepage.drag_ingredient_by_link(random.choice(Data.ingredients_id))
        assert homepage.check_modal_window_order_id_appear()
