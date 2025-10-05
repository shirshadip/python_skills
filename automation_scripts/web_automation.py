from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
from selenium.webdriver.chrome.options import Options

#start chrome browser 
chrome_options=Options()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)


#open youtube 
driver.get("https://www.youtube.com")

#wait for page to load 
time.sleep(1)

#find searchbox and start typing a query

searchbox= driver.find_element(By.NAME,"search_query")
searchbox.send_keys("Python programming tutorials")
searchbox.send_keys(Keys.RETURN) #press enter

#wait to see the result 
#time.sleep(2)
'''#close browser
driver.quit()'''


