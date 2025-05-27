import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'https://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    button_book = browser.find_element(By.ID, 'book') # Находим кнопку Book
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100') # Жмем кнопку когда цена станет 100$
    )
    button_book.click() # Кликаем на кнопку Book
    # Решаем капчу
    x_value = browser.find_element(By.ID, 'input_value').text
    answer_num = math.log(abs(12*math.sin(int(x_value))))
    # Вводим ответ в поле
    browser.find_element(By.XPATH, '//*[@id="answer"]').send_keys(str(answer_num))
    # Жмем кнопку Submit
    browser.find_element(By.ID, 'solve').click()
    # Находим и считываем алерт
    js_alert = browser.switch_to.alert
    print(js_alert.text)
    js_alert.accept()
    time.sleep(5)
finally:
    browser.quit()

# Тест 2
# Тест 3