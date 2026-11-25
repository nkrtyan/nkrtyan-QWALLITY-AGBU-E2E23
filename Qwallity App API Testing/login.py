import requests
from requests.auth import HTTPBasicAuth
import endpoints
import data
import register_user
import logging


def test_login_user(username, password):
    logging.info("Starting user login")

    for attempt in range(10):
        try:
            login_response = requests.post(endpoints.login_endpoint, auth=HTTPBasicAuth(username = username, password = password))
            token = login_response.json().get('token')

            if token:
                logging.info(f"User logged in successfully")
                print("Login successfull.")
                data.headers['Authorization'] = f'Bearer {token}'
                break
            else:
                print(f"Status code: {login_response.status_code}, Response: {login_response.text}")
                logging.info(f"Status code: {login_response.status_code}, Response: {login_response.text}")


        except requests.RequestException as e:
            print(e)
            logging.info(f'Attempt{attempt + 1}: Login failed. Retrying... ')

    return data.headers

    
