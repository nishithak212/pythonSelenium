import time
from selenium import webdriver
driver = webdriver.Chrome() #To launch Chrome browser
#driver = webdriver.Firefox() #To launch Firefox browser
#driver=webdriver.Edge() #To launch Microsoft Edge browser
driver.get("https://www.python.org")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(2)
