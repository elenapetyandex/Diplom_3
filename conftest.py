import random

import pytest
from selenium import webdriver

from api_methods import ApiMethods
from data import Data



@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser = None
    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()
    yield browser
    browser.quit()



@pytest.fixture
def get_access_token():
    email = Data.user_email
    password = Data.user_password
    name = Data.user_name
    body = {
        "email": email,
        "password": password,
        "name": name
    }
    ApiMethods.create_user(body)
    body_1 = {
        "email": email,
        "password": password
    }
    response_login = ApiMethods.login_user(body_1)

    login_list = []
    if response_login.status_code == 200:
        login_list.append(email)
        login_list.append(password)
    access_token = response_login.json().get("accessToken")

    login_list.append(access_token)
    yield login_list
    ApiMethods.delete_user(access_token)


@pytest.fixture
def get_order_number(get_access_token):
    login_list = get_access_token
    access_token = login_list[2]
    order_data = {
        "ingredients": []
    }
    ingredient_list = []
    ingredient_list.append(random.choice(Data.ingredients_id))
    ingredient_list.append(random.choice(Data.ingredients_id))
    for ingredient in ingredient_list:
        order_data["ingredients"].append(ingredient)
    response = ApiMethods.create_order(access_token, order_data)
    order_number = response.json()["order"]["number"]

    login_list.append(order_number)
    yield login_list
    ApiMethods.delete_user(access_token)



