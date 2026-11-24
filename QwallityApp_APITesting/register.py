import endpoint
import data
import requests
from logger import logger


def test_register_user():
    register_data = data.register_body
    logger.info("Starting user registration")

    for attempt in range(10):
        try:
            register_user_response = requests.post(
                endpoint.register_endpoint, json=register_data, headers=data.headers
            )

            if register_user_response.status_code == 201:
                username = register_data["username"]
                password = register_data["password"]
                logger.info("User registered successfully")
                logger.info("Registration response: %s", register_user_response.json())
                print("User registered successfully")
                print(register_user_response.json())
                print("Username - ", username)
                print("Password - ", password)
                return username, password
            else:
                logger.warning(
                    "Attempt %s failed. Status code: %s",
                    attempt + 1,
                    register_user_response.status_code,
                )

                logger.error("Response: %s", register_user_response.text)

                print( "Failed to register user. Status code:", register_user_response.status_code,)
                print("Response", register_user_response.text)

        except requests.RequestException as e:
            logger.exception("Attempt %s: Register request failed", attempt + 1)
            print(f"Attempt {attempt + 1}: Register failed. Retrying registration...")

    return None


if __name__ == "__main__":
    test_register_user()