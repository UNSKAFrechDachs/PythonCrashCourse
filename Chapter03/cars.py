cars = ["bmw", "audi", "toyota", "subaru"]
print("Here is the original list:")
print(cars)

print("\n Here is the sorted list:")
print(sorted(cars, reverse=True))

print("\n Here is the original list again:")
print(cars)

cars.reverse()
print(cars)