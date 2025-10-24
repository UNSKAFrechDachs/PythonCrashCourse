from pathlib import Path

path = Path("guest_book.txt")

guests = "Our guests:"

while True:
    guest_name = input("Please enter your name, or input 'q' to quit: ")
    if guest_name == "q":
        print("Exiting...")
        break
    guests += "\n\t" + guest_name

path.write_text(guests)