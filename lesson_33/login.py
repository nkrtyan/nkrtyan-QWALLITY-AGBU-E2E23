import requests
import endpoints
import data
from requests.auth import HTTPBasicAuth

def test_login_user(username, password):
    for attempt in range(10):
        try:
            login_response = requests.post(endpoints.login_endpoint, auth=HTTPBasicAuth(username = username, password = password))
            token = login_response.json().get('token')

            if token:
                print("loggin successfully!")
                print("Token:", token)
                data.headers['Authorization'] = f'Bearer {token}'
                break

        except requests.exceptions.RequestException as e:
            print(e)
            print(f"Attempt {attempt + 1}: Login failed. Retrying...")

    return data.headers

if __name__ == "__main__":
    test_login_user()