from pathlib import  Path

path = Path("learning_python.txt")
file = path.read_text().replace("Python", "Kotlin")
print(file)