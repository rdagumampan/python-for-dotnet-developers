class CartItem:
    def __init__(self, name, price, quantity):
        self.quantity = quantity
        self.price = price
        self.name = name

    def __repr__(self):
        return "{0}, ${1}".format(self.name, self.price)


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, cart_item):
        self.items.append(cart_item)

    def total_price(self):
        total = 0.00

        for item in self.items.__iter__():
            total += item.price
        return total


cart = ShoppingCart()
cart.add_item(CartItem("milk", 12.25, 1))
cart.add_item(CartItem("bread", 15.50, 1))

print ("total: ${0}".format(cart.total_price()))
for item in cart.items:
    print(item)
