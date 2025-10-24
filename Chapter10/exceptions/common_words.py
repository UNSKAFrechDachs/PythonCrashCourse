from pathlib import Path

files = ["alice.txt", "moby_dick.txt"]

for filename in files:
    path = Path(filename)
    contents = path.read_text(encoding="utf-8")
    print(f"{filename} contains {contents.count("the")} times 'the'")
    print(f"{filename} contains {contents.count("the ")} times 'the '")
