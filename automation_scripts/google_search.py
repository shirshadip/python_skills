from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

#keep chrome open 
chrome=Options()
chrome.add_experimental_option("detach", True)

driver= webdriver.Chrome(options=chrome)

#open google 
driver.get("https://www.google.com")

time.sleep(2)

#find the searchbox and type query 
searchbox = driver.find_element(By.NAME,"q")
searchbox.send_keys("python language")

searchbox.send_keys(Keys.RETURN) #press enter

time.sleep(5)