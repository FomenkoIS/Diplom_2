import requests
from url import URL
import allure

class UserMethods:

    @staticmethod
    @allure.step("Создать пользователя с данными: {body}")
    def create_user(body):
        return requests.post(url = URL.USER_CREATE_ENDPOINT, json=body)
    
    @staticmethod
    @allure.step("Авторизация пользоветеля с данными: {body}")
    def login_user(body):
        return requests.post(url = URL.USER_LOGIN_ENDPOINT, json=body)
    
    @staticmethod
    @allure.step("Удаление пользовтеля с данными: {courier_id}")
    def delete_user(body):
        return requests.delete(url = URL.DELETE_USER_ENDPOINT, json=body)
