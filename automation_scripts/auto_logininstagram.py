from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# keepchrome open ever after script ends 
chrome_options = Options()

chrome_options.add_experimental_option("detach", True)

#start chrome browser 
driver = webdriver.Chrome(options=chrome_options)

#open instagram login page 
driver.get("https://www.instagram.com/accounts/login/")

time.sleep(5) 

#enter email or username 
username = driver.find_element(By.NAME,"username")
username.send_keys("@ig_shirshadip")

#enter password
password = driver.find_element(By.NAME,"password")
password.send_keys("sonu bulu")

password.send_keys(Keys.RETURN) #press enter

time.sleep(10)
