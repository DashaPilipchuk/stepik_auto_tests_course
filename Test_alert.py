import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.find_element(by="css selector", value="button.btn.btn-primary").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element(by='css selector', value='#input_value').text
    y = calc(x)
    browser.find_element(by='css selector', value='#answer').send_keys(y)
    browser.find_element(by='css selector', value='button.btn.btn-primary').click()

finally:
    time.sleep(10)
    browser.quit()


