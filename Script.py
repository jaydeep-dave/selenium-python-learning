from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user_name = 'jaydeep.dave@volansys.com'
password = 'Hello@123'
browser = webdriver.Chrome(r"E:\\chromedriver.exe")
browser.get('https://dashboard-dev.aylanetworks.com/')
#browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[3]/button[2]').click()
email_element = browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[1]/div[3]/div/div[1]/form/ul/li[2]/input')
email_element.send_keys(user_name)
password_element = browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[1]/div[3]/div/div[1]/form/ul/li[2]/input')
password_element.send_keys(password)
#login = browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[1]/div[3]/div/div[1]/form/ul/li[3]/button')
#login.click()



