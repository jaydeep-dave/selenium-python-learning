from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

browser = webdriver.Chrome(r"E:\\chromedriver.exe") #location of webdriver
browser.get('https://www.amazon.in/Test-Exclusive-749/dp/B07DJ8K2KT') #enter URL of your item

element = WebDriverWait(browser, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".//span[@id='priceblock_ourprice']"))
    )

price = float(element.text.replace('₹ ','').replace(',',''))
desired_price = 37000 #enter your desired price here
if price > desired_price:
    print("Price is greater than your desired price. Actual price is: ₹",price,"which is ₹",(price - desired_price),"more than your desired price.")
else:
    print("Price is less than your desired price. Actual price is: ₹",price,"which is ₹",(desired_price - price),"less than your desired price.")
