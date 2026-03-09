# ByteBites Final Design

## UML-Style Class Diagram

### Customer
- name: str
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

## Design Rationale

These four classes directly match the data objects in the feature request. The design keeps responsibilities simple:
- `Customer` stores user identity and order history
- `MenuItem` stores item data
- `Menu` manages the full item collection
- `Order` groups selected items and computes totals