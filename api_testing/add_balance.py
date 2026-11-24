import endpoint
import data
import requests
from requests.auth import HTTPBasicAuth
import get_balance

def add_account_balance(header):
    initial_balance = get_balance.get_account_balance(header)

    if initial_balance is False: 
        logger.error("Cannot get initial account balance.")
        return False

    amount = data.balance_body["amount"]
    
    for attempt in range(10):
        try:
            add_balance_response = requests.post(endpoint.add_balance_endpoint, headers=header, json=data.balance_body)
            if add_balance_response.status_code == 200:    
                print(f"Account balance added successfully: {amount}")
                new_balance = get_balance.get_account_balance(header)
                
                if new_balance is False:
                    print("Can not get updated account balance.")
                    return False
                
                expected_balance = initial_balance + amount
                
                if new_balance == expected_balance:
                    print("Balance verification passed.")
                    return True
                else:
                    print(
                        f"Balance verification failed. "
                        f"Expected: {expected_balance}, Actual: {new_balance}"
                    )
                    return False
            else:
                print(
                    f"Failed to add balance. Status code: "
                    f"{add_balance_response.status_code}"
                )
                return False   
        except requests.RequestException as e:
            print(e)
            print(f"Attempt {attempt + 1}: Adding account balance is failed. Retrying...")