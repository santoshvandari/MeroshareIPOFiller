from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time,os
load_dotenv()

username = os.getenv("USER_NAME")
password = os.getenv("PASSWORD")
DPCapital = os.getenv("DPCAPITAL")
print(username)

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)


# Opening the Browser and Meroshare Tab 
url='https://meroshare.cdsc.com.np/'
webdriver = webdriver.Chrome(options=options)
webdriver.get(url)
time.sleep(2)

# Getting the Select Element for Selecting the Capital
element = webdriver.find_element(By.ID, "selectBranch")
element.click()
option_xpath = f"//ul[@class='select2-results__options']//li[contains(text(), '{DPCapital}')]"
option_element = webdriver.find_element(By.XPATH, option_xpath)
option_element.click()


# selecting the User element and sending the keys
usernameEl = webdriver.find_elements(By.ID,"username")[0]
passwordEl = webdriver.find_elements(By.ID,"password")[0]
usernameEl.send_keys(username)
passwordEl.send_keys(password)


# Selecting the Login Button and Clicking it
loginbtn=webdriver.find_elements(By.XPATH,"//button[@type='submit']")[0]
print(loginbtn)
loginbtn.click()
print("Logged in Successfully")

