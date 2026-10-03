import requests
from url import URL
import allure

class IngredientsMethods:
    @staticmethod
    @allure.step("Получение списка ингредиентов")
    def get_ingredients():
        return requests.get(url = URL.LIST_OF_INGREDIENTS)
