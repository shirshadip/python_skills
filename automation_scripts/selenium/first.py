from selenium import webdriver


driver = webdriver.Chrome()

driver.get("http://selenium.dev")
title = driver.title
print (title)
# driver.quit()
driver.implicitly_wait(1)