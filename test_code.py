
# importing all the modules to be used
from bookstore import BookStore
from loyaltyprogram import LoyaltyProgram
from book import Book
from customer import Customer
from shoppingcart import ShoppingCart
from order import Order

# creating a book store object
store = BookStore("The Book Store","street 1 home town near main read")

# creating book objects
book1 = Book("Introduction to Physics", "Isaac Newton", "2005", "Science", 15.99)
book2 = Book("Basic Chemistry", "Marie Curife", "2010", "Science", 12.99)
book3 = Book("Advanced Mathematics", "Carl Gauss", "2018", "Mathematics", 20.99)
book4 = Book("World History", "Herodotus", "2015", "History", 18.99)
book5 = Book("Introduction to Biology", "Charles Darwin", "2012", "Science", 14.99)

# adding books into store
store.add_book(book1,3)
store.add_book(book2,5)
store.add_book(book3,2)
store.add_book(book4,7)
store.add_book(book5,3)

# registering the customers into store
store.register_customer(1, "Mohammed", "UAE", "+971501234567", True)
store.register_customer(2, "Ahmed", "UAE", "+971502345678", False)
store.register_customer(3, "Hamad", "UAE", "+971503456789", True)
store.register_customer(4, "Khalid", "UAE", "+971504567890", False)
store.register_customer(5, "Salim", "UAE", "+971505678901", True)

# creating cart for customer 1 and adding books into cart
cart = ShoppingCart()
store.assign_cart_to_customer(cart,customer_id=1)
cart.add_item(book1,2)
cart.add_item(book3,1)

# placing the order and showing the invoice returned by the function
print(store.place_order(1))

# creating cart for customer 2 and adding books into cart
cart2 = ShoppingCart()
store.assign_cart_to_customer(cart2,customer_id=2)
cart2.add_item(book2,2)
cart2.add_item(book3,1)
cart2.add_item(book4,2)
cart2.add_item(book5,1)

# placing the order and showing the invoice returned by the function
print(store.place_order(2))
