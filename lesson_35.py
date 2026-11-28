from selenium import webdriver
from selenium.webdriver.common.by import By

locators = {
    "Benz_radio_button": (By.ID, "benzradio"),
    "Honda_checkbox": (By.CSS_SELECTOR, "input#hondacheck"),
    "Open_Tab_button": (By.ID, "opentab"),
    "Orange_option": (By.CSS_SELECTOR, "#multiple-select-example option[value='orange']"),
    "Peach_option": (By.CSS_SELECTOR, "#multiple-select-example option[value='peach']"),
    "Show_button": (By.ID, "show-textbox"),
    "Hide_Show_Example_field": (By.ID, "displayed-text"),
    "Enter_Your_Name_field": (By.CSS_SELECTOR, "input#name"),
    "Mouse_Hover_Example_title": (By.XPATH, "//legend[text()='Mouse Hover Example']"),
    "Python_Programming_cell": (By.XPATH, "//table[@id='product']//td[text()='Python Programming Language']"),
}

def find_locators_count():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.letskodeit.com/practice")

    found_count = 0
    for name, (by, value) in locators.items():
        elements = driver.find_elements(by, value)
        if elements:
            found_count += len(elements)
        else:
            None

    print(f"\nTotal elements found: {found_count} out of {len(locators)}")

    driver.close()

if __name__ == "__main__":
    find_locators_count()