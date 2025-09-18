import pytest
import time, math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with open("login.txt") as file:  # чтение файла txt с двумя строками. 1я email, 2я password
    data = file.readlines()  # файл login.txt должен находиться в папке с этим проектом
    text = ""


@pytest.fixture(scope="class")  # тесты так же работают со scope="function"
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    print(text)  # вывод нужного текста в консоль


class TestLoginAndAnswer:

    @pytest.mark.parametrize("link", [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"
    ])
    def test_website_autorization_wait_for_modal_close(self, driver, link):

        global text
        driver.get(link)
        driver.implicitly_wait(3)
        wait = WebDriverWait(driver, 3)

        # ниже проверка на введёную уч. запись. Если нет, то логинится.
        check_exist = len(driver.find_elements(By.CSS_SELECTOR, ".navbar__profile"))
        if check_exist == 0:  # проверка присутствия элемента, если check_exist == 0: отсутствует.
            driver.find_element(By.CSS_SELECTOR, "#main-navbar .navbar__auth_login").click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".auth-widget.sign-form")))
            driver.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys(data[0])
            driver.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys(data[1])
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".sign-form__btn[type='submit']"))).click()
            wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".auth-widget.sign-form")))

        # ниже 2 строки это проверка на доступность text input. Если блок. то жмётся кнопка "решить снова".
        disabled = driver.find_element(By.CSS_SELECTOR, ".textarea").get_attribute('disabled')
        if disabled is not None: driver.find_element(By.CSS_SELECTOR, ".again-btn").click()

        answer = math.log(int(time.time()))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".textarea"))).send_keys(str(answer))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))).click()
        check = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints p"))).text
        if check != "Correct!": text += check

        assert "Correct!" == check, "Ответ не верный :)"


if __name__ == "__main__":
    pytest.main()