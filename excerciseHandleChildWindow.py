import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service_obj = Service("C:/Users/nishi/Documents/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)

driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,".blinkingText").click()

windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])
assert "DOCUMENTS REQUEST" == driver.find_element(By.XPATH,"//h1").text
print(driver.find_element(By.XPATH,"//h1").text)

emailID = driver.find_element(By.XPATH,"//p/strong/a[@href='mailto:mentor@rahulshettyacademy.com']").text #Extracting email ID using DOM-based locators. Self found solution
#message = driver.find_element(By.CSS_SELECTOR,".red").text #Instrcutor's instructions to use this method using python split and strip methods
#emailID = message.split("at")[1].strip().split(" ")[0]
print(emailID)

#time.sleep(2)
driver.close()

driver.switch_to.window(windowsOpened[0])
assert "Free Access to InterviewQues/ResumeAssistance/Material" == driver.find_element(By.CSS_SELECTOR,".blinkingText").text

driver.find_element(By.ID,"username").send_keys(emailID)
driver.find_element(By.ID,"password").send_keys("learning")
driver.find_element(By.ID,"signInBtn").click()

wait = WebDriverWait(driver,8)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".alert-danger")))
errorMessage = driver.find_element(By.CSS_SELECTOR,".alert-danger").text
print(driver.find_element(By.CSS_SELECTOR,".alert-danger").text)


time.sleep(2)
