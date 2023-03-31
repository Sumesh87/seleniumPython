import time

from selenium.webdriver.common.by import By

from pageObject.CartPopUp import CartPopup


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    buttonlist = []


    # Homepage
    searchBoxTple = (By.CSS_SELECTOR, "input.search-keyword")
    cartBtnTple = (By.CSS_SELECTOR, "div.product-action>button")
    cartButtonTple = (By.XPATH, "//div/button[text()='ADD TO CART']")
    productNameTple = (By.XPATH, "parent::div/parent::div/h4")
    cartImageTple = (By.XPATH, "//img[@alt='Cart']")

    discountAmt = (By.CSS_SELECTOR, ".discountAmt")

    def searchItems(self):
        return self.driver.find_element(*ProductPage.searchBoxTple)

    def addToCart(self):
        return self.driver.find_elements(*ProductPage.cartBtnTple)

    def cartButton(self):
        return self.driver.find_elements(*ProductPage.cartButtonTple)

    def productName(self):
        return self.driver.find_element(*ProductPage.productNameTple)

    def cartImage(self):
        return self.driver.find_element(*ProductPage.cartImageTple)

    def searchProduct(self, productname):
        self.searchItems().send_keys(productname)
        time.sleep(2)

    def addSearchedItemsToCart(self):
        # Get list of searched products based on Cart button
        cartCount = len(self.addToCart())
        assert cartCount == 3
        cartButtons = self.cartButton()

        # Add all products in a loop
        for cart in cartButtons:
            # get the product name and add to a list
            ProductPage.buttonlist.append(cart.find_element(*self.productNameTple).text)
            cart.click()
        print(ProductPage.buttonlist)

    def navigateToCheckoutPage(self):
        # click on image icon
        time.sleep(1)
        self.cartImage().click()
        time.sleep(2)

        # click on proceed to checkout
        cartPop = CartPopup(self.driver)
        cartPop.goToCheckout().click()
        time.sleep(5)