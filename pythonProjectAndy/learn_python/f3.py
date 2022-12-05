

def student_info(*args, **kwargs): # accept many
    print(args)
    print(kwargs)

courses = ['Math', 'Art', 'Unix']
info = {'name': 'Taulant', 'age': 43, 'phone': '555-5555', 'job': 'SRE'}

student_info(courses, info)     #
student_info(*courses, **info)  # unpact values