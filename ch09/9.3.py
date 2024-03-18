# This program will allow an instructor to store student exam info
# It will write to a csv file
import csv
done = False

with open('grades.csv', mode='w', newline='') as output_file:
    while not done:
        print("Write done if done")
        inputs = input("Enter firstname, lastname, exam1grade, exam2grade, exam3grade: ")
        if inputs.strip().lower() == 'done':
            done = True
            break
        try:
            firstname,lastname,exam1grade,exam2grade,exam3grade = map(str.strip, inputs.split(','))
            exam1grade = int(exam1grade)
            exam2grade = int(exam2grade)
            exam3grade = int(exam3grade)
            
            writer = csv.writer(output_file)
            writer.writerow([firstname, lastname, exam1grade, exam2grade, exam3grade])
        except ValueError:
            print("### ERROR ###         Check your format")
        

