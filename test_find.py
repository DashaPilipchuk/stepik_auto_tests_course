import math
import time

from selenium import webdriver

#вставляем нужную ссылку
link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
#вызываем методом get нужную ссылку
browser.get(link)

#создаем функцию, которая сосчитает значение
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

#находим на странице x
x_element_find = browser.find_element(by='css selector', value='#treasure')
x_element_valux = x_element_find.get_attribute("valuex")
x = x_element_valux
y = calc(x)
#находим поле куда встаить значение
input1 = browser.find_element(by='css selector', value='#answer')
#вставляем значение
input1.send_keys(y)

#нажимем на кнопки и выходим из браузера
browser.find_element(by='css selector',value='#robotCheckbox').click()
browser.find_element(by='css selector',value='#robotsRule').click()
browser.find_element(by='css selector',value='button.btn.btn-default').click()
time.sleep(5)
browser.quit()