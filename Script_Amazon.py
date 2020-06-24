from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(r"E:\\chromedriver.exe") #location of webdriver
browser.get('https://www.amazon.in/')




#keep browser open
#chrome_options = Options()
#chrome_options.add_experimental_option("detach", True)