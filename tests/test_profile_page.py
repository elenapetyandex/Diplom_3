import allure

from pages.profile_page import ProfilePage
from urls import Urls

@allure.feature('страница Личный кабинет.')
class TestProfilePage:
    @allure.title('При клике по кнопке главной страницы "Личный кабинет"  авторизованным пользователем происходит переход на страницу "Профиль".')
    def test_click_profile_logined_user_go_to_profile_page(self, driver, get_access_token):
        profilepage = ProfilePage(driver)

        profilepage.get_url(Urls.main_url)

        profilepage.wait_url(Urls.main_url)

        profilepage.click_on_profile_button()

        profilepage.wait_url(Urls.login_page_url)
        login_list = get_access_token
        email = login_list[0]
        password = login_list[1]
        profilepage.fill_login_input(email, password)
        profilepage.click_enter_button()
        profilepage.wait_url(Urls.main_url_authorized)
        profilepage.click_on_profile_button()
        profilepage.wait_url(Urls.profile_page_url)
        assert profilepage.get_current_url() == Urls.profile_page_url

    @allure.title('При клике по кнопке главной страницы "Личный кабинет" происходит переход на страницу "Вход".')
    def test_click_to_profile__unlogined_user_go_to_login_page(self, driver):
        profilepage = ProfilePage(driver)

        profilepage.get_url(Urls.main_url)

        profilepage.wait_url(Urls.main_url)

        profilepage.click_on_profile_button()

        profilepage.wait_url(Urls.login_page_url)

        assert profilepage.get_current_url() == Urls.login_page_url

    @allure.title('При клике на кнопку "История заказов" номер сделанного пользователем заказа появляется в истории заказов на странице профиля.')
    def test_order_number_in_order_history_when_user_made_order(self, driver, get_order_number):
        profilepage = ProfilePage(driver)

        profilepage.get_url(Urls.main_url)

        profilepage.wait_url(Urls.main_url)

        profilepage.click_on_profile_button()

        profilepage.wait_url(Urls.login_page_url)
        login_list = get_order_number
        email = login_list[0]
        password = login_list[1]
        profilepage.fill_login_input(email, password)
        profilepage.click_enter_button()
        profilepage.wait_url(Urls.main_url_authorized)
        profilepage.click_on_profile_button()
        profilepage.wait_url(Urls.profile_page_url)
        profilepage.click_order_history_button()
        assert profilepage.find_order_in_order_history(login_list[3])

    @allure.title('При клике на кнопку "История заказов" форма "Профиль" исчезает со страницы профиля')
    def test_go_to_order_history_form_when_user_have_not_order(self, driver, get_access_token):
        profilepage = ProfilePage(driver)

        profilepage.get_url(Urls.main_url)

        profilepage.wait_url(Urls.main_url)

        profilepage.click_on_profile_button()

        profilepage.wait_url(Urls.login_page_url)
        login_list = get_access_token
        email = login_list[0]
        password = login_list[1]
        profilepage.fill_login_input(email, password)
        profilepage.click_enter_button()
        profilepage.wait_url(Urls.main_url_authorized)
        profilepage.click_on_profile_button()
        profilepage.wait_url(Urls.profile_page_url)
        profilepage.click_order_history_button()
        assert profilepage.check_profile_form_invisible()

    @allure.title('При клике на кнопку "Выход" происходит переход со страницы профиля на страницу логина')
    def test_click_exit_button_go_to_login_page(self, driver, get_access_token):
        profilepage = ProfilePage(driver)

        profilepage.get_url(Urls.main_url)

        profilepage.wait_url(Urls.main_url)

        profilepage.click_on_profile_button()

        profilepage.wait_url(Urls.login_page_url)
        login_list = get_access_token
        email = login_list[0]
        password = login_list[1]
        profilepage.fill_login_input(email, password)
        profilepage.click_enter_button()
        profilepage.wait_url(Urls.main_url_authorized)
        profilepage.click_on_profile_button()
        profilepage.wait_url(Urls.profile_page_url)
        profilepage.log_out_from_profile()
        profilepage.wait_url(Urls.login_page_url)
        assert profilepage.get_current_url() == Urls.login_page_url

    @allure.title('При клике на кнопку "Конструктор" происходит переход  со страницы профиля на главную страницу')
    def test_click_constructor_from_profile_go_to_home_page(self,driver, get_access_token):
        profilepage = ProfilePage(driver)

        profilepage.get_url(Urls.main_url)

        profilepage.wait_url(Urls.main_url)

        profilepage.click_on_profile_button()

        profilepage.wait_url(Urls.login_page_url)
        login_list = get_access_token
        email = login_list[0]
        password = login_list[1]
        profilepage.fill_login_input(email, password)
        profilepage.click_enter_button()
        profilepage.wait_url(Urls.main_url_authorized)
        profilepage.click_on_profile_button()
        profilepage.wait_url(Urls.profile_page_url)
        profilepage.click_constroctor_button()
        profilepage.wait_url(Urls.main_url_authorized)
        assert  profilepage.get_current_url() == Urls.main_url_authorized

    @allure.title('При клике на кнопку "Лента заказов" происходит переход со страницы профиля на страницу заказов')
    def test_click_order_list_button_go_to_orders_page(self, driver, get_access_token):
        profilepage = ProfilePage(driver)
        profilepage.get_url(Urls.main_url)

        profilepage.wait_url(Urls.main_url)

        profilepage.click_on_profile_button()

        profilepage.wait_url(Urls.login_page_url)
        login_list = get_access_token
        email = login_list[0]
        password = login_list[1]
        profilepage.fill_login_input(email, password)
        profilepage.click_enter_button()
        profilepage.wait_url(Urls.main_url_authorized)
        profilepage.click_on_profile_button()
        profilepage.wait_url(Urls.profile_page_url)
        profilepage.click_order_list_button()
        profilepage.wait_url(Urls.order_list_page)
        assert profilepage.get_current_url() == Urls.order_list_page





