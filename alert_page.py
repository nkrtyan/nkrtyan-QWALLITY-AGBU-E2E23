import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.letskodeit.com/practice")

text_name = "Varduhi Ani"

alert_text = driver.find_element(By.NAME, "enter-name")
alert_text.send_keys(text_name)

alert = driver.find_element(By.ID, "alertbtn")
alert.click()

popupwindow = driver.switch_to.alert
actual_text = popupwindow.text
print(actual_text)

if text_name in actual_text:
    popupwindow.accept()
    driver.save_screenshot("screen.png")
    print("Test finish successful")
else:
    popupwindow.accept()
    driver.save_screenshot("screen.png")
    raise ValueError("Expected text was not found in the alert")


driver.close()