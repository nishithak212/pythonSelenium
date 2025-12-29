import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Head Mode: Browser opens, and we see all the actions being performed that were mentioned in the script
#Headless Mode: Tester does not see browser invocation. Test runs in invisble mode, with chrome browser running in the background

#Declare chrome options to run the test in headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")


service_obj = Service("C:/Users/nishi/Documents/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj, options=chrome_options) #We also mention chrome options here to tell the browser we are running headless mode
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()


#For certian actions like to scroll down on a web page, we dont have direct menthods available in Selenium
#Therefore we use javascript within selenium to perform such actions
#Javascript method to scroll down -->  window.scrollBy(x,y) eg: x=0 (i.e. 0 pixel top of page), y=500 (i.e to 500th pixel)
#To scroll to bottom of the page --> window.scrollBy(0,document.body.scrollHeight)
#Whenever we use driver.excute_script, it means we are excuting javascript


driver.execute_script("window.scrollBy(0,document.body.scrollHeight);") #Javascript is given in quotes. 
#Whenever we use driver.excute_script, it means we are excuting javascript

time.sleep(2) #Defining sleep observe the scroll
#To scroll up to a particular section of the webpage. Here minus defines scrolling up
driver.execute_script("window.scrollBy(document.body.scrollHeight,-800);")

time.sleep(2) #Defining sleep observe the scroll
#To scroll down to a particular section of the webpage
driver.execute_script("window.scrollBy(document.body.scrollHeight,500);")

#To take a screenshot at the current state of the web page
driver.get_screenshot_as_file("screenshot_SH500.png")



time.sleep(2)