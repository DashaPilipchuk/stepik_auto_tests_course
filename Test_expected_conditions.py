import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# говорим Selenium проверять в течение 12 секунд, пока прайс не станет меньше 100 $
try:
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element(by="css selector", value="#book").click()
    browser.execute_script("window.scrollBy(0,100);")
    x = browser.find_element(by='css selector', value='#input_value').text
    y = calc(x)
    browser.find_element(by='css selector', value='#answer').send_keys(y)
    browser.find_element(by='css selector', value='#solve').click()

finally:
    time.sleep(5)
    browser.quit()

