import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

service_obj = Service("C:/Users/nishi/Documents/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)

driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

#Handle mouse hovers using action class
#There is a class called ActionChains

action = ActionChains(driver)
#action.double_click(driver.find_element(By)).perform() #one of the action we can perform using ActionChains class
#action.context_click().perform() #one of the action we can perform using ActionChains class
#action.drag_and_drop().perform()
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform() #-- We can use this for hover function on Mouse Hover Button on the web page

#to right click on the first option displayed when mouse is hover on Mouse Hover button. Right click gives the small options box with Open link in new tab, Inspect etc
action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()

#to click on reload
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()

time.sleep(5)