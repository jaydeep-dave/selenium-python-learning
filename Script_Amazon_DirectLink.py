from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager #https://pypi.org/project/webdriver-manager/
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(ChromeDriverManager().install()) 
browser.get('https://www.amazon.in/Test-Exclusive-547/dp/B078BNQ318') #enter URL of your item

element = WebDriverWait(browser, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".//span[@id='priceblock_ourprice']"))
    )

price = float(element.text.replace('₹ ','').replace(',',''))
desired_price = 37000 #enter your desired price here
if price > desired_price:
    print("Price is greater than your desired price. Actual price is: ₹",price,"which is ₹",(price - desired_price),"more than your desired price.")
else:
    print("Price is less than your desired price. Actual price is: ₹",price,"which is ₹",(desired_price - price),"less than your desired price.")
    browser.find_element_by_xpath(".//input[@id='buy-now-button']").click()

    #enter email
    email = '' #enter your email address here
    password = '' #enter your password here
    email_element = browser.find_element_by_xpath(".//input[@id='ap_email']").send_keys(email)
    browser.find_element_by_xpath(".//input[@id='continue']").click()
    password_element = browser.find_element_by_xpath(".//input[@id='ap_password']").send_keys(password)
    browser.find_element_by_xpath(".//input[@id='signInSubmit']").click()

time.sleep(3)
browser.quit()