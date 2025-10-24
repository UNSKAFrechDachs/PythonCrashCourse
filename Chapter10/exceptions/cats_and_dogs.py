from pathlib import Path

try:
    cats = Path("cats.txt").read_text()
    dogs = Path("dogs.txt").read_text()
except FileNotFoundError:
    #print("File not found")
    pass
else:
    print(cats)
    print(dogs)