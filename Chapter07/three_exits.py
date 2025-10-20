while True:
    message = input("""What topping do you want on your pizza?
   (enter 'quit' to exit) """)
    if message == 'quit':
        break
    else:
        print(f"I'll put {message} on your pizza.")

message = ""
while message != 'quit':
    message = input("""What topping do you want on your pizza?
   (enter 'quit' to exit) """)
    if message == 'quit':
        continue
    print(f"I'll put {message} on your pizza.")

active = True
while active:
    message = input("""What topping do you want on your pizza?
   (enter 'quit' to exit) """)
    if message == 'quit':
        active = False
    else:
        print(f"I'll put {message} on your pizza.")
