import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

service_obj = Service("C:/Users/nishi/Documents/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)

#Add all the products to the cart that show up on the page when "ber" is given in search bar. This needs to be handled dynamically as producst can be added or removed from the website in real time
products = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(products)
print(count)
assert count > 0

#To have an entire access of products in the displayed list. This is called chaining of web elements
for product in products:
    product.find_element(By.XPATH,"div/button").click()

#Click on the cart
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()

#Proceed to checkout
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

#But as there is some wait for the system to load and display the text we need to apply wait
time.sleep(3)

#Apply promo code and click apply
driver.find_element(By.CSS_SELECTOR,"input[class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

#To verify if promo code is applied successfully.
#But as there is some wait for the system to load and display the text we need to apply wait
time.sleep(10)
promoCodeApplied =  driver.find_element(By.CLASS_NAME,"promoInfo")
assert promoCodeApplied.text == "Code applied ..!"
print(promoCodeApplied.text)






time.sleep(2)
