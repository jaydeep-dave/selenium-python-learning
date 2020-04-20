from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user_name = 'jaydeep.dave@volansys.com'
password = 'Hello@123'
#location of webdriver
browser = webdriver.Chrome(r"E:\\chromedriver.exe")
browser.get('https://dashboard-dev.aylanetworks.com/')
browser.find_element_by_css_selector('#privacyModal > div.modal-dialog.modal-lg > div > div.modal-footer > button:nth-child(2)').click()
email_element = browser.find_element_by_name('email')
email_element.send_keys(user_name)
password_element = browser.find_element_by_name('password')
password_element.send_keys(password)
login_element = browser.find_element_by_css_selector('#login > ul > li:nth-child(3) > button').click()
#please enter value of your B-Bridge's DSN into tr:nth-child($value$)
select_device = browser.find_element_by_css_selector('#devices > div > table > tbody > tr:nth-child(10) > td.green-text-field.ng-binding').click()