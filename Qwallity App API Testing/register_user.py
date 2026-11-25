import endpoints
import data
import requests
import logging


def test_register_user():
    logging.info("Starting user registration")
    register_data = data.register_body

    for attempt in range(10):
        try:
            register_user_response = requests.post(endpoints.register_endpoint, json=register_data, headers=data.headers)

            if register_user_response.status_code == 201:
                username = register_data["username"]
                password = register_data["password"]
                logging.info("User registered successfully")
                logging.info("Registration response: %s", register_user_response.json())
                print("User registered successfully!")
                print(register_user_response.json())
                print("Username - ", username)
                print("Password - ", password)
                return username, password
            else:
                logging.error("Response: %s, Status code: %s", register_user_response.text, register_user_response.status_code)
                print("Failed to register user. Status code:", register_user_response.status_code)
                print("Response:", register_user_response.text)
                break

        except requests.RequestException as e:
            print(e)
            logging.error(f"Attempt {attempt + 1}: Register failed. Retrying...")





