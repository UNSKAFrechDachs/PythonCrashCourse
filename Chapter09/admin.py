from user import User
from privileges import Privileges


class Admin(User):
    """Admin class."""

    def __init__(self, first_name, last_name, favorite_color, birth_date, privileges, **additional_info):
        User.__init__(self, first_name, last_name, favorite_color, birth_date, **additional_info)
        self.privileges = Privileges(privileges)
