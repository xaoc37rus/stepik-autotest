from faker import Faker
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/registration1.html"
fake = Faker()

try:
    # Создаем объект класса (браузер) и переходим по ссылке
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    #time.sleep(1)

    # Находим обязательные поля
    required_inputs = browser.find_elements(By.XPATH, '//div[@class="first_block"]//input') # //input[@required]
    # browser.find_elements(By.CSS_SELECTOR, 'div[class="first_block"] input') # CSS div.first_block input или input[required]
    #time.sleep(1)

    # проверка, что кол-во required полей совпадает с изначальным
    assert len(required_inputs) == 3

    # Заполняем обязательные поля
    for element in required_inputs:
        element.send_keys(fake.word())
    #time.sleep(1)

    # Нажимаем кнопку Submit
    browser.find_element(By.XPATH, '//button[@type="submit"]').click() # CSS button[type=submit]
    #time.sleep(1)

    # Проверяем прошла ли регистрация
    registration_result = browser.find_elements(By.XPATH, '//h1[contains(text(), "Congratulations! You have successfully registered!")]')
    if registration_result:
        print('Регистрация пройдена успешна')
    else:
        print('Регистрация не удалась')
    time.sleep(1)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
