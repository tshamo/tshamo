
import datetime


class User:
    """
    A memebr of FriendFace. For now we are
    only storing their name and birthday.
    But soon we will store uncomfortable
    amount of user information. """
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday # yyyymmdd

        # Extract first and last name
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

        self.email = self.first_name.lower() + '.' + self.last_name.lower() + '@company.com'


    def age(self):
        """ Return the age of the use in years. """
        today = datetime.date(2022, 11, 2)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd) # Date of birth
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)

user1 = User("Taulant Shamo", "19781210")
user2 = User("Irena Shamo", "19800722")
print("Name", "Lastname", "Age", "Email")
print(user1.first_name, user1.last_name, user1.age(), user1.email)
print(user2.first_name, user2.last_name, user2.age(), user2.email)