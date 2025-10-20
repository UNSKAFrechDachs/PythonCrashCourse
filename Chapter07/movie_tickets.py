while True:
    message = input("""Tell me your age to get the ticket price
    (enter 'quit' to exit): """)
    if message == 'quit':
        break
    else:
        message = int(message)
        if message < 3:
            print("Your ticket is free!")
        elif 3 <= message < 12:
            print("Your ticket costs $10.")
        else:
            print("Your ticket costs $15.")