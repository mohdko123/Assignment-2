from loyaltyprogram import LoyaltyProgram
from customer import Customer
from order import Order

class BookStore:
    def __init__(self,name,location):
        self.__name = name
        self.__location = location
        self.customers = []
        self.books = []
        self.quantity = []
        self.orders = []
        self.loyalty_program = LoyaltyProgram()
        self.vat = 0.08

    def __str__(self):
        return "Store {} Address {}\nOrders : {}\nBooks : {}".format(self.get_name(),self.get_location(),len(self.orders),len(self.books))

    def add_book(self,book,quantity):
        self.books.append(book)
        self.quantity.append(quantity)

    def remove_book(self,book):
        if book in self.books:
            book_idx = self.books.index(book)
            quantity = self.quantity[book_idx]
            if quantity > 0:
                self.quantity[book_idx] = quantity-1
            else:
                self.quantity.pop(book_idx)
                self.books.pop(book_idx)
        else:
            print("book not found")

    def register_customer(self,customer_id, name, address, contact,loyalty_member):
        customer = Customer(customer_id, name, address, contact,loyalty_member)
        self.customers.append(customer)

    def remove_customer(self,customer_id):
        for i in self.customers:
            if i.get_customer_id() == customer_id:
                self.customers.remove(i)
                print("customer removed")
                return
        print("customer not found")

    def assign_cart_to_customer(self,cart,customer_id):
        for i in self.customers:
            if i.get_customer_id() == customer_id:
                i.assign_cart(cart)
                print("cart assigned")
                return
        print("customer not found")

    def place_order(self,customer_id):

        order_items = {}

        for i in self.customers:
            if i.get_customer_id() == customer_id:
                cart = i.get_cart()
                if cart == None:
                    print("cart not found for the customer")
                else:
                    cart_items = cart.get_items()
                    # print(cart_items)
                    for item, quantity in cart_items.items():
                        if item in self.books:
                            book_idx = self.books.index(item)
                            book_quantity = self.quantity[book_idx]
                            if book_quantity >= quantity:
                                order_items[item] = quantity
                                print("book added into order")
                            else:
                                print("out of stock")

                order = Order(order_items)
                invoice = self.generate_invoice(order,i)
                return invoice

        print("customer not found")

    def generate_invoice(self,order,customer):
        original_total = order.get_total_price()
        if customer.get_loyalty_member():
            loyalty_discount = original_total * self.loyalty_program.get_loyalty_discount()
        else:
            loyalty_discount = 0

        total_books = order.get_total_ebooks()
        if total_books > 5:
            bulk_discount = original_total * self.loyalty_program.get_bulk_discount()
        else:
            bulk_discount = 0

        vat = original_total * self.vat

        final_total = original_total - (loyalty_discount + bulk_discount) + vat

        # Basic invoice string with .format() method
        invoice = "Invoice\n" \
                  "-----------------------------------\n" \
                  "Customer Name: {}\n" \
                  "Customer ID: {}\n" \
                  "Order Summary:\n" \
                  "Original Total:      USD {:.2f}\n" \
                  "Loyalty Member Discount:       -USD {:.2f}\n" \
                  "Bulk Discount:    USD {:.2f}\n" \
                  "VAT (8%):            USD {:.2f}\n" \
                  "-----------------------------------\n" \
                  "Total Amount Due:     USD {:.2f}\n" \
                  "-----------------------------------\n" \
                  "Thank you for shopping with {}!\n".format(
                      customer.get_name(),
                      customer.get_customer_id(),
                      original_total,
                      loyalty_discount,
                      bulk_discount,
                      vat,
                      final_total,
                      self.get_name()
                  )

        return invoice




    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def get_location(self):
        return self.__location

    def set_location(self,loc):
        self.__location = loc