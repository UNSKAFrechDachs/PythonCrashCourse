from pathlib import Path
import json


def get_stored_user(path):
    """Tries to get the user. Returns None if not found."""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None


def get_new_user(path: Path):
    """Gets new user from input and saves it to path."""
    user_info = {"name": input("Enter your username: "),
                 "height": int(input("Enter your height in cm: ")),
                 "age": int(input("Enter your age: "))}

    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info


def check_username(current_name):
    new_name = input("Enter your username: ")
    return new_name.lower() == current_name.lower()


def greet_user():
    path = Path("user.json")
    user_info = get_stored_user(path)
    if user_info:
        if input(f"Are you {user_info['name']}? (y/n) ").lower() == "y":
            print(f"Welcome back, {user_info["name"]}!")
            print(f"You are {user_info["height"]} cm tall")
            print(f"You are {user_info["age"]} years old")
            return

    user_info = get_new_user(path)
    print(f"We'll remember you when you come back, {user_info['name']}!")


greet_user()
