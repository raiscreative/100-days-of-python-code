num_students = int(input('How many students do you have?'))
student_scores = {}
for i in range(1, num_students +1):
    student = input(f'Student {i} name and score:').split()
    student_name = student[0]
    student_score = int(student[1])
    student_scores[student_name] = student_score
student_grades = {}
for student in student_scores:
    if student_scores[student] > 90:
        student_grades[student] = 'Outstanding'
    elif student_scores[student] > 80:
        student_grades[student] = 'Exceeds Expectations'
    elif student_scores[student] > 80:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'
for student in student_grades:
    print(f'{student}\'s grade: {student_grades[student]}')