cubes = [value ** 3 for value in range(1,11)]
for cube in cubes:
    print(cube)

print("The first three items in the list are: ")
for cube in cubes[:3]:
    print(cube)

print("Three items form the middle of the list are: ")
for cube in cubes[2:5]:
    print(cube)

print("The last three items in the list are: ")
for cube in cubes[-3:]:
    print(cube)