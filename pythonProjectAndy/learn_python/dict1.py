student = {'id': 1, 'name': 'John', 'age':25, 'courses': ['Math', 'CompSci']}

print(student)
print(student.get('phone','Not Found'))

student.update({'name': 'Jane', 'age':30, 'phone': '555-5555'})

print(student.get('phone','Not Found'))  ## this is better for scenariuos that key you are searching does not exists in the dictory. Rather than throwing errors
print(student)