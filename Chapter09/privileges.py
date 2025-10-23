class Privileges:
    """Class Privileges."""
    def __init__(self, privileges):
        self.privileges = privileges
    def show_privileges(self):
        print("Available privileges:")
        for privilege in self.privileges:
            print(f"\t- {privilege}")
