from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time  
import csv 

driver =webdriver.Chrome(executable_path="D:\Softwares\Chrome Driver\chromedriver.exe")

driver.get("https://www.youtube.com/user/krishnaik06/videos")

print(driver.title) # Title of a page
driver.get("https://www.youtube.com/c/Telusko/videos")
time.sleep(5)
print(driver.title)
driver.back()
print(driver.title)
driver.forward()
print(driver.title)
print(driver.current_url) # returns the URL of the page

time.sleep(5)
#driver.close()
driver.quit() # closes all browsers