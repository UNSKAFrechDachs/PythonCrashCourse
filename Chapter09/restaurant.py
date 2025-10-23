class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name} serves {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} has been opened.")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served):
        self.number_served += number_served


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors = ["Vanilla"]):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def list_flavors(self):
        print("These flavors are available:")
        for flavor in self.flavors:
            print(f"\t- {flavor}")


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

