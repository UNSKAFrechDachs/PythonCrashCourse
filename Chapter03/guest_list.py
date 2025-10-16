guests = ["Zeus", "Thanatos", "Kratos"]

for guest in guests:
    print(f"Hello dear {guest.title()}, \nI'd like to invite you to dinner.")

print(f"Kratos can't come.")
guests[-1] = "Venus"

for guest in guests:
    print(f"Hello dear {guest.title()}, \nI'd like to invite you to dinner.")

print("I have just been informed, that we have a bigger table.")

guests.insert(0, "Zagreus")
guests.insert(3, "Gaia")
guests.append("Ceres")
print(f"I will have {len(guests)} guests.")
for guest in guests:
    print(f"Hello dear {guest.title()}, \nI'd like to invite you to dinner.")

print("The new table won't arrive in time, so there will only be space for two.")
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest} you can't come.")
for guest in guests:
    print(f"Hello dear {guest.title()}, \nI'd like to invite you to dinner.")

del guests[0]
del guests[0]
print(guests)