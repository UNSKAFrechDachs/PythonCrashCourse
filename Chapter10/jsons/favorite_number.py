from pathlib import Path
import json


def retrieve_favorite_number(path):
    if path.exists():
        contents = path.read_text()
        number = json.loads(contents)
        return number
    else:
        return None


def store_favorite_number(path):
    number = input("Tell me your favorite number: ")
    content = json.dumps(number)
    path.write_text(content)
    return number


def discuss_favorite_number():
    path = Path("favorite_number.json")
    number = retrieve_favorite_number(path)
    if number:
        print(f"I know your favorite number! It's {number}.")
    else:
        number = store_favorite_number(path)


discuss_favorite_number()