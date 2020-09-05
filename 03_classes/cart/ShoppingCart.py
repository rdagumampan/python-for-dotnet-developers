class ShoppingCart:
    def __init__(self, session_id):
        self.session_id = session_id

    def __repr__(self):
        return "Cart id: {0}".format(self.session_id)
