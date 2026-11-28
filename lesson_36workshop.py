from selenium import webdriver
from selenium.webdriver.common.by import By

def alert_message():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.letskodeit.com/practice")

    serach_field = driver.find_element(By.ID, "name")
    names = "Mariam and Varditer"
    serach_field.send_keys(names)
    alert_button = driver.find_element(By.ID, "alertbtn")
    driver.implicitly_wait(10)
    alert_button.click()

    alert = driver.switch_to.alert
    alert_text = alert.text
    if names in alert_text:
        print(f"Our names are in the alert")
    else:
        print(f"Our names are missing from the alert")
    alert.accept()

    driver.close()

if __name__ == "__main__":
    alert_message()