from selenium import webdriver
from selenium.webdriver.chrome.service import Service


#To specify how the browser should be invoked and use various chrome options
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--start-maximized") - Chrome Option to maximize the window. Disabling this as running this script in headless mode
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--ignore-certificate-errors")


service_obj = Service("C:/Users/nishi/Documents/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj,options=chrome_options)

driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)


