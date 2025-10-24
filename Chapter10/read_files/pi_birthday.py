from pathlib import Path

path = Path("pi_million_digits.txt")
lines = path.read_text().splitlines()
pi_string = ""
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form ddmmyy: ")
if birthday in pi_string:
    print("It is in the first million digits!")
else:
    print("It is not in the first million digits :(")