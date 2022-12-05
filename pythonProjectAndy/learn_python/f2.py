
def hello_func(greeting, name = 'You'):
    return f'{greeting}, {name}.'

print(hello_func('Hello'))


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', 'Unix', name='Taulant', age=43, phone='555-5555', job='SRE')