# Draft UML from Copilot

## Candidate Classes

### Customer
- name: str
- purchase_history: list

### MenuItem
- name: str
- price: float
- category: str
- popularity_rating: int

### Menu
- items: list[MenuItem]

### Order
- items: list[MenuItem]
- customer: Customer | None

## Relationships
- A `Menu` contains many `MenuItem` objects.
- An `Order` contains many `MenuItem` objects.
- A `Customer` has a purchase history of past `Order` objects.

## Notes
This draft is close to the feature request, but it should stay simple and avoid adding extra classes that were not requested.