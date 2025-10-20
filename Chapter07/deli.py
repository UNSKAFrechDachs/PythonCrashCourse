sandwich_orders = ["Tuna", "Chicken Teriyaki", "Ham", "Pepperoni", "Philly cheese steak"]
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()
    finished_sandwiches.append(order)
    print(f"I made your {order} sandwich!")