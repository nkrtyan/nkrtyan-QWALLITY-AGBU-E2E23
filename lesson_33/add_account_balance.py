import endpoints
import data
import requests
from requests.auth import HTTPBasicAuth
import get_account_balance

def test_add_account_balance(headers):
    for attempt in range(10):
        try:
            add_balance_response = requests.post(endpoints.add_balance_endpoint, json=data.balance_body, headers=headers)
            if add_balance_response.status_code == 201:
                amount = data.balance_body["amount"]
                print(f"Account balance added successfully! Amount added: {amount}")

                new_balance = get_account_balance.test_get_account_balance(headers)
                print(f"New account balance: {new_balance}")

        except requests.RequestException as e:
            print(e)
            print(f"Attempt {attempt + 1}: Adding account balance failed. Retrying...")

    return add_balance_response.json().get("message")