import math
import time

from selenium import webdriver

#paste link
link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
#get our link
browser.get(link)

#make function for calculating
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

#to find on page x
x_element_find = browser.find_element(by='css selector', value='#treasure')
x_element_valux = x_element_find.get_attribute("valuex")
x = x_element_valux
y = calc(x)
#to find input
input1 = browser.find_element(by='css selector', value='#answer')
#paste the found value
input1.send_keys(y)

#click the buttons
browser.find_element(by='css selector',value='#robotCheckbox').click()
browser.find_element(by='css selector',value='#robotsRule').click()
browser.find_element(by='css selector',value='button.btn.btn-default').click()
time.sleep(5)
browser.quit()
