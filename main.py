import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

options = Options()
# options.headless = True
driver = webdriver.Chrome('./chromedriver', chrome_options=options)
driver.get('https://fast.com/')

# wait for test to finish i.e. when speed message is shown
WebDriverWait(driver, 60).until(
    expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '#your-speed-message[style*="display: block"]'))
)

speed_val = driver.find_element_by_id('speed-value').get_attribute('innerHTML')
speed_units = driver.find_element_by_id(
    'speed-units').get_attribute('innerHTML')
print(speed_val)
print(speed_units)
driver.quit()
