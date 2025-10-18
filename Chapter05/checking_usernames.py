current_users = ["jesse", "walter", "mike", "jim", "pam", "admin"]
new_users = ["skylar", "mike", "dwight", "gustavo", "erin"]

lowercase_current_users = [name.lower() for name in current_users]
for user in new_users:
    if user.lower() in lowercase_current_users:
        print("This name is already taken, please choose another.")
    else:
        print("This name is available!")