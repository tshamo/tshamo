from typing import List

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']

nums = [1, 3, 5, 2, 4]
nums_2 = [6, 8, 7, 9]
#courses.extend(courses_2)

#courses.pop('Math')
nums.extend(nums_2)

sorted_courses = sorted(courses)

courses.sort(reverse=True)
nums.sort()

#print(nums)
print(courses)
print(sorted_courses)
print('Art' in courses)

'''
for item in sorted_courses:
    print(item)
'''
for index, course in enumerate(sorted_courses, start=1):
    print(index, course)

# join as string with comma separator - split list to strings
course_str = ', '.join(courses)

# split - build list from strings
new_list = course_str.split(',')

print(course_str)
print(new_list)