from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = (
    "https://bonigarcia.dev/"
    "selenium-webdriver-java/"
    "slow-calculator.html"
)


class CalculatorPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self):
        self.driver.get(
            URL
        )

    def set_delay(self, seconds):
        delay = self.driver.find_element(
                 By.ID,
                 "delay"
        )
        delay.clear()
        delay.send_keys(str(seconds))

    def click_button(self, value):
        self.driver.find_element(
            By.XPATH,
            f"//span[text()='{value}']"
        ).click()

    def get_result(self):
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
