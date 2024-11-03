
class Customer:
    def __init__(self, customer_id, name, address, contact,loyalty_member):
        self.__customer_id = customer_id
        self.__name = name
        self.__address = address
        self.__contact = contact
        self.__loyalty_member = loyalty_member
        self.my_cart = None

    def browse_books(self):
        pass

    def purchase_book(self):
        pass

    def assign_cart(self,cart):
        self.my_cart = cart

    def get_cart(self):
        return self.my_cart

    def get_customer_id(self):
        return self.__customer_id

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_contact(self):
        return self.__contact

    def set_contact(self, contact):
        self.__contact = contact

    def get_loyalty_member(self):
        return self.__loyalty_member

    def set_loyalty_member(self,lm):
        self.__loyalty_member = lm