from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import environment_veriables # TODO, not used
import os

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.facebook.com/")


username = driver.find_element(By.NAME, "email")
password = driver.find_element(By.NAME, "pass")
submit = driver.find_element(By.XPATH, '//*[@id="login_form"]/div/div[1]/div/div[3]')

username.send_keys(os.environ.get('UserName'))
password.send_keys(os.environ.get('Password'))

submit.click()
time.sleep(10)

driver.close()
print("Test is finished.")
# Nel, correct, working code