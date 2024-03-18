# This program will read from the grades.csv file
# It will then display in a tabular format

import csv


print("{:<10} {:<10} {:<10} {:<10} {:<10}".format("Firstname", "Lastname", "Exam1", "Exam2", "Exam3"))
with open('grades.csv', mode='r') as file:
    reader = csv.reader(file)
    for record in reader:
        firstname, lastname, exam1, exam2, exam3 = record
        print("{:<10} {:<10} {:<10} {:<10} {:<10}".format(firstname, lastname, exam1, exam2, exam3))
