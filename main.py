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
crn= os.getenv("CRN")
transactionpin= os.getenv("TRANSACTIONPIN")


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
if len(applyissue) == 0:
    print("No IPO/FPO Available")
    exit()
for company in applyissue:
    print("Getting Comapny Details")
    issuefor = (((company.find_elements(By.XPATH,"//span[@tooltip='Sub Group']")[0]).get_attribute("innerHTML")).strip()).lower()
    issuetype = (((company.find_elements(By.XPATH,"//span[@tooltip='Share Type']")[0]).get_attribute("innerHTML")).strip()).lower()
    sharetype = (((company.find_elements(By.XPATH,"//span[@tooltip='Share Group']")[0]).get_attribute("innerHTML")).strip()).lower()
    button = (company.find_elements(By.XPATH,"//button[@class='btn-issue'][@type='button']")[0])
    buttonText = ((button.find_elements(By.TAG_NAME,"i")[0].get_attribute("innerHTML")).strip()).lower()
    print(f"Issue For: {issuefor} \nIssue Type: {issuetype} \nShare Type: {sharetype} \nButton Text: {buttonText} \n")
    # check contains or nto 

    if "general" and "public" in issuefor and ("ipo" in issuetype or "fpo" in issuetype) and "ordinary" in sharetype and "apply" in buttonText:
    # if "general public" in issuefor and "ipo" in issuetype and "apply" in buttonText:
        print("Entering the Apply Section")
        button.click()
        time.sleep(2)

        # Selecting the Bank Account
        print("Selecting the Bank Account")
        bankaccount = webdriver.find_elements(By.XPATH,"//*[@id='selectBank']/option")[1]
        bankaccount.click()
        time.sleep(2)


        # Selecting the Bank Accoutn Number
        print("Selecting the Bank Account Number")
        bankaccountnumber = webdriver.find_elements(By.XPATH,"//*[@id='accountNumber']/option")[1]
        bankaccountnumber.click()
        time.sleep(2)

        # Entering the Quantity to apply
        print("Entering the Quantity to Apply")
        unitstoapply=webdriver.find_element(By.ID,'appliedKitta')
        unitstoapply.send_keys("10")


        #Entering the CRN Number
        print("Entering the CRN Number")
        crnnumber=webdriver.find_element(By.ID,'crnNumber')
        crnnumber.send_keys(crn)

        #Checking the Terms and Conditions
        print("Checking the Terms and Conditions")
        termsandconditions = webdriver.find_element(By.ID,'disclaimer')
        termsandconditions.click()

        # Clicking the Proceed Button
        print("Clicking the Proceed Button")
        proceedbutton = webdriver.find_element(By.XPATH,"//*[@id='main']/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[5]/div[2]/div/button[1]")
        proceedbutton.click()

        # Entering the PIN Number 
        print("Entering the PIN Number")
        pininput=webdriver.find_element(By.ID,'transactionPIN')
        pininput.send_keys(transactionpin)

        # Clicking the Apply Button
        applybutton=webdriver.find_element(By.XPATH,"//*[@id='main']/div/app-issue/div/wizard/div/wizard-step[2]/div[2]/div/form/div[2]/div/div/div/button[1]")
        # applybutton.click()
        print("Successfully Applied for the IPO")
    else:
        print("No IPO/FPO Available for the Company")
