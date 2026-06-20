import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    driver.maximize_window()  # Развернуть окно браузера на весь экран

    # 1. Откройте страницу
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # Пауза только для наблюдения
    time.sleep(3)

    # 2. Найдите и нажмите кнопку Start
    start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_button.click()

    # 3. Дождитесь появления текста Hello World!
    hello_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
    )

    # 4. Сделайте скриншот страницы
    driver.save_screenshot("hello_world.png")

    # 5. Проверьте текст
    assert hello_text.text == "Hello World!"

    driver.quit()
