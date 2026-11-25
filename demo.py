import os
import time
# from dotenv import load_dotenv
# from dotenv import set_key
from selenium import webdriver


# print(os.environ["my_pass"])
# print(os.environ["my_username"])

# os.environ["API_USER"] = "SuperUser"
# os.environ["API_PASSWORD"] = "asasas"

# USER = os.environ.get("API_USER")
# PASSWORD = os.environ.get("API_PASSWORD")
# print(USER)
# print(PASSWORD)

# #for registration

# os.environ["username"] = "SuperUser"
# os.environ["pass"] = "asasas"
# os.environ["token"] = 'kdjnvnvjfn'

# username = os.environ.get("username")

# #load dotenv
# load_dotenv()

# print(os.getenv("api_key"))

# set_key(".env", "api_key", "new_value")

# load_dotenv(override=True)

# print(os.getenv("api_key"))

#selenium
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.python.org/")
# time.sleep(3)
print(driver.title)
driver.close()
