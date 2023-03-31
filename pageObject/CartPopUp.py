from selenium.webdriver.common.by import By

class CartPopup:

    def __init__(self, driver):
        self.driver = driver

    # Cart Pop up
    proceedToCheckout = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")

    def goToCheckout(self):
        return self.driver.find_element(*CartPopup.proceedToCheckout)