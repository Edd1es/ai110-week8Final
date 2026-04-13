# ByteBites Final Design

## Updated System Overview

For the week 8 version of ByteBites, I kept the original backend structure from week 3 and added a lightweight recommendation feature. The main idea is that the system can now suggest menu items based on a customer's favorite category and the popularity of each item. This makes the app feel a little smarter while still staying simple and readable.

## UML-Style Class Diagram

### Customer
- name: str
- favorite_category: str | None
- purchase_history: list[Order]

Methods:
- add_purchase(order)

### MenuItem
- name: str
- price: float
- category: str
- popularity_rating: int

### Menu
- items: list[MenuItem]

Methods:
- add_item(item)
- filter_by_category(category)
- sort_by_popularity(descending=True)
- recommend_items(preferred_category, min_popularity=0, top_k=3)
- recommend_for_customer(customer, min_popularity=0, top_k=3)

### Order
- customer: Customer | None
- items: list[MenuItem]

Methods:
- add_item(item)
- calculate_total()

## Relationships

- `Menu` has many `MenuItem` objects.
- `Order` has many `MenuItem` objects.
- `Customer` has many past `Order` objects in purchase history.
- `Order` may optionally belong to one `Customer`.
- `Menu` now also uses customer preferences to generate recommendations.

## Data Flow

1. A customer is created with an optional favorite category.
2. Menu items are stored inside the menu.
3. The menu checks each item against the customer's preferred category.
4. Matching category items get a bigger score boost.
5. Popularity rating is also added into the score.
6. The system sorts items by score and returns the top recommendations.

## Design Rationale

I kept the original design simple because the week 3 ByteBites project was already centered around clear class responsibilities. Instead of adding a totally new complicated class, I extended the `Menu` class with recommendation methods since it already manages the collection of menu items. That made the feature easier to test and easier to explain. The recommendation logic is not machine learning, but it still acts like a small intelligent layer because it ranks results based on user preference plus popularity.