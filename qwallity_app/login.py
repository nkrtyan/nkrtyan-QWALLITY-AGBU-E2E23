import requests
from requests.auth import HTTPBasicAuth
import endpoints
import data


def test_login_user(username, password):
    for attempt in range(10):

        try:
            login_response = requests.post(
                endpoints.login_endpoint, 
                auth=HTTPBasicAuth(username=username, password=password))
            
            if login_response.status_code == 200:
                token = login_response.json().get('token')

                if token:
                    print("Login successful.")
                    data.headers['Authorization'] = f'Bearer {token}'
                    break
            else:
                print(f"Login is failed with status code: {login_response.status_code}")

        except requests.RequestException as e:
            print(e)
            print(f"Attempt {attempt + 1}: Login failed. Retrying...")
        
    return data.headers

if __name__ == "__main__":
    test_login_user()