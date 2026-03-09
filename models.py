# ByteBites backend models
# Classes:
# - Customer: stores customer name and purchase history
# - MenuItem: stores item details
# - Menu: stores and manages a collection of menu items
# - Order: stores selected items and calculates totals


class Customer:
    def __init__(self, name: str):
        self.name = name
        self.purchase_history = []

    def add_purchase(self, order):
        self.purchase_history.append(order)


class MenuItem:
    def __init__(self, name: str, price: float, category: str, popularity_rating: int):
        self.name = name
        self.price = float(price)
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def filter_by_category(self, category: str):
        return [item for item in self.items if item.category.lower() == category.lower()]

    def sort_by_popularity(self, descending: bool = True):
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=descending)


class Order:
    def __init__(self, customer=None):
        self.customer = customer
        self.items = []

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.price for item in self.items)