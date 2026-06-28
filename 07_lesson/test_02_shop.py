import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop():
    driver = webdriver.Firefox()
    driver.maximize_window()

    # страницы
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    # 1. открыть сайт + логин
    login.open()
    login.login()

    # 2. добавить товары
    inventory.add_backpack()
    inventory.add_tshirt()
    inventory.add_onesie()

    # 3. корзина
    inventory.open_cart()

    # 4. checkout
    cart.checkout()

    # 5. заполнение формы
    checkout.fill_form()

    # 6. итог
    total = checkout.get_total()

    # 7. проверка
    assert total == 58.29

    driver.quit()
