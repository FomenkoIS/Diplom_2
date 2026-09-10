import requests
from url import URL
import allure

class OrderMethods:
    @staticmethod
    @allure.step("Создать заказ с данными: {body}")
    def create_order(body, token=None):
        if token:
            body['authorization'] = token 
        return requests.post(url = URL.ORDER_CREATE_ENDPOINT, json=body)



