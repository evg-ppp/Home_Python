import allure
import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    """Создает экземпляр браузера Firefox и закрывает его после теста."""
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Покупка товаров")
@allure.description("Проверка полного процесса оформления заказа")
@allure.feature("Checkout")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver):
    """Проверка успешного оформления заказа."""

    # Создание объектов страниц
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    with allure.step("Открыть страницу авторизации"):
        login.open()

    with allure.step("Войти под зарегистрированным пользователем"):
        login.login()

    with allure.step("Добавить товары в корзину"):
        inventory.add_backpack()
        inventory.add_tshirt()
        inventory.add_onesie()

    with allure.step("Открыть корзину"):
        inventory.open_cart()

    with allure.step("Перейти к оформлению заказа"):
        cart.checkout()

    with allure.step("Заполнить данные покупателя"):
        checkout.fill_form()

    with allure.step("Получить итоговую стоимость заказа"):
        total = checkout.get_total()

    with allure.step("Проверить итоговую стоимость заказа"):
        total = checkout.get_total()
        assert total == 58.29
