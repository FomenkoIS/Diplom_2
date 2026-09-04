import requests
from url import URL
import allure

class UserMethods:

    @staticmethod
    @allure.step("Создать курьера с данными: {body}")
    def create_user(body):
        return requests.post(url = URL.COURIER_CREATE_ENDPOINT, json=body)
    
    @staticmethod
    @allure.step("Выполнить вход курьера с данными: {body}")
    def login_user(body):
        return requests.post(url = URL.COURIER_LOGIN_ENDPOINT, json=body)
    
    @staticmethod
    @allure.step("Удалить курьера с ID: {courier_id}")
    def delete_user(courier_id):
        return requests.delete(f"{URL.DELETE_COURIER_ENDPOINT}/{courier_id}")
