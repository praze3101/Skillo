from typing import List

courses: List[str] = ['math', 'physics']
courses.insert(1, 'art')
courses2 = ['sport', 'history']
courses.extend(courses2)
num = [6,8,2,3,5]
sorted_num = sorted(num)
#num.sort(reverse=True)
sorted_courses = sorted(courses)
print(sorted_num)
print(num)

print(sorted_courses)
print('math' in courses)
print(courses.index('math'))
for index,item in enumerate(courses,start=1):
    print(index,item)
course_str = ','.join(courses)
print(course_str)