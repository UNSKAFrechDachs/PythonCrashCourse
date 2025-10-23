from restaurant import Restaurant, IceCreamStand

first_restaurant = Restaurant("Daikan", "japanese food")
second_restaurant = Restaurant("MacDo", "fast food")
third_restaurant = IceCreamStand("Fontanella", "icecream", ["Mango", "Strawberry", "Mint-Choco"])

print(first_restaurant.restaurant_name)
print(first_restaurant.cuisine_type)
first_restaurant.describe_restaurant()
first_restaurant.open_restaurant()
second_restaurant.describe_restaurant()
third_restaurant.describe_restaurant()
print(third_restaurant.number_served)
third_restaurant.set_number_served(3)
print(third_restaurant.number_served)
third_restaurant.increment_number_served(3)
print(third_restaurant.number_served)
third_restaurant.list_flavors()
