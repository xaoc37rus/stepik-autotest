import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/math.html"

try:
    # Открываем браузер и переходим по ссылке
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    # Проверяем отмечен ли чекбокс I'm the robot
    if browser.find_element(By.ID, 'robotCheckbox').get_attribute('checked') == 'true':
        print(f'Чекбокс/Радиокнопка уже отмечена')
    else:
        print(f'Чекбокс/Радиокнопка еще не отмечена')
    time.sleep(1)

    # Проверяем отмечена ли радиокнопка Robots rule
    if browser.find_element(By.ID, 'peopleRule').get_attribute('checked') == 'true':
        print(f'Чекбокс/Радиокнопка уже отмечена')
    else:
        print(f'Чекбокс/Радиокнопка еще не отмечена')
    time.sleep(1)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()