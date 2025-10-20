sandwich_orders = ["Pastrami", "Tuna", "Chicken Teriyaki", "Pastrami", "Ham", "Pepperoni", "Philly cheese steak",
                   "Pastrami"]
print("The deli has run out of pastrami")
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
print(sandwich_orders)