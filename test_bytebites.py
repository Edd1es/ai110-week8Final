from models import Customer, MenuItem, Menu, Order


def test_calculate_total_with_multiple_items():
    burger = MenuItem("Burger", 10.0, "Entrees", 5)
    soda = MenuItem("Soda", 5.0, "Drinks", 4)

    order = Order()
    order.add_item(burger)
    order.add_item(soda)

    assert order.calculate_total() == 15.0


def test_order_total_is_zero_when_empty():
    order = Order()
    assert order.calculate_total() == 0


def test_filter_menu_items_by_category():
    menu = Menu()
    burger = MenuItem("Burger", 10.0, "Entrees", 5)
    soda = MenuItem("Soda", 5.0, "Drinks", 4)
    cake = MenuItem("Cake", 6.0, "Desserts", 3)

    menu.add_item(burger)
    menu.add_item(soda)
    menu.add_item(cake)

    drinks = menu.filter_by_category("Drinks")

    assert len(drinks) == 1
    assert drinks[0].name == "Soda"


def test_customer_purchase_history_updates():
    customer = Customer("Eddie")
    order = Order(customer)

    customer.add_purchase(order)

    assert len(customer.purchase_history) == 1
    assert customer.purchase_history[0] == order


def test_recommend_items_prioritizes_matching_category():
    menu = Menu()
    burger = MenuItem("Burger", 10.0, "Entrees", 5)
    soda = MenuItem("Soda", 5.0, "Drinks", 4)
    fries = MenuItem("Fries", 4.0, "Entrees", 3)

    menu.add_item(burger)
    menu.add_item(soda)
    menu.add_item(fries)

    recommendations = menu.recommend_items("Entrees", top_k=2)

    assert len(recommendations) == 2
    assert recommendations[0].category == "Entrees"
    assert recommendations[1].category == "Entrees"


def test_recommend_items_uses_popularity_within_category():
    menu = Menu()
    burger = MenuItem("Burger", 10.0, "Entrees", 5)
    fries = MenuItem("Fries", 4.0, "Entrees", 3)

    menu.add_item(burger)
    menu.add_item(fries)

    recommendations = menu.recommend_items("Entrees", top_k=2)

    assert recommendations[0].name == "Burger"
    assert recommendations[1].name == "Fries"


def test_recommend_for_customer_uses_favorite_category():
    menu = Menu()
    burger = MenuItem("Burger", 10.0, "Entrees", 5)
    soda = MenuItem("Soda", 5.0, "Drinks", 4)

    menu.add_item(burger)
    menu.add_item(soda)

    customer = Customer("Eddie", favorite_category="Drinks")
    recommendations = menu.recommend_for_customer(customer, top_k=1)

    assert len(recommendations) == 1
    assert recommendations[0].name == "Soda"


def test_recommend_for_customer_returns_empty_without_preference():
    menu = Menu()
    menu.add_item(MenuItem("Burger", 10.0, "Entrees", 5))

    customer = Customer("Eddie")
    recommendations = menu.recommend_for_customer(customer)

    assert recommendations == []