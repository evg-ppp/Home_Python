from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = (
    "https://bonigarcia.dev/"
    "selenium-webdriver-java/"
    "slow-calculator.html"
)


class CalculatorPage:
    """Класс для работы со страницей калькулятора."""

    def __init__(self, driver) -> None:
        """
        Инициализация страницы.

        :param driver: Экземпляр WebDriver.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self) -> None:
        """Открывает страницу калькулятора."""
        self.driver.get(URL)

    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает задержку вычисления.

        :param seconds: Время задержки в секундах.
        """
        delay = self.driver.find_element(By.ID, "delay")
        delay.clear()
        delay.send_keys(str(seconds))

    def click_button(self, value: str) -> None:
        """
        Нажимает кнопку калькулятора.

        :param value: Значение кнопки.
        """
        self.driver.find_element(
            By.XPATH,
            f"//span[text()='{value}']"
        ).click()

    def get_result(self) -> str:
        """
        Возвращает результат вычисления.

        :return: Результат на экране калькулятора.
        """
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"),
                "15"
            )
        )

        return self.driver.find_element(
            By.CLASS_NAME,
            "screen"
        ).text
