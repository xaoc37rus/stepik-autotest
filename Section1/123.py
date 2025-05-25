import math
from faker import Faker
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://SunInJuly.github.io/execute_script.html'
fake = Faker()

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    # Находим значение Х и считаем
    x_value = browser.find_element(By.ID, 'input_value').text
    answer_num = math.log(abs(12*math.sin(int(x_value))))
    #time.sleep(1)

    # Вводим ответ в поле
    browser.find_element(By.XPATH, '//*[@id="answer"]').send_keys(str(answer_num))
    #time.sleep(1)

    # Отмечаем чекбокс I'm the robot
    browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]').click()
    #time.sleep(1)

    # Скролим страницу к радиокнопке Robots rule и отмечаем её
    radio_robots_rule = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    _ = radio_robots_rule.location_once_scrolled_into_view
    radio_robots_rule.click()
    #time.sleep(1)

    # Кликаем по кнопке Submit
    browser.find_element(By.TAG_NAME, "button").click()

    # Считываем алерт, выводим его текст в консоль и закрываем его
    js_alert = browser.switch_to.alert
    print(js_alert.text)
    js_alert.accept()
    time.sleep(5)

finally:
    browser.quit()