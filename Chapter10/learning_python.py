from pathlib import Path

path = Path("learning_python.txt")
entire_file = path.read_text()

print(f"{entire_file}\n\n")
for line in path.read_text().splitlines():
    print(line)