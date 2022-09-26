from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path="D:\Softwares\Chrome Driver\chromedriver.exe")
driver.get("https://www.youtube.com/user/krishnaik06/videos")
driver.implicitly_wait(30)
my_element = driver.find_element(By.TAG_NAME,"style-scope ytd-c4-tabbed-header-renderer iron-selected").click()
time.sleep(5)
driver.close()