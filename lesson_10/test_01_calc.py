import allure
from selenium import webdriver

from pages.calculator_page import CalculatorPage


@allure.title("Проверка калькулятора")
@allure.description("Проверка результата вычисления 7 + 8")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc():

    driver = webdriver.Chrome()

    page = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        page.open()

    with allure.step("Установить задержку 45 секунд"):
        page.set_delay(45)

    with allure.step("Выполнить вычисление 7 + 8"):
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

    with allure.step("Проверить результат"):
        assert page.get_result() == "15"

    driver.quit()
