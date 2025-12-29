import time
from selenium import webdriver #-- Modern Selenium 4 , recommended way
from selenium.webdriver.firefox.service import Service #--Manual configuration of geckodriver
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/nishi/Documents/geckodriver-v0.36.0-win64/geckodriver.exe") #--Manual configuration of geckodriver
driver=webdriver.Firefox(service=service_obj) #--Manual configuration of geckodriver

#driver = webdriver.Firefox() #-- Modern Selenium 4 , recommended way

driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Click Here").click()
windowsOpened = driver.window_handles # --Stores all the windows opened in a list format


driver.switch_to.window(windowsOpened[1]) # -- This switches to the window with index 1. (Window we open first has index 0 and the window that opens through the script has index 1 and so on)
print(driver.find_element(By.TAG_NAME,"h3").text)
time.sleep(2)
#to close child window
driver.close()

driver.switch_to.window(windowsOpened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text
print(driver.find_element(By.TAG_NAME,"h3").text)


time.sleep(2)