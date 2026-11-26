from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import logging
import requests


def login_test(username, password):

    driver = webdriver.Chrome()
    driver.maximize_window()

    for attempt in range(10):
        try:
            driver.get("https://www.facebook.com")

            username_field = driver.find_element(By.NAME, "email")
            password_field = driver.find_element(By.NAME, "pass")
            submit = driver.find_element(By.XPATH, '//*[@id="login_form"]/div/div[1]/div/div[3]/div/div/div')

            if username_field == os.environ.get("my_username") and password_field == os.environ.get("my_pass"):
                logging.info("Login done successfully! ")
            elif username_field != os.environ.get("my_username") and password_field == os.environ.get("my_pass"):
                logging.warning("Please enter a valid username.")
            elif username_field == os.environ.get("my_username") and password_field != os.environ.get("my_pass"):
                logging.warning("Please enter a valid password.")
            elif username_field != os.environ.get("my_username") and password_field != os.environ.get("my_pass"): 
                logging.warning("Please enter a valid credentials for username and password.")
            else:
                logging.warning("Unknown error.")

            username_field.send_keys(username)
            password_field.send_keys(password)
            time.sleep(3)

            submit.click()
            time.sleep(10)

            
            logging.info("Test log in to Facebook done successfully!")
            print("Test log in to Facebook done successfully!")

        except requests.RequestException as e:
            print(e)
            logging.info('Attempt %s: Log in failed. Retrying...', attempt + 1)
            
    driver.close()











