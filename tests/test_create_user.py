
from api_methods.user_methods import UserMethods
import allure



class TestCreateUser:


    @allure.title("Создание уникального пользователя")
    @allure.description("Проверка успешного создания курьера с логином Bam")
    def test_create_unique_user_succeed(self, random_user_data):

        user_data = random_user_data

        response = UserMethods.create_user(user_data)

        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        assert response.json()['success'] is True
        assert 'accessToken' in response.json()
        assert 'refreshToken' in response.json()
        

    @allure.title("Создание пользователя, который уже зарегистрирован")
    @allure.description("Проверка, что при повторной регистрации возвращается 403 и success=false")
    def test_create_user_already_exists_failed(self, random_user_data):


        user_data = random_user_data
        response_1 = UserMethods.create_user(user_data)
        assert response_1.status_code == 200, "Первый пользователь не создался"

        response_2 = UserMethods.create_user(user_data)
        assert response_2.status_code == 403, f"Expected status code 403, but got {response_2.status_code}"
        assert response_2.json()['success'] is False


    @allure.title("создать пользователя, если не заполнить поле Логин(name)")
    @allure.description("Проверка, что если не заполнить обязательное поле Логин возвращается 401 и success=false")
    def test_create_user_without_name_failed(self, random_user_data):

        user_data = random_user_data.copy()
        del user_data['name']

        response= UserMethods.create_user(user_data)
      
        assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"
        assert response.json()['success'] is False




    @allure.title("создать пользователя, если не заполнить поле Пароль")
    @allure.description("Проверка, что если не заполнить обязательное поле Пароль возвращается 401 и success=false")
    def test_create_user_without_password_failed(self, random_user_data):
            
        user_data = random_user_data.copy()
        del user_data['password']
        
        response= UserMethods.create_user(user_data)
              
        assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"
        assert response.json()['success'] is False