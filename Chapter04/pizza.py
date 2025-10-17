pizzas = ["Pepperoni", "Tuna", "Hawaii"]

for pizza in pizzas:
    print(f"I like {pizza} pizza")
print("\nI really like pizza")

friend_pizzas = pizzas[:]

pizzas.append("Diavolo")
friend_pizzas.append("Sucuk")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)