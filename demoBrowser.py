import time
from selenium import webdriver

#In Selenium pacakge, there is a class called webdriver
#To execute the test in chrome browser, there is a method called chrome in webdriver class


from selenium.webdriver.chrome.service import Service

#***Chrome driver service - This plays a key role in invoking web browser. Webdriver talks to chrome driver and
# chrome driver runs the told commands on the chrome browser
#By default, Selenium checks the chrome driver version, goes to the internet downloads it and talks to that
# chrome driver version

#**** Below step is recommended to invoke chrome browser ****#
# driver = webdriver.Chrome() #Invoke chrome browser
# driver.get("https://www.python.org") #to hit the url

#**** If driver is not opening automatically. Eg. If old chrome browser or if company vpn doesnot allow
# to download latest chrome driver use the below step****#
service_obj = Service("C:/Users/nishi/Documents/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.python.org")



time.sleep(2) #time is a python library. This will make the script to wait for 2 seconds