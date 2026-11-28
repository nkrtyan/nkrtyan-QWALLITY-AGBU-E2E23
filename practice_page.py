import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

benz = (By.XPATH, '//input[@id="benzradio"]')
honda = (By.ID, 'hondacheck')
opentab = (By.LINK_TEXT, "Open Tab")
# orange = (By.XPATH, "//option[@value='orange']")
# peach = (By.XPATH, "//option[@value='peach']")
orange_or_peach = (By.XPATH, "//option[@value='orange' or @value='peach']")
show = (By.ID, "show-textbox")
showhide = (By.NAME, "show-hide")
name = (By.NAME, "enter-name")
mouse = (By.XPATH, "//legend[text()='Mouse Hover Example']")
web_table = (By.XPATH, "//table[@id='product']//td[text()='Python Programming Language']")

def counter(practice_list):
    count = 0
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.letskodeit.com/practice")
    

    for item in practice_list:
        elements = driver.find_elements(*item)
        count += len(elements)

    print(f"The count is {count}")
    

if __name__ == "__main__":
    practice_list = [benz, honda, opentab, orange_or_peach, show, showhide, name, mouse, web_table]
    counter(practice_list)