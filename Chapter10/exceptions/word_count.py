def count_words(path):
    """Counts the number of words in a file."""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Sorry, the file {path} doesn't exist.")
    else:
        num_words = len(contents.split())
        print(f"There are {num_words} words in {path}.")