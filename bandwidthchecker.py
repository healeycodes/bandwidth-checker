import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import requests

FAST_URL = 'https://fast.com/'
FAST_COMPLETE_CSS = '#your-speed-message[style*="display: block"]'
FAST_SPEED_ID = 'speed-value'
FAST_UNITS_ID = 'speed-units'


def test_speed(driver):
    """
    Tests internet bandwidth via Netflix's fast.com.
        :param query: A webdriver instance of chrome
        :return: Tuple with the results (speed, units) both strings
    """
    driver.get(FAST_URL)

    # wait for test to finish i.e. when 'your speed message' is shown
    WebDriverWait(driver, 120).until(
        expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, FAST_COMPLETE_CSS))
    )

    speed_val = driver.find_element_by_id(
        FAST_SPEED_ID).get_attribute('innerHTML')
    speed_units = driver.find_element_by_id(FAST_UNITS_ID
                                            ).get_attribute('innerHTML')
    driver.quit()
    return {"speed": speed_val, "units": speed_units, "date": time.time()}


def send_speed(url, data, pw):
    """
    Send bandwidth result to external source.
        :param url: Endpoint to send a POST request to
        :param data: Dictionary of speed, units, and time
        :param pw: Password for the endpoint
    """
    data['pw'] = pw
    r = requests.post(url, json=data)
    return r.status_code


def create_chrome_driver(chrome_driver_path):
    """
    Create instance of a chrome webdriver.
        :param chrome_driver_path: Path to chromedriver executable
    """
    options = Options()
    options.headless = True
    return webdriver.Chrome(chrome_driver_path, options=options)


if __name__ == '__main__':
    chrome_driver_path = sys.argv[1]  # path to chrome driver
    endpoint = sys.argv[2]  # endpoint to save results
    pw = sys.argv[3]  # password for endpoint
    driver = create_chrome_driver(chrome_driver_path)
    results = test_speed(driver)
    status = send_speed(endpoint, results, pw)
    print(status)
