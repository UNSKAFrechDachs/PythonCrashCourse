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
    def __init__(self, restaurant_name, cuisine_type, flavors=["Vanilla"]):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def list_flavors(self):
        print("These flavors are available:")
        for flavor in self.flavors:
            print(f"\t- {flavor}")
