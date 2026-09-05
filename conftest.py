from faker import Faker
import pytest
from api_methods.user_methods import UserMethods

faker = Faker()




@pytest.fixture
def random_user_data():
    email = faker.email()
    password = faker.password(length=6, special_chars=True, digits=True)
    name = faker.name()
    
    user_data = {
        'email': email,
        'password': password,
        'name': name
    }
    
    yield user_data
    
    try:
       
        login_response = UserMethods.login_user(user_data)
        
        if login_response.status_code == 200:
            access_token = login_response.json().get('accessToken')
            if access_token:
                UserMethods.delete_user(access_token)
    except Exception:
        pass