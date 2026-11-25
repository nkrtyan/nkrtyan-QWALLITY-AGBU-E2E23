from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S', 
    filename='sel_env.log',
    filemode='a+', 
    encoding='utf-8' 
)

load_dotenv() 

email = os.getenv("fb_email")
pwd = os.getenv("fb_pass")

if not email or not pwd:
    logging.error("Email or password not found in .env file!")
else:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.facebook.com/")

    username = driver.find_element(By.NAME, "email")
    password = driver.find_element(By.NAME, "pass")
    submit = driver.find_element(By.XPATH, '//*[@id="login_form"]/div/div[1]/div/div[3]/div/div/div')
    
    username.send_keys(email)
    password.send_keys(pwd)
    submit.click()
    
    time.sleep(20)

    logging.info(f"Login succeeded! Page title: {driver.title}")
    driver.close()
    logging.info("Test is finished")