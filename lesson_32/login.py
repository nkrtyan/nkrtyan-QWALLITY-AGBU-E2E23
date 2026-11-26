import requests
import endpoints
from requests.auth import HTTPBasicAuth
from register_user import test_register_user
import data



def test_login_user(username, password):
    try:
        # username, password = test_register_user()
        login_response = requests.post(endpoints.login_register_endpoint , auth=HTTPBasicAuth(username, password))
        token = login_response.json().get('token')
        if token:
            print('Login successful!')
            data.headers['Authorization'] = f'Bearer {token}'

    except requests.RequestException as e:
        print(e)
    return data.headers 



# if __name__ == '__main__':
#     test_login_user()