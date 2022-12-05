

class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'


    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod ## do not use class method at all
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:  # Sat or Sun
            return False
        return True

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname,self.email)

emp_1 = Employee('Andy', 'Shamo', 5000)
emp_2 = Employee('Taulant', 'Shamo', 80000)

emp_str_1 = 'John-Doe-7000'

new_emp_1 = Employee.from_string(emp_str_1)

'''print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())
print(emp_2.fullname())

Employee.fullname(emp_1)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

emp_1.raise_amount = 1.05'''


print(emp_1.__repr__())
print(emp_2.__str__())

#Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(new_emp_1.email)
print(new_emp_1.pay)

import datetime

my_date = datetime.date(2022, 12, 3)

print(Employee.is_workday(my_date))