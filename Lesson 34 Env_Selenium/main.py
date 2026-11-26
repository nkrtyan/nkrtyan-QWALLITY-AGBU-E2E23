import os
from facebook import login_test
import logging
import log


if __name__ == "__main__":

    logging.info("Starting test")
    logging.basicConfig()

    username = os.environ.get("my_username")
    password = os.environ.get("my_pass")

    login_test(username, password)

    logging.info("Test finished!")
