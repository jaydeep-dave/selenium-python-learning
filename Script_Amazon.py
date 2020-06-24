from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(r"E:\\chromedriver.exe") #location of webdriver
browser.get('https://www.amazon.in/')
search_text = "One Plus 8"
browser.find_element_by_xpath(".//input[@id='twotabsearchtextbox']").send_keys(search_text)
browser.find_elements_by_xpath(".//div[@class='nav-search-submit nav-sprite']").click()





#keep browser open
#chrome_options = Options()
#chrome_options.add_experimental_option("detach", True)