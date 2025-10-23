from die import Die

d6 = Die(6)
d10 = Die(10)
d20 = Die(20)

print("D6")
for _ in range(10):
    print(d6.roll_die())
print("D10")
for _ in range(10):
    print(d10.roll_die())
print("D20")
for _ in range(10):
    print(d20.roll_die())
