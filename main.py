print('Welcome to Grading Program !')
student_scores = {
    'Ram': 81,
    'Shyam': 78,
    'Hari': 99,
    'Sita': 74,
    'Gita': 62,
}

student_grades = {}
for i in student_scores:
    if 90 < student_scores[i] <= 100:
        student_grades[i] = 'Outstanding'
    elif 80 < student_scores[i] <= 90:
        student_grades[i] = 'Exceeds Expectations'
    elif 70 < student_scores[i] <= 80:
        student_grades[i] = 'Acceptable'
    elif 60 < student_scores[i] <= 70:
        student_grades[i] = 'Fail'
print(student_grades)
