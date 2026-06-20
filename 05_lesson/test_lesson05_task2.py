
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")
    # Сохраняем исходный URL
    initial_url = driver.current_url
    sleep(5)
    # Ввод имени в поле custname
    driver.find_element(By.NAME, "custname").send_keys("Евгений")
    sleep(5)
    # Нажатие кнопки Submit
    driver.find_element(By.XPATH, "//button[text()='Submit order']").click()
    sleep(5)
    # Проверка, что URL изменился
    assert driver.current_url != initial_url
    sleep(5)

    driver.quit()
    sleep(5)
