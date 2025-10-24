from pathlib import Path

path = Path("guest.txt")

guest_name = input("Please enter your name: ")
path.write_text(guest_name)