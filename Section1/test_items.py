import pytest
import time
from selenium.webdriver.common.by import By

# По умолчанию запускается в хроме с русским языком, пример запуска с французским: pytest --language=fr test_items.py

def test_check_button(browser):
    browser.implicitly_wait(3)
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    button_add_to_basket = browser.find_elements(By.CSS_SELECTOR, 'button[class="btn btn-lg btn-primary btn-add-to-basket"]')
    if len(button_add_to_basket) > 0:
        print(f'Кнопка добавления в корзину присутствует, текст на кнопке {button_add_to_basket[0].text}'
              f'Браузер закроется через 30 секунд')
    else:
        assert False, 'Кнопка добавления в корзину не найдена'
    time.sleep(30)

if __name__ == "__main__":
    pytest.main()