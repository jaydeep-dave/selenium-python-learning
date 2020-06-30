from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

browser = webdriver.Chrome(r"E:\\chromedriver.exe") #location of webdriver
browser.get('https://www.amazon.in/')
search_text = "One Plus 8" #enter your search text here
search = browser.find_element_by_xpath(".//input[@id='twotabsearchtextbox']").send_keys(search_text)
browser.find_element_by_xpath(".//div[@class='nav-search-submit nav-sprite']//input[@class='nav-input']").click()

element = WebDriverWait(browser, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, ".//span[contains(text(),'OnePlus 7T Pro (Haze Blue, 8GB RAM, Fluid AMOLED Display, 256GB Storage, 4085mAH Battery)')]")) #enter exact text of your device from the search list
    )
element.click()

#reference: https://medium.com/@pavel.tashev/python-and-selenium-open-focus-and-close-a-new-tab-4cc606b73388
browser.switch_to.window(browser.window_handles[1])

element = WebDriverWait(browser, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".//span[@id='priceblock_ourprice']"))
    )
element.get_attribute('innerHTML')

element = WebDriverWait(browser, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".//span[@id='priceblock_ourprice']"))
    )

element.get_attribute('innerHTML')
