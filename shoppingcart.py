
class ShoppingCart:
    def __init__(self):
        self.__items = {}

    def get_items(self):
        return self.__items

    def add_item(self, ebook, quantity=1):
        if ebook in self.__items:
            self.__items[ebook] += quantity
        else:
            self.__items[ebook] = quantity

    def remove_item(self, ebook):
        if ebook in self.__items:
            del self.__items[ebook]

    def clear_cart(self):
        self.__items.clear()