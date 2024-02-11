from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#Initializate Chrome WebDriver instance
driver = webdriver.Chrome()

#List of driver API calls
#driver.add_cookie
#driver.add_credential()
#driver.add_virtual_authenticator()
#driver.back()

#List of driver Capabilities

driver.capabilities.clear()
driver.capabilities.update()

#Instance of element type


#Open google
driver.get("https://google.com")

element = driver.find_element_by_id("search")
