import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
load_dotenv()

email = os.getenv("FACEBOOK_EMAIL")
password = os.getenv("FACEBOOK_PASSWORD")
if email and password:
    print("Credentials loaded successfully")
else:
    print("Credentials not found")

#driver = webdriver.Chrome()
#driver.get("https://www.facebook.com/")
driver = webdriver.Chrome()

print("Chrome opened successfully")

driver.get("https://www.facebook.com/")

print("Facebook page opened")
wait = WebDriverWait(driver, 20)

email_field = wait.until(
    EC.visibility_of_element_located((By.ID, "email"))
)
email_field.send_keys(email)
password_field = wait.until(
    EC.visibility_of_element_located((By.ID, "pass"))
)

password_field.send_keys(password)

login_button = wait.until(
    EC.element_to_be_clickable((By.NAME, "login"))
    )
login_button.click()