class LoyaltyProgram:
    def __init__(self, discount_rate=0.1, bulk_discount_rate=0.2):
        self.__discount_rate = discount_rate
        self.__bulk_discount_rate = bulk_discount_rate

    def get_loyalty_discount(self):
        return self.__discount_rate

    def set_loyalty_discount(self,d):
        self.__discount_rate = d

    def get_bulk_discount(self):
        return self.__bulk_discount_rate

    def set_bulk_discount(self,bd):
        self.__bulk_discount_rate = bd