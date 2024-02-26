# This program will use the capabilities of Panda's dataframes
# It will print the results of the tests in a readable format

import pandas as pd

#A
print("Section A")
temperature_a = {
    'Maxine': [90, 92, 89],
    'James': [93, 91, 94],
    'Amanda': [88, 90.1, 91]
}
section_a = pd.DataFrame(temperature_a)
print("The result of Section A is")
print(section_a)
#B
print('')
print("Section B")
section_b = pd.DataFrame(temperature_a, ["Morning", "Afternoon", "Evening"])
print("The result of Section B is")
print(section_b)
#C
print('')
print("Section C")
print("The result of Section C is")
print(section_b['Maxine'])
#D
print('')
print("Section D")
print("The result of Section D is")
print(section_b.loc['Morning'])
#E
print('')
print("Section E")
print("The result of Section E is")
print(section_b.loc[['Morning', 'Evening']])
#F
print('')
print("Section F")
print("The result of Section F is")
print(section_b[['Amanda', 'Maxine']])
#G
print('')
print("Section G")
print("The result of Section G is")
print(section_b[['Amanda', 'Maxine']].loc[['Morning', 'Afternoon']])
#H
print('')
print("Section H")
print("The result of Section H is")
temperatures_description = section_b.describe()
print(temperatures_description)
#I
print('')
print("Section I")
print("The result of Section I is")
transposed_temperature = section_b.T
print(transposed_temperature)
#J
print('')
print("Section J")
print("The result of Section J is")
sorted_temperature = section_b.sort_index(axis=1)
print(sorted_temperature)
