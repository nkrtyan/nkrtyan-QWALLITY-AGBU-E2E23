import requests
from requests.auth import HTTPBasicAuth
import endpoint
import data


def test_login_user(username, password):
    login_data = {
        "username": username,
        "password": password
    }

    for attempt in range(10):
        try:
            login_response = requests.post(endpoint.login_endpoint,auth=HTTPBasicAuth(username, password), json=login_data, headers=data.headers)
            token = login_response.json().get("token")
            
            if token:
                print("User logged in successfully")
                print(login_response.json())
                print("Token - ", token)
                data.headers["Authorization"] = f"Bearer {token}"
                break
    
        except requests.RequestException as e:
            print(e)
            print(f"Attempt {attempt + 1}: Login failed. Retrying...")
    return data.headers

if __name__ == "__main__":
    test_login_user(username, password)