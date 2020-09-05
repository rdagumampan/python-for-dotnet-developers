class Anonymous(dict):
    __getattr = dict.get
    __setattr = dict.__setitem__


customer = Anonymous(name="Rodel Dagumampan", address="Gladsaxe, Denmark", contact_no="1234-5678")
print(customer)
print(customer["name"])
print(customer.name)

