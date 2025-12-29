import time
from selenium import webdriver
#from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#service_obj=Service("C:/Users/nishi/Documents/geckodriver-v0.36.0-win64/geckodriver.exe")
#driver=webdriver.Firefox(service=service_obj)
service_obj = Service("C:/Users/nishi/Documents/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)


driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

#Switch to frame
driver.switch_to.frame("courses-iframe")
driver.find_element(By.LINK_TEXT,"Browse Learning Paths").click()

heading = driver.find_element(By.CSS_SELECTOR,"h1").text
assert heading == "Choose Your Learning Journey"
print(heading)

#driver.find_element(By.ID,"tinymce").send_keys("I am able to automate frames")

#Switch back to default content
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"h1").text)

