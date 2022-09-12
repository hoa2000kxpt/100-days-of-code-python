"""
# Old approach:

numbers = [1, 2, 3]

new_list = []

for n in numbers:

    add_1 = n + 1

    new_list.append(add_1)

print(new_list)
# New approach: List Comprehension

new_list = [n + 1 for n in numbers]
print(new_list)

double_num = [num * 2 for num in range(1, 5)]
print(double_num)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', ''Freddie]
upper_name = [name.upper() for name in names if len(name) > 5]

students_scores = {student:random.randint(1, 100) for student in names}
passed_students = {student:score for (student, score0) in students_scores.item() if score >= 60}
"""




