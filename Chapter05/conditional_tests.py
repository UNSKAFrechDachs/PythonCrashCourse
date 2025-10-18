name = "strandberg"
price = 1799
strings = 7
pickups = "Fishman"
cool_manufacturers = ["esp", "schecter", "ibanez"]

print("is the brand Mayones? I predict True")
print(name.lower() == "mayones")

print("\nis the brand Strandberg? I predict True")
print(name.lower() == "strandberg")

print("\nis it cheaper than 2000€? I predict False")
print(price < 2000)

print("\nis it more expensive than 1000€? I predict True")
print(price > 1000)

print("\ndoes it have 6 strings? I predict True")
print(strings == 6)

print("\ndoes it have less than 6 strings? I predict False")
print(strings < 6)

print("\ndoes it have no strings? I predict False")
print(strings == 0)

print("\n does it have 7 strings? I predict True")
print(strings == 7)

print("\ndoes it have emg pickups? I predict True")
print(pickups.lower() == "emg")

print("\ndoes it have fishman fluence? I predict False")
print(pickups.lower() == "fishman")

print("\nis the price between 1500€ and 2000€? I predict True")
print(1500 < price < 2000)

print("\nis it a 7 or 8 string guitar? I predict True")
print(strings == 7 or strings == 8)

print("\nis it made by schecter and has Fishman pickups? I predict False")
print(name.lower() == "schecter" and pickups.lower() == "fishman")

print("\nis it made by a cool manufacturer? I predict True")
print(name in cool_manufacturers)

print("\nis it not made by a cool manufacturer? I predict False")
print(name not in cool_manufacturers)