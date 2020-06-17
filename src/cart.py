class Cart:
    """
        main Cart class representing the set of product selected by the customer
    """

    def __init__(self):
        self.__products = []
        self.__percentageDiscount = 0.0
        self.__bundle = []
        self.__discount = 0.0

    def __repr__(self):
        return f"The products in the cart are {self.__products}"

    def addProductsAvailable(self, productAvailable):
        self.__productsAvailable = productAvailable

    def addBundlesAvailable(self, bundlesAvailable):
        self.__bundlesAvailable = bundlesAvailable

    def addProductsInCart(self, expectedProducts):
        self.__products.extend(expectedProducts)

    def getDiscount(self):
        self.__findTheBundleWithMaxDiscount()
        self.__sixPercentIfNoBundleAndMoreThanFive()
        self.__calculateDiscount()
        return self.__discount

    def __findTheBundleWithMaxDiscount(self):
        for bundle in self.__bundlesAvailable:
            if self.__checkBundleProductsInCart(bundle.products):
                if bundle.discount > self.__percentageDiscount:
                    self.__percentageDiscount = bundle.discount
                    self.__bundle = bundle.products

    def __checkBundleProductsInCart(self, bundle_products):
        if not bundle_products:
            raise ValueError("Empty Bundle not expected.")

        return all(product in self.__products for product in bundle_products)

    def __sixPercentIfNoBundleAndMoreThanFive(self):
        if self.__percentageDiscount == 0.0 and len(self.__products) > 5:
            self.__percentageDiscount = 0.06
            self.__bundle = self.__products

    def __calculateDiscount(self):
        for cart_product in self.__products:
            if cart_product in self.__productsAvailable.keys():
                if self.__productsAvailable[cart_product].sku in self.__bundle:
                    self.__discount += (
                        self.__productsAvailable[cart_product].price
                        * self.__percentageDiscount
                    )

        self.__discount = round(self.__discount, 2)

    @staticmethod
    def fillCartAndComputeDiscount(
        productsAvailable, bundlesAvailable, expectedProducts
    ):
        cart = Cart()

        cart.addProductsAvailable(productsAvailable)
        cart.addBundlesAvailable(bundlesAvailable)

        cart.addProductsInCart(expectedProducts)

        discount = cart.getDiscount()

        return discount
