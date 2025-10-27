from pathlib import Path
import json

numbers = [x**3 for x in range(10)]

path = Path("numbers.json")
contents = json.dumps(numbers)
path.write_text(contents)