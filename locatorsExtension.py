import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/nishi/Documents/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Forgot password?").click()

#We can also use PARTIAL_LINK_TEXT to match
#driver.find_element(By.PARTIAL_LINK_TEXT,"Forgot").click()

#below is parent to child traverse using XPATH
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")

#below is parent to chile traverse using CSS
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("hello@1234")

driver.find_element(By.CSS_SELECTOR,"form div:nth-child(3) input").send_keys("hello@1234")

#driver.find_element(By.XPATH,"//button[@type='submit']").click()

#We can also use text on the page and create XPATH
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()



time.sleep(5)