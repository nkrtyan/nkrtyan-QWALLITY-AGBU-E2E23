import endpoints
import requests
import data
import logging

def test_get_account_balance(headers):
    logging.info("Starting to get account balance.")

    for attempt in range(10):
        try:
            get_account_balance_response = requests.get(endpoints.get_account_balance_endpoint, headers=headers)

            if get_account_balance_response.status_code == 200:
                balance = int(get_account_balance_response.json().get("balance"))
                logging.info(f"Current account balance {balance}")
                return balance
            
            else:
                print(f"Error while trying get account balance. Status code: get_account_balance_response.status_code")
                return False

        except requests.RequestException as e:
            print(e) 
            logging.info("Attempt %s: Getting account balance failed. Retrying... ", attempt + 1)    
           