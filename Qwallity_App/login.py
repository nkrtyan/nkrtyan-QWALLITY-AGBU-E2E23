import requests
from requests.auth import HTTPBasicAuth
import endpoints
import data
import register_user


def test_login_user():
    for attempt in range(10):
        username, password = register_user.test_register_user()

        try:
            login_response = requests.post(endpoints.login_endpoint, auth=HTTPBasicAuth(username, password))
            token = login_response.json().get('token')

            if token:
                print("Login successfull.")
                data.headers['Authorization'] = f'Bearer {token}'
                break
        except requests.RequestException as e:
            print(e)
            print(f'Attempt{attempt + 1}: Login failed. Retrying... ')

    return data.headers

if __name__ == "__main__":
    test_login_user()
    
