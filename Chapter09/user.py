from privileges import Privileges


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


