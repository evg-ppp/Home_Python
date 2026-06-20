from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_saucedemo_total():
    options = Options()
    driver = webdriver.Firefox(options=options)

    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    items = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie",
    ]

    for item in items:
        driver.find_element(
            By.XPATH,
            f"//div[text()='{item}']/ancestor::div"
            f"[@class='inventory_item']//button"
        ).click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Evgeniy")
    driver.find_element(By.ID, "last-name").send_keys("Pitonov")
    driver.find_element(By.ID, "postal-code").send_keys("101000")

    driver.find_element(By.ID, "continue").click()

    total_text = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_total_label")
        )
    ).text

    total = total_text.replace("Total: ", "")

    assert total == "$58.29", f"Ожидалось $58.29, получено {total}"

    driver.quit()
