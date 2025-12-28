import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/nishi/Documents/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)

name = "Pooh" #declaring  a variable to save name that will be sent to test the pop up

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()

#Below step is used to switch driver from browser mode to alert mode to capture the pop-up displayed on the screen#
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText

time.sleep(2)
#To click on OK button on the pop-up we use below method
alert.accept()


#To dismiss or cancel or close we use alert.dismiss()
driver.find_element(By.CSS_SELECTOR,"#confirmbtn").click()
confirmPopup= driver.switch_to.alert
confirmPopupText = confirmPopup.text
print(confirmPopupText)
assert "Hello , Are you sure you want to confirm?" in confirmPopupText
time.sleep(2)
confirmPopup.dismiss()


time.sleep(3)
