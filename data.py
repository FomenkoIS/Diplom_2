
from api_methods.ingredients_methods import IngredientsMethods



class DataForOrder:

    @staticmethod
    def get_list_of_ingredients():

        response = IngredientsMethods.get_ingredients()
        assert response.status_code == 200, "Не удалось получить ингредиенты"
        
        data = response.json()

        list_of_id = []
        for ingredient in data['data']:
            list_of_id.append(ingredient['_id'])
        return list_of_id
