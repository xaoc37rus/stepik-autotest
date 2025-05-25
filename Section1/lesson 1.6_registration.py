from faker import Faker # Библиотека для генерации фейковых данных, прикольная штука, нужно устанавливать
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/registration2.html"
fake = Faker() # Создаём экземпляр класса Faker

try:
    # Создаем объект класса (браузер) и переходим по ссылке
    browser = webdriver.Chrome()
    browser.get(link)
    # time.sleep(1)

    # Находим первое обязательное поле и заполняем
    browser.find_element(By.XPATH, '(//input[@required])[1]').send_keys(fake.word()) #CSS div.first_block input.first
    # Находим второе обязательное поле и заполняем
    browser.find_element(By.XPATH, '(//input[@required])[2]').send_keys(fake.word()) #CSS div.first_block input.second
    # Находим третье обязательное поле и заполняем
    browser.find_element(By.XPATH, '(//input[@required])[3]').send_keys(fake.word()) #CSS div.first_block input.third

    # Нажимаем кнопку Submit
    browser.find_element(By.XPATH, '//button[@type="submit"]').click() # CSS button[type=submit]
    time.sleep(3)

    # Проверяем прошла ли регистрация
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1") # находим элемент, содержащий текст
    welcome_text = welcome_text_elt.text # записываем в переменную welcome_text текст из элемента welcome_text_elt

    # C помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    print('Регистрация успешно пройдена')

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
