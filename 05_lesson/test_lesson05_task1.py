from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def test_navigation():
    driver = webdriver.Chrome()

    driver.get("https://httpbin.org/")

    # Переход по ссылке HTML Forms
    driver.find_element(By.LINK_TEXT, "HTML form").click()
    sleep(5)

    # Проверка URL после перехода
    assert driver.current_url == "https://httpbin.org/forms/post"
    sleep(5)
    # Возврат назад
    driver.back()
    sleep(5)
    # Проверка возврата на исходную страницу
    assert driver.current_url == "https://httpbin.org/"

    driver.quit()
    sleep(10)
