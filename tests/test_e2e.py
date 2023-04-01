import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.CartDetailsPage import CartDetailsPage
from pageObject.CartPopUp import CartPopup
from pageObject.ProductPage import ProductPage
from utilities.BaseClass import BaseClass


class TestBasic(BaseClass):

    def test_e2e(self):

        # changes made to git
        productPage = ProductPage(self.driver)
        cartPage = CartDetailsPage(self.driver)

        # Search product based on productName and add items to Cart
        productPage.searchProduct("ber")
        productPage.addSearchedItemsToCart()

        # click on image icon  and proceed to checkout
        productPage.navigateToCheckoutPage()

        # get all product name
        cartPage.getAllAddedProductName()

        # get all prices and sum it
        cartPage.calculateExpectedSum()

        # Apply discount using coupon code
        cartPage.applyCouponCodeAndWait()
        cartPage.getActualTotalAmount()

        # Validate the applied discount
        cartPage.validateDiscount()
