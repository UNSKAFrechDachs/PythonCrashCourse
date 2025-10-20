poll_results ={}

while True:
    name = input("What is your name? ")
    destination = input("Where do you want to go? ")

    poll_results[name] = destination
    decision = input("Continue poll? (y/n)")
    if decision == "n": break

print("--- Poll Results ---")
for name, destination in poll_results.items():
    print(f"\n{name}")
    print(destination)
