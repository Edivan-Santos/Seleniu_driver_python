from selenium   import webdriver
import time

#driver = webdriver.Chrome()
#driver.get('https://www.saucedemo.com/v1/')

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.saucedemo.com/v1/')
time.sleep(5)