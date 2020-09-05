# import class declared in another file
# import classes from python package
from types import SimpleNamespace

# import class declared in another file in another directory
from cart.ShoppingCart import ShoppingCart
from classes import Customer

customer = Customer("Rodel", "Gladsaxe, Denmark", 12345678)
print("Welcome " + customer.name + " from " + customer.address)

shoppingCart = ShoppingCart("SESSION-12345678")
print("Your cart number is " + shoppingCart.session_id)

discount = SimpleNamespace(discount_code="PROMO-1234", discount_percent=25.50)
print("Your discount is {0} percent".format(discount.discount_percent))
