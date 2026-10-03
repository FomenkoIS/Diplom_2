from api_methods.order_methods import OrderMethods
from api_methods.user_methods import UserMethods
import allure

from data import DataForOrder
from api_methods.user_methods import UserMethods
import allure



class TestCreateOrder:


    @allure.title("Создание заказа с авторизованным пользователем")
    @allure.description("Проверка успешного создания заказа с авторизованным пользователем, ответ 200 и success=true")
    def test_create_order_with_authorization_succeed(self, random_user_data):

        user_data = random_user_data
        UserMethods.create_user(user_data)

        login_response = UserMethods.login_user(user_data)
        token = login_response.json()['accessToken']

        ingreddients = DataForOrder.get_list_of_ingredients()
        order_data = {'ingredients': ingreddients[:3]}

            
        order_response = OrderMethods.create_order(order_data, token)
        assert order_response.status_code == 200, f"Expected status code 200, but got {order_response.status_code}"
        assert order_response.json()['success'] is True
        
        


    @allure.title("Создание заказа без авторизации пользователя")
    @allure.description("Проверка успешного создания заказа не авторизованным пользователем, ответ 200 и success=true")
    def test_create_order_without_authorization_succeed(self, random_user_data):
    
       
        ingreddients = DataForOrder.get_list_of_ingredients()
        order_data = {'ingredients': ingreddients[:3]}
    
                
        order_response = OrderMethods.create_order(order_data)
        assert order_response.status_code == 200, f"Expected status code 200, but got {order_response.status_code}"
        assert order_response.json()['success'] is True



    @allure.title("Создание заказа с 1 ингредиентом")
    @allure.description("Проверка успешного создания заказа с одним ингредиентом, ответ 200 и success=true")
    def test_create_order_with_one_ingredient_succeed(self, random_user_data):

        user_data = random_user_data
        UserMethods.create_user(user_data)

        login_response = UserMethods.login_user(user_data)
        token = login_response.json()['accessToken']
           
        ingreddients = DataForOrder.get_list_of_ingredients()
        order_data = {'ingredients': ingreddients[:1]}
        
                    
        order_response = OrderMethods.create_order(order_data, token)
        assert order_response.status_code == 200, f"Expected status code 200, but got {order_response.status_code}"
        assert order_response.json()['success'] is True



    @allure.title("Создание заказа без ингредиентов")
    @allure.description("без ингредиентов невозможно сделать заказ, ответ 400 и success=false")
    def test_create_order_without_ingredients_failed(self, random_user_data):

        user_data = random_user_data
        UserMethods.create_user(user_data)


        login_response = UserMethods.login_user(user_data)
        token = login_response.json()['accessToken']
                   
        order_data = {}
                
                            
        order_response = OrderMethods.create_order(order_data, token)
        assert order_response.status_code == 400, f"Expected status code 400, but got {order_response.status_code}"
        assert order_response.json()['success'] is False




    @allure.title("Создание заказа с неверным хэшем ингредиентов")
    @allure.description("Нельзя создать заказ с неверным хэшем ингредиентов, ответ 500")
    def test_create_order_with_invalid_hash_failed(self, random_user_data):
    
        user_data = random_user_data
        UserMethods.create_user(user_data)
    
    
        login_response = UserMethods.login_user(user_data)
        token = login_response.json()['accessToken']
                       
        order_data = {'ingredients': ['invalid_hash_1', 'invalid_hash_2', 'invalid_hash_3']}
                    
                                
        order_response = OrderMethods.create_order(order_data, token)
        assert order_response.status_code == 500, f"Expected status code 500, but got {order_response.status_code}"
        
