import random

result_set = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e"]

def draw_ticket(length=4):
    result = ""
    for _ in range(length):
        result += random.choice(result_set)
    return result

result = draw_ticket()
print(f"The ticket that matches these 4 numbers: {result}, wins a prize!")

my_ticket = "1234"

counter = 0
while True:
    counter += 1
    if draw_ticket() == my_ticket: break

print(f"The ticket was: {my_ticket}.")
print(f"It took {counter} draws.")