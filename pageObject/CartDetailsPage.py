from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CartDetailsPage:

    def __init__(self, driver):
        self.driver = driver

    productlist = []
    expectedSum = 0
    actualTotalAmt = 0

    # Cart Details page
    productlistElement = (By.CSS_SELECTOR, "p.product-name")
    priceList = (By.XPATH, "//tr/td[5]/p")
    actualTotalAmt = (By.CSS_SELECTOR, ".totAmt")
    promoCode = (By.CSS_SELECTOR, ".promoCode")
    promoBtn = (By.CSS_SELECTOR, ".promoBtn")
    promoInfo = (By.CSS_SELECTOR, ".promoInfo")
    discountAmt = (By.CSS_SELECTOR, ".discountAmt")

    def getProductNameList(self):
        return self.driver.find_elements(*CartDetailsPage.productlistElement)

    def getPriceList(self):
        return self.driver.find_elements(*CartDetailsPage.priceList)

    def getActualTotalAmt(self):
        return self.driver.find_element(*CartDetailsPage.actualTotalAmt)

    def getPromoCode(self):
        return self.driver.find_element(*CartDetailsPage.promoCode)

    def getPromoBtn(self):
        return self.driver.find_element(*CartDetailsPage.promoBtn)

    def getPromoInfo(self):
        return self.driver.find_element(*CartDetailsPage.promoInfo)

    def getDiscountAmt(self):
        return self.driver.find_element(*CartDetailsPage.discountAmt)

    def getAllAddedProductName(self):
        # get all product name
        productlistElement = self.getProductNameList()
        for product in productlistElement:
            CartDetailsPage.productlist.append(product.text)

        print(CartDetailsPage.productlist)

    def applyCouponCodeAndWait(self):
        # Apply discount using coupon code
        self.getPromoCode().send_keys("rahulshettyacademy")
        self.getPromoBtn().click()

        # check discount amount is less than original amount
        wait = WebDriverWait(self.driver, 8)
        # wait.until(expected_conditions.presence_of_element_located((*cartPage.promoInfo)))
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

    def calculateExpectedSum(self):
        # get all prices and sum it
        amounts = self.getPriceList()

        CartDetailsPage.expectedSum = 0
        for amount in amounts:
            CartDetailsPage.expectedSum = CartDetailsPage.expectedSum + int(amount.text)

        myamount = "The total amount is {0}"
        print(myamount.format(CartDetailsPage.expectedSum))

        actualTotalAmt = int(self.getActualTotalAmt().text)
        assert CartDetailsPage.expectedSum == actualTotalAmt
        return CartDetailsPage.expectedSum

    def getActualTotalAmount(self):
        CartDetailsPage.actualTotalAmt = int(self.getActualTotalAmt().text)
        print("The expectedSum amount is : " + str(CartDetailsPage.expectedSum))
        print("The actual Total amount is : " + str(CartDetailsPage.actualTotalAmt))
        assert CartDetailsPage.expectedSum == CartDetailsPage.actualTotalAmt

    def validateDiscount(self):
        discountedTotalAmt = float(self.getDiscountAmt().text)
        print("The asserted discounted Total amount is : " + str(discountedTotalAmt) + " lesser than " + str(CartDetailsPage.actualTotalAmt))
        assert discountedTotalAmt < CartDetailsPage.actualTotalAmt
