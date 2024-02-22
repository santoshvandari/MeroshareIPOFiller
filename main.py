from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


# Open the browser and go to the website and open it continutouly. DOn't close automatically.
# This is a simple script to open the browser and go to the website and open it continutouly. DOn't close automatically.


options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
options.add_experimental_option("detach", True)


url='https://meroshare.cdsc.com.np/'
webdriver = webdriver.Chrome(options=options)
webdriver.get(url)
# webdriver.Maximize_window()

time.sleep(2)

username = webdriver.find_elements(By.ID,"username")[0]
password = webdriver.find_elements(By.ID,"password")[0]
print(username)
print(password)

username.send_keys("2208324")
password.send_keys("123456")

loginbtn=webdriver.find_elements(By.XPATH,"//button[@type='submit']")
print(loginbtn)
loginbtn.click()
