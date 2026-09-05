from faker import Faker
import pytest
from api_methods.user_methods import UserMethods

faker = Faker()




@pytest.fixture
def random_user_data():
    email = faker.email(domain='yandex.ru')
    password = faker.password(length=6, special_chars=True, digits=True)
    name = faker.user_name()
    
    user_data = {
        'email': email,
        'password': password,
        'name': name
    }
    
    yield user_data
    
    try:
       
        login_response = UserMethods.login_user(user_data)
        
        if login_response.status_code == 200:
            token = login_response.json().get('accessToken')
            if token:
                UserMethods.delete_user(token)
    except Exception:
        pass