
from datetime import datetime

class Order:
    def __init__(self, items):
        self.__items = items
        self.__order_date = datetime.now()

    def get_total_price(self):
        '''
        This method calculates the total price of the items in the order
        and returns the total amount

        '''
        total = 0
        for item,quantity in self.__items.items():
            total += (quantity*item.get_price())
        return total

    def get_total_ebooks(self):
        '''
        This method calculates the total number of books ordered and return it.

        '''
        number_of_books = 0
        for item,quantity in self.__items.items():
            number_of_books += quantity
        return number_of_books
    
    # getter and setter methods
    def get_items(self):
        return self.__items

    def set_items(self,items):
        self.__items = items

    def get_order_date(self):
        return self.__order_date

    def set_order_date(self,order_date):
        self.__order_date = order_date
