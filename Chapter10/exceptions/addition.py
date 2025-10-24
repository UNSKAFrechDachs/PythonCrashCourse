while True:
    try:
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
    except ValueError:
        print("Sorry, you didn't enter a number.")
    else:
        print(first_number + second_number)
