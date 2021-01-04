import time
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def scraping(url):
  option = Options()
  option.headless = True
  driver = webdriver.Chrome()

  driver.get(url)
  time.sleep(2)

  driver.find_element_by_xpath(
    "//div[@class='item-page']//div[@class='alert alert-icolink']//a[@class='alert-link']"
  ).click()
  time.sleep(2)

  driver.find_element_by_xpath(
     "//div[@class='table-responsive']//tbody//tr//td//a[@class='btn btn-primary btn-sm center-block']"
  ).click()
  time.sleep(2)

  current_url = driver.current_url
  return current_url