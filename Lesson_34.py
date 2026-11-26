from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.facebook.com/")

time.sleep(6)

print(driver.title)

username = driver.find_element(By.NAME, "email")
password = driver.find_element(By.NAME, "pass")

submit = driver.find_element(By.XPATH, '//div[@aria-label="Log In" and @role="button"]')

username.send_keys(" ")
password.send_keys(" ")

submit.click()

time.sleep(5)

driver.close()