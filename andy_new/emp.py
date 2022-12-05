
import datetime


class User:
    """
EXPLAIN THE CLASS

 """
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = User("Taulant", "Shamo", 50000)
emp_2 = User("Andy", "Shamo", 100000)

print(emp_1.email, emp_1.fullname())
print(emp_2.email, emp_2.fullname())