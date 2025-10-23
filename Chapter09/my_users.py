from user import User
from admin import Admin

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
