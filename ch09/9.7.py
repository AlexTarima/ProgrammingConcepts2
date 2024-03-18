# This program will read from the grades.csv file
# It will then display in a tabular format

import json

with open('grades.json', 'r') as json_file:
    grades = json.load(json_file)

print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("Firstname", "Lastname", "Exam1", "Exam2", "Exam3", "Average"))
exam1_total = 0
exam2_total = 0
exam3_total = 0
exam_count = 0
with open('grades.csv', mode='r') as file:
    for student in grades['students']:
        firstname = student['first_name']
        lastname = student['last_name']
        exam1 = student['exam1']
        exam2 = student['exam2']
        exam3 = student['exam3']
        exam1_total += exam1
        exam2_total += exam2
        exam3_total += exam3
        exam_count += 1
        average = exam1 + exam2 + exam3
        print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(firstname, lastname, exam1, exam2, exam3, average))

    exam1_average = "{:.2f}".format(exam1_total/exam_count)
    exam2_average = "{:.2f}".format(exam2_total/exam_count)
    exam3_average = "{:.2f}".format(exam3_total/exam_count)
    print('-' * 60)
    print("{:<10} {:<10} {:<10} {:<10} {:<10}".format("Class", "Average:", exam1_average, exam2_average, exam3_average))
