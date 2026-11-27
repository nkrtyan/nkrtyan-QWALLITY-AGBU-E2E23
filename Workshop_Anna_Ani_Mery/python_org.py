from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

def search(browser):

    if browser == "Chrome":
        driver = webdriver.Chrome()
    elif browser == "Edge":
        driver = webdriver.Edge()   
    else:
        raise ValueError("Unsupported browser")

    driver.maximize_window()
    driver.get("https://www.python.org/")
    time.sleep(3)
    assert "Python" in driver.title


    search = driver.find_element(By.ID, "id-search-field")
    submit = driver.find_element(By.ID, "submit")

    search_text = "aaaa"
    search.send_keys(search_text)
    time.sleep(3)
    submit.click()
    time.sleep(3)

    if driver.find_element(By.XPATH, '//*[@id="content"]/div/section/form/ul/li'):
        print(f"{search_text} was not found")

    print(f"Running of {item} has been done successfully. ")
    driver.close()


if __name__ == "__main__":

    browser = ["Chrome", "Edge", "Firfox"]
    for item in browser:
        search(item)


