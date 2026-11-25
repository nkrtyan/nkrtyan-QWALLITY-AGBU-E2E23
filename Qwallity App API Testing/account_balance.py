import endpoints
import requests
import data
import logging
import get_account_balance

def test_adding_account_balance(headers):
    initial_balance = get_account_balance.test_get_account_balance(headers)

    if initial_balance is False:
        logging.info("Cannot get initial account balance.")
        return False

    amount = data.account_data["amount"]
    card_number = data.account_data["card_num"]

    for attempt in range(10):

        try:
            account_balance_response = requests.post(endpoints.account_balance_endpoint, data.account_balance_body, headers=headers)

            if account_balance_response.status_code == 200: 
                logging.info(f"Account filled with amount {amount} from card {card_number}")

                new_balance = get_account_balance.test_get_account_balance(headers)

                if new_balance is False:
                    logging.info("Cannot get updated account balance.")
                    return False
                expected_balance = initial_balance + amount

                if new_balance == expected_balance:
                    logging.info("Balance verification passed.")
                    return True
                else:
                    logging.error(
                        f"Balance verification failed. "
                        f"Expected: {expected_balance}, Actual: {new_balance}"
                        )
                    return False

        except requests.RequestException as e:
            print(e) 
            logging.info(f"Attempt {attempt + 1}: Filling account balance failed.Retrying... ")

    return False            

