import requests
import endpoints
import data
import logging

def test_fill_balance(headers):
    for attempt in range(10):
        try:
            initial_response = requests.get(
                endpoints.account_balance_endpoint,
                headers=headers
            )
            if initial_response.status_code != 200:
                logging.info(f"Attempt {attempt + 1}: Failed to get initial balance.")
                continue

            initial_balance = int(initial_response.json().get("balance"))

            add_balance_response = requests.post(
                endpoints.fill_balance_endpoint,
                headers=headers,
                json=data.add_amount_body
            )

            if add_balance_response.status_code == 200:
                amount = data.add_amount_body["amount"]
                logging.info(f"Account balance added successfully: {amount}")

                updated_response = requests.get(
                    endpoints.account_balance_endpoint,
                    headers=headers
                )
                new_balance = int(updated_response.json().get("balance"))

                if new_balance == initial_balance + amount:
                    logging.info(f"Verified: Balance increased by {amount}! From {initial_balance} to {new_balance}")
                    return True
                else:
                    logging.error(f"Verification failed: Expected {initial_balance + amount}, but got {new_balance}")
                    return False
            else:
                logging.error(f"Attempt {attempt + 1}: Failed with status {add_balance_response.status_code}")

        except requests.exceptions.RequestException as e:
            logging.error(e)
            logging.error(f"Attempt {attempt + 1}: Request failed. Retrying...")


    return False

if __name__ == "__main__":
    test_fill_balance()