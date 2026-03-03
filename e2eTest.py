import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service("C:/Users/nishi/Documents/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(8)

driver.get("https://rahulshettyacademy.com/angularpractice/")

#For the href value =>href="/angularpractice/shop" we can use below CSS or Xpath regular expressions instead
#of specifying the whole value. Although not recommended

#Regular expression CSS --> a[href*='shop']

#Regular expression XPath --> //a[contains(@href,'shop')]

#Below step is to click on Shop link
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()


#Next task is to iterate through the product cards and select one
products = driver.find_elements(By.XPATH,"//div[@class='card h-100']") #==> Returns list of webelements. In our case list of product cards

#Iterate through each product
for product in products:
    productName = product.find_element(By.XPATH,"div/h4/a").text #gives product name
    if productName == "Blackberry":
        product.find_element(By.XPATH,"div/button").click()

#Add to cart
driver.find_element(By.CSS_SELECTOR,"a[class*=btn-primary]").click()

#Click on checkout
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()

#Handling auto suggestive options for country
driver.find_element(By.ID,"country").send_keys("Ind")

#System takes some time to display the list of countries. For this we use explicit wait
wait = WebDriverWait(driver,10) #WebDriverWait class. Waits for 10 seconds as defined
wait.until(EC.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()

#Click agree terms and conditions
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()

#Click on Submit
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()


#Valdiating success message on the screen
successText = driver.find_element(By.CLASS_NAME,"alert-success").text

#Assertion
assert "Success! Thank you!" in successText

time.sleep(3)

driver.close()
