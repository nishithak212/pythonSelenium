import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

service_obj = Service("C:/Users/nishi/Documents/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)


driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

radioButtons = driver.find_elements(By.CSS_SELECTOR,"input[type='radio']")
#radioButtons = driver.find_elements(By.CSS_SELECTOR,".radioButton") #---- This is CSS selector using classname. Syntax is
# === .classname. Which in this case is .radioButton

#radioButtons[2].click() #--We can use indexing directly to click on radio button 2 if we know for sure that the order of radio buttons does not change
#assert radioButtons[2].is_selected() #-- To check if radio button that is on index 2 is selected


print(len(radioButtons))

for radioButton in radioButtons:
    if radioButton.get_attribute("value") == "radio2":
        radioButton.click()
        assert radioButton.is_selected()
        break

assert driver.find_element(By.ID,"displayed-text").is_displayed() #-- is_displayed() is used to check if certian element is displayed on the web page
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()




time.sleep(2)




    

