import endpoints
import data
import requests

def test_register_user():
    register_data = data.register_body()

    for attempt in range(10):
        try:
            register_user_response = requests.post(endpoints.register_endpoint, json=register_data, headers=data.headers())

            if register_user_response.status_code == 201:
                username = register_data['username']
                password = register_data['password']
                print(f"User registered successfully!")
                print(register_user_response.json())
                print(f"Username: {username}")
                print(f"Password: {password}")
                return username, password
            else:
                print("Failed to register user. Status code:", register_user_response.status_code)
                print("Response:", register_user_response.text)
                break
        except requests.exceptions.RequestException as e:
            print(e)
            print(f"Attempt {attempt + 1}: Register  failed. Retrying...")

if __name__ == "__main__":
    test_register_user()
