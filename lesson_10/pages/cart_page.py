from selenium.webdriver.common.by import By


class CartPage:
    """Класс для работы со страницей корзины."""

    def __init__(self, driver) -> None:
        """
        Инициализация страницы.

        :param driver: Экземпляр WebDriver.
        """
        self.driver = driver

    def checkout(self) -> None:
        """Переходит к оформлению заказа."""
        self.driver.find_element(By.ID, "checkout").click()
