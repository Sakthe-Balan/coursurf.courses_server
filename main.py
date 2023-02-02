from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time 

path = "msedgedriver.exe"
browser = webdriver.Edge(path)

website = "https://www.classcentral.com/"

provider = "coursera"

# search = input("Enter the course you want to search: ")
wait = WebDriverWait(browser, 10)

def topicSearch(search):
  browser.get(website)
  browser.maximize_window()
  # inputSearch = browser.find_element('//input[@placeholder="Search 100,000 courses…"]')
  inputSearch = browser.find_element(By.XPATH, '//input[@placeholder="Search 100,000 courses…"]')
  inputSearch.send_keys(search)
  inputSearch.submit()

  time.sleep(2)
  
  print("Courses loaded")
  browser.quit()


def courseProvider(provider):
  courseProviderUrl = "https://www.classcentral.com/provider/" + provider
  browser.get(courseProviderUrl)
  browser.maximize_window()
  browser.implicitly_wait(5)
  time.sleep(1)
  
  loadMoreButton = browser.find_element(By.XPATH, '//*[@id="page-provider"]/div[1]/div[3]/div[5]/div/button')
  
  
  for i in range(1, 10):
    while True:
      try:
        loadMoreButton.click()
        time.sleep(0.45+(i/50))
        # loadMoreButton = browser.find_element(By.XPATH, '//*[@id="page-provider"]/div[1]/div[3]/div[5]/div/button')
        loadMoreButton = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-provider"]/div[1]/div[3]/div[5]/div/button')))
      except:
        print("No more courses to load")
        break
      
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5+i)
    loadMoreButton = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-provider"]/div[1]/div[3]/div[5]/div/button')))
    time.sleep(1+i)
    
    # time.sleep(2)
  time.sleep(30)
  print("Courses loaded")
  # browser.quit()


def courseProviderURL(provider):
  browser.maximize_window()
  baseUrl = "https://www.classcentral.com/provider/" + provider
  for i in range(1,5):
    browser.get(str(baseUrl+"?page="+str(i)))
    xpath = ['//*[@id="page-provider"]/div[1]/div[3]/div[5]/ol/li[1]','//*[@id="page-provider"]/div[1]/div[3]/div[5]/ol/li[2]','//*[@id="page-provider"]/div[1]/div[3]/div[5]/ol/li[3]','//*[@id="page-provider"]/div[1]/div[3]/div[5]/ol/li[4]','//*[@id="page-provider"]/div[1]/div[3]/div[5]/ol/li[5]']
    for card in xpath:
      result = browser.find_element(By.XPATH, '//*[@id="page-provider"]/div[1]/div[3]/div[5]/ol/li[3]')
      result = result.find_element(By.XPATH, '//div[1]/div[1]/div[2]/a[1]/h2')
      result = result.get_attribute('innerHTML')
      print(result)
      time.sleep(1)
    # time.sleep(2)

# xpath for courseproviders = //*[@id="page-provider"]/div[1]/div[3]/div[5]/ol/li[1]
  

# courseProvider("coursera")
courseProviderURL("coursera")
