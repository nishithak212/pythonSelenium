import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



browserSortedVeggies = []   
service_obj = Service("C:/Users/nishi/Documents/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)

driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element(By.XPATH,"//div/a[@class='cart-header-navlink' and text()='Top Deals']").click()


#Switch window
windows = driver.window_handles
driver.switch_to.window(windows[1])

#Pseduo Code
#1. click on column header
#2. collect all vegetable names into a list --> browser sorted veggieList
#3. sort browser sorted veggieList => newSortedList
#4. veggieList == newSortedList -- Assertion

#1. click on column header
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()


#2. collect all vegetable names into a list --> browser sorted veggieList
veggieWebElements = driver.find_elements(By.XPATH,"//tr/td[1]")

for element in veggieWebElements:
    browserSortedVeggies.append(element.text)

originalBrowserSortedList = browserSortedVeggies.copy() #.copy()--recommended or .slice() method to be used when creating copy of the list

#3. sort browser sorted veggieList => newSortedList
browserSortedVeggies.sort()

#4. veggieList == newSortedList -- Assertion
assert browserSortedVeggies == originalBrowserSortedList

print("Broswer sorted list:", browserSortedVeggies)
print("Original sorted list:", originalBrowserSortedList)

