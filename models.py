# ByteBites backend models
# Classes:
# - Customer: stores customer name and purchase history
# - MenuItem: stores item details
# - Menu: stores and manages a collection of menu items
# - Order: stores selected items and calculates totals

# ByteBites backend models
# Week 8 update:
# Added a lightweight recommendation feature so the system can
# suggest menu items based on category preferences and popularity.


class Customer:
    def __init__(self, name: str, favorite_category: str | None = None):
        self.name = name
        self.favorite_category = favorite_category
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

    def recommend_items(self, preferred_category: str, min_popularity: int = 0, top_k: int = 3):
        """
        Returns top menu recommendations based on:
        - matching the preferred category
        - popularity rating
        - lower price as a small tie-breaker

        This is a simple recommendation layer, not a full ML system.
        """
        scored_items = []

        for item in self.items:
            score = 0

            if item.category.lower() == preferred_category.lower():
                score += 5

            score += item.popularity_rating

            if item.popularity_rating >= min_popularity:
                scored_items.append((score, item))

        scored_items.sort(key=lambda pair: (-pair[0], pair[1].price, pair[1].name))
        return [item for _, item in scored_items[:top_k]]

    def recommend_for_customer(self, customer, min_popularity: int = 0, top_k: int = 3):
        """
        Recommends items using the customer's saved favorite category.
        """
        if not customer.favorite_category:
            return []
        return self.recommend_items(customer.favorite_category, min_popularity, top_k)


class Order:
    def __init__(self, customer=None):
        self.customer = customer
        self.items = []

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.price for item in self.items)