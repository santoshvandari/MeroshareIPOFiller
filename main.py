from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time,os
load_dotenv()

# Getting the .env file Data 
username = os.getenv("USER_NAME")
password = os.getenv("PASSWORD")
DPCapital = os.getenv("DPCAPITAL")


# for login  to the mero share
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


# Opening the MyAsba Tab and Clicking it
time.sleep(2)

myAsbaEl= webdriver.find_elements(By.XPATH,"//*[@id='sideBar']/nav/ul/li[8]/a")[0]
myAsbaEl.click()



print("Getting the Total Issue Company")
time.sleep(2)
# Get the apply button element 
applyissue = webdriver.find_elements(By.CLASS_NAME,"company-list")

# print(applyissue)

for company in applyissue:
    print("Comapny Details")
    issuefor = (((company.find_elements(By.XPATH,"//span[@tooltip='Sub Group']")[0]).get_attribute("innerHTML")).strip()).lower()
    issuetype = (((company.find_elements(By.XPATH,"//span[@tooltip='Share Type']")[0]).get_attribute("innerHTML")).strip()).lower()
    sharetype = (((company.find_elements(By.XPATH,"//span[@tooltip='Share Group']")[0]).get_attribute("innerHTML")).strip()).lower()
    button = (company.find_elements(By.XPATH,"//button[@class='btn-issue'][@type='button']")[0])
    print("Button: ",button)
    print("Button html : ",button.get_attribute("innerHTML"))
    buttonText = ((button.find_elements(By.TAG_NAME,"i")[0].get_attribute("innerHTML")).strip()).lower()
    print(f"Issue For: {issuefor} \nIssue Type: {issuetype} \nShare Type: {sharetype} \nButton Text: {buttonText} \n")
    # check contains or nto 

    if "general" and "public" in issuefor and ("ipo" in issuetype or "fpo" in issuetype) and "ordinary" in sharetype and "apply" in buttonText:
    # if "general public" in issuefor and "ipo" in issuetype and "apply" in buttonText:
        print("Entering the Apply Section")
        print("Applying for the IPO")
        button.click()
        time.sleep(2)
        # print(webdriver.find_elements(By.XPATH,'html')[0].get_attribute("innerHTML"))

        # with open("apply.html","w") as file:
        #     file.write(webdriver.page_source)

        # Selecting the Bank Account
        bankaccount = webdriver.find_elements(By.XPATH,"//*[@id='selectBank']/option")[1]
        print(bankaccount)
        bankaccount.click()
        time.sleep(2)


        # Selecting the Bank Accoutn Number
        bankaccountnumber = webdriver.find_elements(By.XPATH,"//*[@id='accountNumber']/option")[1]
        print(bankaccountnumber)
        

