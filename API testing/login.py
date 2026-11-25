import requests
from requests.auth import HTTPBasicAuth
import endpoints
import data
import logging

def test_login_user(username, password):
    for attempt in range(10):
        try:
            login_response = requests.post(
                endpoints.login_endpoint, 
                auth=HTTPBasicAuth(username=username, password=password)
            )
            
            if login_response.status_code == 200:
                token = login_response.json().get('token')
                if token:
                    logging.info("Login successfully!")
                    logging.info("Token:", token)
                    data.headers['Authorization'] = f'Bearer {token}'
                    return data.headers
            else:
                logging.error(f"Login is failed with status code: {login_response.status_code}")
                
        except requests.exceptions.RequestException as e:
            logging.error(e)
            logging.error(f"Attempt {attempt + 1}: Login failed. Retrying...")

if __name__ == "__main__":
    test_login_user()