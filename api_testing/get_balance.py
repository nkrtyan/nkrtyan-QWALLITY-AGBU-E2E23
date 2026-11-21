import endpoint
import data
import requests
from requests.auth import HTTPBasicAuth
import add_course_adv


def get_account_balance(header):
    for attempt in range(10):
        try:
            get_balance_response = requests.get(endpoint.get_balance_endpoint, headers=header)
            if get_balance_response.status_code == 200:
                balance = int(get_balance_response.json().get("balance"))
                print(f"Current account balance: {balance}")
                return balance
        
        except requests.RequestException as e:
            print(e)
            print(f"Attempt {attempt + 1}: Can't get account balance. Retrying...")