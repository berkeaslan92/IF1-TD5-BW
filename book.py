from enum import Enum
from functools import total_ordering

class Side(Enum):
    SELL = 0
    BUY = 1

@total_ordering
class Order:
    def __init__(self, quantity, price, side):
        self.quantity = quantity
        self.price = price
        self.side = side
        self.priority = 0

    def __eq__(self, other):
        return other and self.quantity == other.quantity and self.price == other.price and self.side = other.side

    def __lt__(self, other):
        return other and self.price < other.price and self.side == other.side

    def __str__(self):
        return "%s @ %s" % (self.quantity, self.price)

    def __repr__(self):
        return "Order(%s, &s)" % (self.quantity, self.price)


