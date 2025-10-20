while True:
   message = input("""What topping do you want on your pizza?
   (enter 'quit' to exit) """)
   if message == 'quit':
       break
   else:
       print(f"I'll put {message} on your pizza.")