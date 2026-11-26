
import endpoints 
import data
import requests


def register_user():
    register_user_response = data.register_body

    for attempt in range(3):
        try:
            register_user_response = requests.post(
                endpoints.register_endpoint,
                json=register_user_response,
                headers=data.headers
            )

            if register_user_response.status_code == 201:
                username = register_user_response.json()["username"]
                password = register_user_response.json()["password"]
                print("User registered successfully!")
                print(f"Username - {username}")
                print(f"Password - {password}")
                print(register_user_response.json())
                return

            else:
                print(f"Failed to register user. Status code: {register_user_response.status_code}")
                print(register_user_response.text)
                return

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            if attempt < 2:
                print(f"Attempt {attempt + 1}: Register failed. Retrying...")

if __name__ == "__main__":
    register_user()