# This program will allow an instructor to store student exam info
# It will write to a json file

import json
done = False
gradebook_dict = {'students': []}

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
        
        student_data = {
            'first_name': firstname,
            'last_name': lastname,
            'exam1': exam1grade,
            'exam2': exam2grade,
            'exam3': exam3grade
        }
        gradebook_dict['students'].append(student_data)
    except ValueError:
        print("### ERROR ###         Check your format")
    

with open('grades.json', 'w') as json_file:
    json.dump(gradebook_dict, json_file, indent=4)