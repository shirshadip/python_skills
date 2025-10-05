import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

#keep chrome open 
chrome=Options()
chrome.add_experimental_option("detach", True)

driver= uc.Chrome()

#open google 
driver.get("https://www.google.com")

time.sleep(2)

#find the searchbox and type query 
searchbox = driver.find_element(By.NAME,"q")
searchbox.send_keys("python language")

searchbox.send_keys(Keys.RETURN) #press enter

time.sleep(5)

#get search results titles and links 
results = driver.find_elements(By.CSS_SELECTOR, "h3")[:5]

print ("top 5 google search results:")
for i,result in enumerate(results,start=1):
    try:
        link=result.find_element(By.XPATH, "..").get_attribute("href")
        print (f"{i}.{result.text} ->{link}")
    except:
         pass