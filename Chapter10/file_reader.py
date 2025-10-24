from pathlib import Path

path = Path("pi_million_digits.txt")
contents = path.read_text()
pi_string = ""
for line in contents.splitlines():
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
