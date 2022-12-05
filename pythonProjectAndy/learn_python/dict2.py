student = {'id': 1, 'name': 'John', 'age':25, 'phone': '555-5555', 'courses': ['Math', 'CompSci']}

print(len(student))

print(student.keys())
print(student.values())
print(student.items())

print(student)

for key, value in student.items():
    print(key, value)