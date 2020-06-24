from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(r"E:\\chromedriver.exe") #location of webdriver
browser.get('https://www.amazon.in/')
search_text = "One Plus 8" #enter your search text here
search = browser.find_element_by_xpath(".//input[@id='twotabsearchtextbox']").send_keys(search_text)
browser.find_element_by_xpath(".//div[@class='nav-search-submit nav-sprite']//input[@class='nav-input']").click()

element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'OnePlus 8 5G (Glacial Green 6GB RAM+128GB Storage)')]"))
    )
element.click()