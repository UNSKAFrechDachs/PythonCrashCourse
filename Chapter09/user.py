class User:
    """Simple user class."""
    def __init__(self, first_name, last_name, favorite_color, birth_date, **additional_info):
        self.first_name = first_name
        self.last_name = last_name
        self.favorite_color = favorite_color
        self.birth_date = birth_date
        self.additional_info = additional_info
        self.login_attempts = 0

    def describe_user(self):
        print(f"""This is {self.first_name.title()} {self.last_name.title()}.
Born on {self.birth_date} and likes the color: {self.favorite_color}.
Here's some additional information: {self.additional_info}.""")

    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}. Nice to see you!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    """Admin class."""
    def __init__(self, first_name, last_name, favorite_color, birth_date, privileges, **additional_info):
        User.__init__(self, first_name, last_name, favorite_color, birth_date, **additional_info)
        self.privileges = Privileges(privileges)

class Privileges:
    """Class Privileges."""
    def __init__(self, privileges):
        self.privileges = privileges
    def show_privileges(self):
        print("Available privileges:")
        for privilege in self.privileges:
            print(f"\t- {privilege}")

my_user = User("Max",
               "Mustermann",
               "green",
               "11.09.2002",
               gender="male",
               eye_color="blue")
other_user = Admin("Marion",
                  "Musterfrau",
                  "fuchsia",
                  "1.1.1980",
                   privileges=["Can ban"],
                  gender="female",
                  eye_color="blue",
                  hair_color="red",
                  favorite_music="ambient")
my_user.describe_user()
my_user.greet_user()
other_user.describe_user()
other_user.greet_user()


for _ in range(15):
    my_user.increment_login_attempts()
    print(my_user.login_attempts)
my_user.reset_login_attempts()
print(my_user.login_attempts)
other_user.privileges.show_privileges()