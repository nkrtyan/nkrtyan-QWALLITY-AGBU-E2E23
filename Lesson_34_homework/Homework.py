from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

#step 1) Open the Chrome
driver=webdriver.Chrome()
driver.maximize_window()

#step 2) Navigate to Facebook
driver.get("https://www.facebook.com")

#step 3)Enter Email/mobile number and password
username=driver.find_element(By.NAME, "email")
password=driver.find_element(By.NAME, "pass")
submit=driver.find_element(By.XPATH, '//*[@id="login_form"]/div/div[1]/div/div[3]/div/div/div')

username.send_keys(os.getenv("username",""))
password.send_keys(os.getenv("password",""))
time.sleep(3)

#step 4) click log in
submit.click()

#step 5)close the browser
driver.close()
# Nel, correct, working code, you can move he logic inside the function