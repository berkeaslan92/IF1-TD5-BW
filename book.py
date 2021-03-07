from enum import Enum
from functools import total_ordering
from operator import itemgetter, attrgetter

class Side(Enum):
    SELL = 0
    BUY = 1

@total_ordering
class Order:

    prio = 0

    def __init__(self, quantity, price, side):
        self.quantity = quantity
        self.price = price
        self.side = side
        Order.prio += 1
        self.priority = Order.prio

    def __eq__(self, other):
        return other and self.quantity == other.quantity and self.price == other.price and self.side == other.side

    def __lt__(self, other):
        return lambda self, other: self.price < other.price

    def __str__(self):
        return "Quantity: %s // Price: %s // Side: %s // Priority: %s" % (self.quantity, self.price, self.side, self.priority)

class Book:

  def __init__ (self, name):
    self.name = name
    self.book = []

  def transaction_execution(self):
    # while self.book
    # condition pour remove l'ordre
    # comparer les quantités pour index 1 et index n, si condition => remove l'ordre

    while self.book[0].price <= self.book[-1].price:

      number_of_orders_in_book = len(self.book)
      best_buy = self.book[number_of_orders_in_book-1]
      best_sell = self.book[0]
      print(best_buy)
      print(best_sell)


      # If the quantities are equal
      if best_buy.quantity == best_sell.quantity:
        print(f"Transaction executed : {best_buy.quantity} at {best_buy.price}")
        self.book.remove(best_buy)
        self.book.remove(best_sell)

      # If best buy quantity > best sell quantity
      elif best_buy.quantity > best_sell.quantity:
        print(f"Transaction executed : {best_sell.quantity} at {best_buy.price}")
        best_buy.quantity = best_buy.quantity - best_sell.quantity
        self.book.remove(best_sell)

      else:
        print(f"Transaction executed : {best_buy.quantity} at {best_buy.price}")
        best_sell.quantity = best_sell.quantity - best_buy.quantity
        self.book.remove(best_buy)

  def insert_sell(self, quantity, price):
    self.book.append(Order(quantity, price, 0))
    print(f"INSERT SELL ORDER: {self.book[-1]}")
    self.book.sort(key=lambda x: (x.side, x.price, -x.priority))
    if len(self.book) > 1:
      self.transaction_execution()
    self.print_order()

  def insert_buy(self, quantity, price):
    self.book.append(Order(quantity, price, 1))
    print(f"INSERT BUY ORDER: {self.book[-1]}")
    self.book.sort(key=lambda x: (x.side, x.price, -x.priority))
    if len(self.book) > 1:
      self.transaction_execution()
    self.print_order()

  def print_order(self):
    print(f"Book on {self.name}")
    for i in self.book:
      print(i)
    print("\n")
