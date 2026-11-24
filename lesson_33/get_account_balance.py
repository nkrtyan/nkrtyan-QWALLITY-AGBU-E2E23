import endpoints
import data
import requests
from requests.auth import HTTPBasicAuth
import add_advance_course

def test_get_account_balance(headers):
    for attempt in range(10):
        try:
            get_balance_response = requests.get(endpoints.get_balance_endpoint, json=data.balance_body, headers=headers)
            if get_balance_response.status_code == 200:
                balance = get_balance_response.json().get("balance")
                print(f"Account balance retrieved successfully! Current balance: {balance}")
                break

        except requests.RequestException as e:
            print(e)
            print(f"Attempt {attempt + 1}: Retrieving account balance failed. Retrying...")

    return get_balance_response.json().get("message")
