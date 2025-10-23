class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name} serves {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} has been opened.")

first_restaurant = Restaurant("Daikan", "japanese food")
print(first_restaurant.restaurant_name)
print(first_restaurant.cuisine_type)
first_restaurant.describe_restaurant()
first_restaurant.open_restaurant()

second_restaurant = Restaurant("MacDo", "fast food")
third_restaurant = Restaurant("Fontanella", "icecream")
second_restaurant.describe_restaurant()
third_restaurant.describe_restaurant()