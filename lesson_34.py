import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://www.facebook.com")
    
    email = os.getenv("FB_EMAIL")
    password_value = os.getenv("FB_PASSWORD")
    
    if not email or not password_value: 
        print("Facebook credentials are missing!")
    
    username = driver.find_element(By.NAME, "email")
    password = driver.find_element(By.NAME, "pass")
    
    username.send_keys(email)
    password.send_keys(password_value)
    
    submit = driver.find_element(By.XPATH, '//*[@id="login_form"]/div/div[1]/div/div[3]/div/div/div/div[1]/div/span/span')
    submit.click()
    driver.close()
    print(f"test is finished")
except Exception as e:
    print(f"Login Facebook failed")

#Nel, code is working, structure is correct, good job :)