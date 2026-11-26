from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from config_logging import setup_logger
import logging

setup_logger()
   
fb_email = os.environ.get('FB_EMAIL')
fb_password = os.environ.get('FB_PASS')

if not fb_email or not fb_password:
    logging.error("Facebook email or password is not set in environment variables.")
else:
    logging.info("Facebook email and password retrieved from environment variables.")

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.facebook.com/")
    print(driver.title)
    logging.info("Facebook login page opened successfully.",{"title": driver.title})


    username = driver.find_element(By.NAME, "email")
    password = driver.find_element(By.NAME, "pass")
    submit = driver.find_element(By.XPATH, '//*[@id="login_form"]/div/div[1]/div/div[3]')
    username.send_keys(fb_email)
    password.send_keys(fb_password)
    logging.info("Entered successfully.")
    submit.click()
    logging.info("Button clicked.")
    time.sleep(20)
    driver.close()
    logging.info("Browser closed successfully.")
# Nel, code is correct, environment is reading correctly
