import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service("C:/Users/nishi/Documents/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break
#print(driver.find_element(By.ID,"autosuggest").text) -- This does not print the country selected in the above for loop as
#.text only works on elements on the web page that are present when the page is loaded for the first time.
#But as the value is in dropdown , this value does not get captured and printed this way.
#To make sure the correct text is captured, we use the below method


#Get Attribute of values to validate dynamic texts on the browser
print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))

#Assertion will pass here as assert of True will be True
assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"

#Assertion will fail here as assert of False will be False as it is comparing value "India" with "BASIndia"
#assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "BASIndia"






time.sleep(5)


