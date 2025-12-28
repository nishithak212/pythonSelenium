import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

service_obj = Service("C:/Users/nishi/Documents/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

#Selenium provides locators such as ID, Xpath, CSSSelector, Classname, name, linkText

#To create custom CSSSelector for an element, syntax is tagname[attribute='value']. Also #id is also CSSSelector.
#Also .classname is also CSSSelector
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("John")

driver.find_element(By.NAME,"email").send_keys("helo@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID,"exampleCheck1").click()

driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()

#Static Dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
#dropdown.select_by_index(1)
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
#dropdown.select_by_value()

#To create custom Xpath for an element, syntax is //tagname[@attribute='value']
#eg for Xpath --> //input[@type='submit']
#Using Xpath if multiple elements are identified in selectorsHub, then we can use indexes to
#define. Eg: (//input[@type='text'])[3]
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)

#Assertion to check if the message displayed on the web page after submitting form is a success
assert "Success" in message

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("HelloAgain")

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()
time.sleep(5)


