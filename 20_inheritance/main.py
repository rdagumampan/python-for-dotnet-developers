import datetime


# create a base class to inherit
class BaseProduct:
    def __init__(self, sku, name, description):
        self.sku = sku
        self.name = name
        self.description = description

    def __repr__(self):
        return "{0} / {1} / {2}".format(self.sku, self.name, self.description)


# create concrete class with extended properties
class PerishableProduct(BaseProduct):
    def __init__(self, sku, name, description, expirationDate):
        # init overrides the parent ctor, so we have to call the base class
        BaseProduct.__init__(self, sku, name, description)
        self.expirationDate = expirationDate

    def __repr__(self):
        return "{0} / {1} / {2} /  {3}".format(self.sku, self.name, self.description, self.expirationDate)


class ApplianceProduct(BaseProduct):
    def __init__(self, sku, name, description, warrantyExpiration):
        # init overrides the parent ctor, so we have to call the base class
        BaseProduct.__init__(self, sku, name, description)
        self.warrantyExpiration = warrantyExpiration

    def __repr__(self):
        return "{0} / {1} / {2} /  {3}".format(self.sku, self.name, self.description, self.warrantyExpiration)


perishableProduct = PerishableProduct("SKU01", "Fresh Milk", "Fresh milk from organic farm.",
                                      datetime.datetime.utcnow())
print(perishableProduct);

applianceProduct = ApplianceProduct("SKU02", "Washing Machine", "Front load washing machine.",
                                    datetime.datetime.utcnow())
print(applianceProduct);

# store all products in container
products = [perishableProduct, applianceProduct]
for product in products:
    print(product)
