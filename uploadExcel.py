from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

file_path = "C:/Users/nishi/PycharmProjects/PythonTesting/pythonSelenium/excelFiles/download.xlsx"

service_obj = Service("C:/Users/nishi/Documents/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")

#download excel file
driver.find_element(By.ID,"downloadButton").click()

#edit the excel with updated file

#upload excel file
file_input = driver.find_element(By.CSS_SELECTOR,"input[type='file']")
file_input.send_keys(file_path) #Provide path of the excel file

#Explicit wait to wait for the upload successful message to appear on the page after excel file upload
wait = WebDriverWait(driver,10)
toast_locator = (By.CSS_SELECTOR,".Toastify__toast-body div:nth-child(2)")
wait.until(EC.visibility_of_element_located(toast_locator))  #We pass a locator inorder for selenium to wait for the element to appear

print(driver.find_element(*toast_locator).text)


