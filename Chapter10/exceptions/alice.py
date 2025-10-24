from pathlib import Path
from word_count import count_words

filenames = ["alice.txt", "little_women.txt", "siddhartha.txt", "moby_dick.txt"]

for filename in filenames:
    path = Path(filename)
    count_words(path)
