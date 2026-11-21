import endpoint
import data
import requests
from requests.auth import HTTPBasicAuth
import get_balance

def add_account_balance(header):
    for attempt in range(10):
        try:
            add_balance_response = requests.post(endpoint.add_balance_endpoint, headers=header, json=data.balance_body)
            if add_balance_response.status_code == 200:
                amount = data.balance_body["amount"]     
                print(f"Account balance added successfully: {amount}")
                
                new_balance = get_balance.get_account_balance(header)
                return new_balance
                
            
        except requests.RequestException as e:
            print(e)
            print(f"Attempt {attempt + 1}: Adding account balance is failed. Retrying...")