import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
load_dotenv()


def login_facebook():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.facebook.com/')

    username = driver.find_element(By.NAME, 'email')
    password = driver.find_element(By.NAME, 'pass')
    submit = driver.find_element(By.XPATH, '//div[@role="button"]')

    username.send_keys(os.getenv('FACEBOOK_EMAIL'))
    password.send_keys(os.getenv('FACEBOOK_PASSWORD'))

    submit.click()

    if 'login' not in driver.current_url:
        print('Login successful')
    else:
        print('Login failed')   





if __name__ == '__main__':
    login_facebook()






