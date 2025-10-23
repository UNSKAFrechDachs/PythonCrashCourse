class User():
    """Simple user class."""
    def __init__(self, first_name, last_name, favorite_color, birth_date, **additional_info):
        self.first_name = first_name
        self.last_name = last_name
        self.favorite_color = favorite_color
        self.birth_date = birth_date
        self.additional_info = additional_info

    def describe_user(self):
        print(f"""This is {self.first_name.title()} {self.last_name.title()}.
Born on {self.birth_date} and likes the color: {self.favorite_color}.
Here's some additional information: {self.additional_info}.""")

    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}. Nice to see you!")


my_user = User("Max",
               "Mustermann",
               "green",
               "11.09.2002",
               gender="male",
               eye_color="blue")
other_user = User("Marion",
                  "Musterfrau",
                  "fuchsia",
                  "1.1.1980",
                  gender="female",
                  eye_color="blue",
                  hair_color="red",
                  favorite_music="ambient")
my_user.describe_user()
my_user.greet_user()
other_user.describe_user()
other_user.greet_user()