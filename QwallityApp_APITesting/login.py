import requests
from requests.auth import HTTPBasicAuth
import endpoint
import data
from logger import logger


def test_login_user(username, password):
    logger.info("Starting user login")

    for attempt in range(10):
        try:
            login_response = requests.post( 
            endpoint.login_endpoint, auth=HTTPBasicAuth(username, password), headers=data.headers)
            token = login_response.json().get("token")

            if token:
                logger.info("User logged in successfully")
                print("User logged in successfully")
                print(login_response.json())
                data.headers["Authorization"] = f"Bearer {token}"
                return data.headers
            else:
                logger.warning(
                    "Login attempt %s failed. Status code: %s",
                    attempt + 1,
                    login_response.status_code,
                )
                logger.error("Response: %s", login_response.text)
                print(f"Login failed. Status code: {login_response.status_code}")
                print("Response:", login_response.text)

        except requests.RequestException:
            logger.exception(
                "Attempt %s: Login request failed",
                attempt + 1,
            )
            print(f"Attempt {attempt + 1}: Login failed. Retrying login...")

    return data.headers


if __name__ == "__main__":
    test_login_user(data.register_body["username"], data.register_body["password"])