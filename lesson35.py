import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

def run_drivers(browser):
    
    if browser == "Chrome":
        driver = webdriver.Chrome()
    elif browser == "Edge":
        driver = webdriver.Edge()
    else:
        raise ValueError('Unsupported browser. ')
    
    
    driver.maximize_window()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    
    
    search = driver.find_element(By.NAME, 'q')
    
    search.send_keys('bla bla')
    search.send_keys(Keys.RETURN)
    time.sleep(3)
    
    assert "No results found." in driver.page_source, "Error message"
    
    driver.close()
    print(f"Test is finished")
    
    
if __name__ == "__main__":
    browser = ["Chrome", "Edge"]
    for item in browser:
        run_drivers(item)