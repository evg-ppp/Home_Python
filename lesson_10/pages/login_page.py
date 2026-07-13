from selenium.webdriver.common.by import By


class LoginPage:
    """Класс для работы со страницей авторизации."""

    def __init__(self, driver) -> None:
        """
        Инициализация страницы.

        :param driver: Экземпляр WebDriver.
        """
        self.driver = driver

    def open(self) -> None:
        """Открывает страницу авторизации."""
        self.driver.get("https://www.saucedemo.com/")

    def login(self) -> None:
        """Выполняет вход под зарегистрированным пользователем."""
        self.driver.find_element(
            By.ID,
            "user-name"
        ).send_keys("standard_user")

        self.driver.find_element(
            By.ID,
            "password"
        ).send_keys("secret_sauce")

        self.driver.find_element(
            By.ID,
            "login-button"
        ).click()
