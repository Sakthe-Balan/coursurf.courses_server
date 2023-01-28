from selenium import webdriver
# from selenium.webdriver.common.by import By
import time 

path = "msedgedriver.exe"
website = "https://www.classcentral.com/"

browser = webdriver.Edge(path)

browser.get(website)

browser.maximize_window()



browser.quit()

