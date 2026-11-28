from selenium import webdriver
from selenium.webdriver.common.by import By



def lets_code():
    driver=webdriver.Chrome()
    driver.maximize_window()
    
    driver.get("https://www.letskodeit.com/practice")
    
    counter=0
    
    benz=driver.find_elements(By.ID, "benzradio")
    honda=driver.find_elements(By.XPATH, '//*[@id="hondacheck"]')
    open_tab=driver.find_elements(By.CSS_SELECTOR, 'div[id^=open]')
    
    list=[benz, honda, open_tab]

    for i in list:
        count=counter + len(i)
        print(count) 

    if __name__=="__main__":
        lets_code()