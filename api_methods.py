import allure
import requests
from urls import Urls


class ApiMethods:
    @staticmethod
    @allure.step('Создать пользователя')
    def create_user(body):
        return requests.post(Urls.create_user_url, data=body)

    @staticmethod
    @allure.step('Логин пользователя')
    def login_user(body):
        return requests.post(Urls.login_url, data=body)

    @staticmethod
    @allure.step('Удалить пользователя')
    def delete_user(access_token):
        return requests.delete(Urls.delete_user, headers={'Authorization': access_token})

    @staticmethod
    @allure.step('Изменить данные пользователя')
    def patch_user(access_token, updated_data):
        return requests.patch(Urls.patch_user, headers={'Authorization': access_token}, data=updated_data)

    @staticmethod
    @allure.step('Создать заказ')
    def create_order(access_token, order_data):
        return requests.post(Urls.create_order, headers={'Authorization': access_token}, data=order_data)

    @staticmethod
    @allure.step('Получить заказ конкретного пользователя')
    def get_order_list(access_token):
        return requests.get(Urls.create_order, headers={'Authorization': access_token})
