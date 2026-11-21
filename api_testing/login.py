import requests
from requests.auth import HTTPBasicAuth
import endpoint
import data


def test_login_user(username, password):

    for attempt in range(10):
        try:
            login_response = requests.post(endpoint.login_endpoint,auth=HTTPBasicAuth(username, password), headers=data.headers)
            token = login_response.json().get("token")
            
            if token:
                print("User logged in successfully")
                print(login_response.json())
                data.headers["Authorization"] = f"Bearer {token}"
                break
    
        except requests.RequestException as e:
            print(e)
            print(f"Attempt {attempt + 1}: Login failed. Retrying...")
    return data.headers

if __name__ == "__main__":
    test_login_user(data.register_body["username"], data.register_body["password"])