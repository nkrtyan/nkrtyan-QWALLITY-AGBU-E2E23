import endpoint
import data
import requests
import logging

logger = logging.getLogger(__name__)


def get_account_balance(header):
    logger.info("Starting to get account balance.")

    for attempt in range(10):
        try:
            logger.info(f"Attempt {attempt + 1}: Getting account balance.")
            get_balance_response = requests.get(endpoint.get_balance_endpoint, headers=header)

            if get_balance_response.status_code == 200:
                balance = int(get_balance_response.json().get("balance"))
                logger.info(f"Current account balance: {balance}")
                return balance

            else:
                logger.error(
                    f"Failed to get account balance. "
                    f"Status code: {get_balance_response.status_code}"
                )
                return False

        except requests.RequestException:
            logger.exception(
                f"Attempt {attempt + 1}: Can't get account balance. Retrying..."
            )

    logger.error("Failed to get account balance after 10 attempts.")
    return False
