from api_methods.user_methods import UserMethods
import allure


class TestLoginUser:

    @allure.title("Логин под существующим пользователем")
    @allure.description("Проверка успешного логина пользователя, ответ 200 и success=true")
    def test_login_existence_user_succeed(self, created_user):


        response_login = UserMethods.login_user(created_user)
        
        assert response_login.status_code == 200
        assert response_login.json()['success'] is True
        assert 'accessToken' in response_login.json()
        assert 'refreshToken' in response_login.json()



    @allure.title("Логин c неверным логином")
    @allure.description("Проверка, что нельзя залогиниться, если ввести неверный логин(email), ответ 401 и success=false")
    def test_login_with_wrong_login_failed(self, random_user_data):
    
        user_data = random_user_data.copy()
            
        UserMethods.create_user(user_data)
    
        user_data['email'] = 'boruto@konoha.ru'
        response_login = UserMethods.login_user(user_data)
            
        assert response_login.status_code == 401
        assert response_login.json()['success'] is False
        assert 'email or password are incorrect' in response_login.json()['message'] 


    @allure.title("Логин c неверным паролем")
    @allure.description("Проверка, что нельзя залогиниться, если ввести неверный пароль, ответ 401 и success=false")
    def test_login_with_wrong_password_failed(self, random_user_data):
        
        user_data = random_user_data.copy()
                    
        UserMethods.create_user(user_data)
        
        user_data['password'] = 'Konoh@'
        response_login = UserMethods.login_user(user_data)
                    
                
        assert response_login.status_code == 401
        assert response_login.json()['success'] is False
        assert 'email or password are incorrect' in response_login.json()['message'] 
