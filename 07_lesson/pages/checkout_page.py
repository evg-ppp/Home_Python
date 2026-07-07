from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self):
        self.driver.find_element(By.ID, "first-name").send_keys("Ivan")
        self.driver.find_element(By.ID, "last-name").send_keys("Ivanov")
        self.driver.find_element(By.ID, "postal-code").send_keys("12345")
        self.driver.find_element(By.ID, "continue").click()

    def get_total(self):
        total_text = self.driver.find_element(
            By.CLASS_NAME, "summary_total_label").text
        return float(total_text.replace("Total: $", ""))
