from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

path = "msedgedriver.exe"
website = "https://www.classcentral.com/"

browser = webdriver.Edge(path)

browser.get(website)

browser.maximize_window()

browser.implicitly_wait(5)

# inputSearch = browser.find_element('//input[@placeholder="Search 100,000 courses…"]')
inputSearch = browser.find_element(By.XPATH, '//input[@placeholder="Search 100,000 courses…"]')
inputSearch.send_keys("python")
inputSearch.submit()

time.sleep(5)

browser.quit()

